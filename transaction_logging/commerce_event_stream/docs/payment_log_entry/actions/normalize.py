"""Action handler seed for payment_log_entry:normalize."""

from __future__ import annotations


DOC_ID = "payment_log_entry"
ACTION_ID = "normalize"
ACTION_RULE = {'allowed_in_states': ['active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['payment_attempt', 'processor_event_log', 'card_authorization_record', 'mobile_money_transaction'], 'borrowed_fields': ['payment/provider context from linked records'], 'inferred_roles': ['approver', 'finance officer']}, 'actors': ['approver', 'finance officer'], 'action_actors': {'record': ['approver'], 'archive': ['approver']}}

def handle_normalize(payload: dict, context: dict | None = None) -> dict:
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
