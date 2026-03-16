"""Action handler seed for checkout_session:create."""

from __future__ import annotations


DOC_ID = "checkout_session"
ACTION_ID = "create"
ACTION_RULE = {'allowed_in_states': ['open', 'in_progress', 'completed', 'abandoned', 'failed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['payment_attempt', 'order_record', 'commerce_customer_account'], 'borrowed_fields': ['customer/account context from commerce_customer_account'], 'inferred_roles': ['account owner', 'finance officer']}, 'actors': ['account owner', 'finance officer'], 'action_actors': {'create': ['account owner'], 'archive': ['account owner']}}

def handle_create(payload: dict, context: dict | None = None) -> dict:
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
