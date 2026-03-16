"""Action handler seed for refund_case:reject."""

from __future__ import annotations


DOC_ID = "refund_case"
ACTION_ID = "reject"
ACTION_RULE = {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'refunded'], 'transitions_to': 'rejected'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['payment_attempt', 'adjustment_record', 'chargeback_case', 'marketplace_return_case'], 'borrowed_fields': ['source payment/order context from linked records'], 'inferred_roles': ['account owner', 'finance officer', 'case owner']}, 'actors': ['account owner', 'finance officer', 'case owner'], 'action_actors': {'create': ['account owner'], 'review': ['finance officer'], 'approve': ['finance officer'], 'reject': ['finance officer'], 'close': ['account owner'], 'archive': ['account owner']}}

def handle_reject(payload: dict, context: dict | None = None) -> dict:
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
