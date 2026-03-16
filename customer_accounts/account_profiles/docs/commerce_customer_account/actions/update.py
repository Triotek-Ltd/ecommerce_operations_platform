"""Action handler seed for commerce_customer_account:update."""

from __future__ import annotations


DOC_ID = "commerce_customer_account"
ACTION_ID = "update"
ACTION_RULE = {'allowed_in_states': ['active', 'suspended'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['account_activity_log', 'wishlist_record', 'purchase_history_snapshot', 'customer_account'], 'borrowed_fields': ['base customer identity from sales/CRM customer_account'], 'inferred_roles': ['procurement officer', 'account owner']}, 'actors': ['procurement officer', 'account owner'], 'action_actors': {'create': ['procurement officer'], 'update': ['procurement officer'], 'archive': ['account owner']}}

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
