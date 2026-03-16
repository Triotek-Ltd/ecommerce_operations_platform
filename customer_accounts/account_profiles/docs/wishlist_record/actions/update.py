"""Action handler seed for wishlist_record:update."""

from __future__ import annotations


DOC_ID = "wishlist_record"
ACTION_ID = "update"
ACTION_RULE = {'allowed_in_states': ['active', 'converted', 'removed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['commerce_customer_account', 'catalog_product', 'order_record'], 'borrowed_fields': ['account identity from commerce_customer_account', 'product display context from catalog_product'], 'inferred_roles': ['account owner']}, 'actors': ['account owner'], 'action_actors': {'create': ['account owner'], 'update': ['account owner'], 'archive': ['account owner']}}

def handle_update(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = ACTION_RULE.get("transitions_to")
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
