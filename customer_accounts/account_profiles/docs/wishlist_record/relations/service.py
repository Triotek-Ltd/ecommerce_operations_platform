"""Relation service seed for wishlist_record."""

from __future__ import annotations

from core.services.relation_resolution import RelationResolutionService


DOC_ID = "wishlist_record"
RELATED_DOCS = [{'doc_id': 'commerce_customer_account', 'relation_type': 'related', 'show_in_related_panel': True}, {'doc_id': 'catalog_product', 'relation_type': 'related', 'show_in_related_panel': True}, {'doc_id': 'order_record', 'relation_type': 'related', 'show_in_related_panel': True}, {'doc_id': 'party_record', 'relation_type': 'related', 'show_in_related_panel': True}]
FETCH_RULES = [{'source_field': 'party', 'doc_id': 'party_record', 'mode': 'context'}, {'source_field': 'customer_account', 'doc_id': 'commerce_customer_account', 'mode': 'context'}, {'source_field': 'related_order_record', 'doc_id': 'order_record', 'mode': 'context'}]

BORROWED_FIELDS = [{'description': 'account identity from commerce_customer_account'}, {'description': 'product display context from catalog_product'}, {'field_id': 'party', 'doc_id': 'party_record', 'description': 'Borrow context from party_record through party.'}, {'field_id': 'customer_account', 'doc_id': 'commerce_customer_account', 'description': 'Borrow context from commerce_customer_account through customer_account.'}, {'field_id': 'related_order_record', 'doc_id': 'order_record', 'description': 'Borrow context from order_record through related_order_record.'}]

class RelationService:
    def _bridge(self, context: dict | None = None) -> RelationResolutionService | None:
        viewset = (context or {}).get("viewset")
        return RelationResolutionService(viewset) if viewset is not None else None

    def resolve_create_relations(self, payload: dict, context: dict | None = None) -> dict:
        bridge = self._bridge(context)
        return bridge.resolve_create_relations(payload) if bridge else {"data": payload}

    def resolve_update_relations(self, instance, payload: dict, context: dict | None = None) -> dict:
        bridge = self._bridge(context)
        return bridge.resolve_update_relations(instance, payload) if bridge else {"data": payload}

    def shape_retrieve_data(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        bridge = self._bridge(context)
        return bridge.serialize_related(instance, serialized_data) if bridge else serialized_data

    def related_targets(self) -> list:
        return RELATED_DOCS

    def borrowed_field_notes(self) -> list:
        return [item.get("description") for item in BORROWED_FIELDS if isinstance(item, dict)]

    def relation_profile(self) -> dict:
        return {
            "related_docs": self.related_targets(),
            "borrowed_fields": self.borrowed_field_notes(),
            "fetch_rule_count": len(FETCH_RULES),
        }
