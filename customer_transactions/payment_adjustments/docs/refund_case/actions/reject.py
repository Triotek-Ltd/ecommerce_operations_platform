"""Action handler seed for refund_case:reject."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "refund_case"
ACTION_ID = "reject"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'refunded'], 'transitions_to': 'rejected'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['payment_attempt', 'adjustment_record', 'chargeback_case', 'marketplace_return_case'], 'borrowed_fields': ['source payment/order context from linked records'], 'inferred_roles': ['account owner', 'finance officer', 'case owner']}, 'actors': ['account owner', 'finance officer', 'case owner'], 'action_actors': {'create': ['account owner'], 'review': ['finance officer'], 'approve': ['finance officer'], 'reject': ['finance officer'], 'close': ['account owner'], 'archive': ['account owner']}}

ACTION_CONTRACT: dict[str, Any] = {'rule': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'refunded'], 'transitions_to': 'rejected'}, 'requires_action_comment': False, 'requires_reason_for_change': False, 'requires_evidence': False, 'is_disposition_action': False, 'creates_submission_snapshot': False, 'creates_official_copy': False, 'requires_signature': False}

def handle_reject(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = cast(str | None, ACTION_RULE.get("transitions_to"))
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "action_contract": ACTION_CONTRACT,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
