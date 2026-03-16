"""Action handler seed for order_line:archive."""

from __future__ import annotations


DOC_ID = "order_line"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['active', 'fulfilled', 'cancelled', 'returned'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['order_record', 'catalog_product', 'fulfillment_case'], 'borrowed_fields': ['catalog/product context from catalog_product', 'order header context from order_record'], 'inferred_roles': ['account owner', 'case owner']}, 'actors': ['account owner', 'case owner'], 'action_actors': {'record': ['account owner'], 'archive': ['account owner']}}

def handle_archive(payload: dict, context: dict | None = None) -> dict:
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
