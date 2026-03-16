"""Action handler seed for fulfillment_case:review."""

from __future__ import annotations


DOC_ID = "fulfillment_case"
ACTION_ID = "review"
ACTION_RULE = {'allowed_in_states': ['opened', 'assigned', 'in_progress', 'resolved', 'escalated'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['order_record', 'order_line', 'shipment_record', 'delivery_exception_case'], 'borrowed_fields': ['order/line context from linked records'], 'inferred_roles': ['account owner', 'operations coordinator', 'case owner']}, 'actors': ['account owner', 'operations coordinator', 'case owner'], 'action_actors': {'create': ['account owner'], 'assign': ['account owner'], 'review': ['operations coordinator'], 'close': ['account owner'], 'archive': ['account owner']}}

def handle_review(payload: dict, context: dict | None = None) -> dict:
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
