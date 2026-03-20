"""Action handler seed for checkout_session:fail."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "checkout_session"
ACTION_ID = "fail"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['open', 'in_progress', 'completed', 'abandoned', 'failed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['payment_attempt', 'order_record', 'commerce_customer_account'], 'borrowed_fields': ['customer/account context from commerce_customer_account'], 'inferred_roles': ['account owner', 'finance officer']}, 'actors': ['account owner', 'finance officer'], 'action_actors': {'create': ['account owner'], 'archive': ['account owner']}}

ACTION_CONTRACT: dict[str, Any] = {'rule': {'allowed_in_states': ['open', 'in_progress', 'completed', 'abandoned', 'failed'], 'transitions_to': None}, 'requires_action_comment': False, 'requires_reason_for_change': False, 'requires_evidence': False, 'is_disposition_action': False, 'creates_submission_snapshot': False, 'creates_official_copy': False, 'requires_signature': False}

def handle_fail(payload: dict, context: dict | None = None) -> dict:
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
