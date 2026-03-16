"""Business-domain service seed for Order Record."""

from __future__ import annotations


ARCHETYPE_PROFILE = {'workflow_profile': {'mode': 'transaction_flow', 'supports_submission': True}, 'reporting_profile': {'supports_snapshots': True, 'supports_outputs': True}, 'integration_profile': {'external_sync_enabled': True, 'tracks_external_refs': True}, 'lifecycle_states': ['placed', 'confirmed', 'partially_fulfilled', 'fulfilled', 'cancelled', 'closed', 'archived'], 'is_transactional': True}

CONTRACT = {'title_field': 'title', 'status_field': 'workflow_state', 'reference_field': 'reference_no', 'required_fields': ['title', 'workflow_state', 'transaction_date'], 'field_purposes': {'workflow_state': 'lifecycle_state', 'transaction_date': 'transaction_date', 'party': 'primary_party', 'currency': 'currency_code', 'total_amount': 'total_amount', 'order_date': 'schedule_marker', 'order_status': 'status_flag', 'related_order_line': 'relation_collection', 'related_fulfillment_case': 'relation_collection', 'related_payment_attempt': 'relation_collection', 'related_shipment_record': 'relation_collection'}, 'search_fields': ['title', 'reference_no', 'description', 'order_code', 'source_reference', 'external_account_reference'], 'list_columns': ['title', 'reference_no', 'transaction_date', 'party', 'total_amount', 'workflow_state'], 'initial_state': 'placed', 'lifecycle_states': ['placed', 'confirmed', 'partially_fulfilled', 'fulfilled', 'cancelled', 'closed', 'archived'], 'terminal_states': ['closed', 'archived'], 'action_targets': {'create': None, 'confirm': 'confirmed', 'update_status': None, 'cancel': None, 'close': 'closed', 'archive': 'archived'}}

WORKFLOW_HINTS = {'business_objective': 'track order progression from placement through fulfillment and closure while preserving a complete status trail', 'actors': ['commerce engine', 'fulfillment owner', 'exception handler'], 'start_condition': 'a platform order is placed', 'ordered_steps': ['Create the order record.', 'Confirm the order.', 'Emit status events as the order changes.', 'Close or cancel the order.'], 'primary_actions': ['create', 'confirm', 'update_status', 'cancel', 'close'], 'action_actors': {'create': ['commerce engine'], 'confirm': ['commerce engine'], 'update_status': ['fulfillment owner', 'exception handler'], 'cancel': ['exception handler'], 'close': ['fulfillment owner'], 'archive': ['fulfillment owner']}, 'primary_transitions': ['order_record: placed -> confirmed -> fulfilled -> closed', 'order_record: placed -> cancelled'], 'downstream_effects': ['creates status history and fulfillment follow-up records for customer visibility and operations control']}

SIDE_EFFECT_HINTS = {'downstream_effects': ['creates status history and fulfillment follow-up records for customer visibility and operations control'], 'related_docs': ['order_line', 'order_status_event', 'fulfillment_case', 'payment_attempt', 'shipment_record'], 'action_targets': {'create': None, 'confirm': 'confirmed', 'update_status': None, 'cancel': None, 'close': 'closed', 'archive': 'archived'}, 'action_side_effects_file': 'side_effects.json'}

class DomainService:
    doc_id = "order_record"
    archetype = "transaction"
    doc_kind = "transaction"

    def required_fields(self) -> list[str]:
        return CONTRACT.get("required_fields", [])

    def state_field(self) -> str | None:
        return CONTRACT.get("status_field")

    def default_state(self) -> str | None:
        return CONTRACT.get("initial_state")

    def list_columns(self) -> list[str]:
        return CONTRACT.get("list_columns", [])

    def validate_invariants(self, payload: dict, *, partial: bool = False) -> dict:
        if partial:
            required_scope = [field for field in self.required_fields() if field in payload]
        else:
            required_scope = self.required_fields()
        missing_fields = [field for field in required_scope if not payload.get(field)]
        if missing_fields:
            raise ValueError(f"Missing required business fields: {', '.join(missing_fields)}")
        state_field = self.state_field()
        allowed_states = set(CONTRACT.get("lifecycle_states", []))
        if state_field and payload.get(state_field) and allowed_states and payload[state_field] not in allowed_states:
            raise ValueError(f"Invalid state '{payload[state_field]}' for {state_field}")
        return payload

    def prepare_create_payload(self, payload: dict, context: dict | None = None) -> dict:
        payload = dict(payload)
        state_field = self.state_field()
        if state_field and not payload.get(state_field) and self.default_state():
            payload[state_field] = self.default_state()
        title_field = CONTRACT.get("title_field")
        reference_field = CONTRACT.get("reference_field")
        if title_field and not payload.get(title_field) and reference_field and payload.get(reference_field):
            payload[title_field] = str(payload[reference_field])
        payload = self.validate_invariants(payload)
        return payload

    def after_create(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        return serialized_data

    def prepare_update_payload(self, instance, payload: dict, context: dict | None = None) -> dict:
        payload = dict(payload)
        payload = self.validate_invariants(payload, partial=True)
        return payload

    def after_update(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        return serialized_data

    def after_action(
        self,
        instance,
        action_id: str,
        payload: dict,
        action_result: dict,
        context: dict | None = None,
    ) -> dict:
        return {
            "updates": {},
            "side_effects": [],
        }

    def shape_retrieve_data(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        serialized_data.setdefault("_business_capabilities", self.business_capabilities())
        return serialized_data

    def workflow_objective(self) -> str | None:
        return WORKFLOW_HINTS.get("business_objective")

    def side_effect_hints(self) -> dict:
        return SIDE_EFFECT_HINTS

    def business_capabilities(self) -> dict:
        return {
            **ARCHETYPE_PROFILE,
            "required_fields": self.required_fields(),
            "state_field": self.state_field(),
            "default_state": self.default_state(),
        }
