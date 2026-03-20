"""Action handler seed for order_record:update_status."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "order_record"
ACTION_ID = "update_status"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['placed', 'confirmed', 'partially_fulfilled', 'fulfilled', 'cancelled'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'track order progression from placement through fulfillment and closure while preserving a complete status trail', 'actors': ['commerce engine', 'fulfillment owner', 'exception handler'], 'start_condition': 'a platform order is placed', 'ordered_steps': ['Create the order record.', 'Confirm the order.', 'Emit status events as the order changes.', 'Close or cancel the order.'], 'primary_actions': ['create', 'confirm', 'update_status', 'cancel', 'close'], 'action_actors': {'create': ['commerce engine'], 'confirm': ['commerce engine'], 'update_status': ['fulfillment owner', 'exception handler'], 'cancel': ['exception handler'], 'close': ['fulfillment owner'], 'archive': ['fulfillment owner']}, 'primary_transitions': ['order_record: placed -> confirmed -> fulfilled -> closed', 'order_record: placed -> cancelled'], 'downstream_effects': ['creates status history and fulfillment follow-up records for customer visibility and operations control']}

ACTION_CONTRACT: dict[str, Any] = {'rule': {'allowed_in_states': ['placed', 'confirmed', 'partially_fulfilled', 'fulfilled', 'cancelled'], 'transitions_to': None}, 'requires_action_comment': False, 'requires_reason_for_change': False, 'requires_evidence': False, 'is_disposition_action': False, 'creates_submission_snapshot': False, 'creates_official_copy': False, 'requires_signature': False}

def handle_update_status(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = cast(str | None, ACTION_RULE.get("transitions_to"))
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "action_contract": ACTION_CONTRACT,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
