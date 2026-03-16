"""Action handler seed for order_status_event:record."""

from __future__ import annotations


DOC_ID = "order_status_event"
ACTION_ID = "record"
ACTION_RULE = {'allowed_in_states': ['active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['order_record', 'commerce_event_log', 'payment_log_entry'], 'borrowed_fields': ['order identity from order_record'], 'inferred_roles': ['account owner', 'finance officer']}, 'actors': ['account owner', 'finance officer'], 'action_actors': {'record': ['account owner'], 'archive': ['account owner']}}

def handle_record(payload: dict, context: dict | None = None) -> dict:
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
