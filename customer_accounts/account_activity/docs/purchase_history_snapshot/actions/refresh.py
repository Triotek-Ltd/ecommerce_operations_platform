"""Action handler seed for purchase_history_snapshot:refresh."""

from __future__ import annotations


DOC_ID = "purchase_history_snapshot"
ACTION_ID = "refresh"
ACTION_RULE = {'allowed_in_states': ['active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['commerce_customer_account', 'order_record', 'account_activity_log'], 'borrowed_fields': ['order', 'account context from linked docs'], 'inferred_roles': ['procurement officer', 'account owner']}, 'actors': ['procurement officer', 'account owner'], 'action_actors': {'create': ['procurement officer'], 'archive': ['account owner']}}

def handle_refresh(payload: dict, context: dict | None = None) -> dict:
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
