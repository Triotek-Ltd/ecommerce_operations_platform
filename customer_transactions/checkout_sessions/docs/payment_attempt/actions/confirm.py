"""Action handler seed for payment_attempt:confirm."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "payment_attempt"
ACTION_ID = "confirm"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['initiated', 'processing', 'succeeded', 'failed', 'cancelled'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['checkout_session', 'order_record', 'payment_intent_record', 'card_authorization_record', 'mobile_money_transaction'], 'borrowed_fields': ['checkout/order context from linked records', 'external payment references from payment integration docs'], 'inferred_roles': ['approver', 'account owner', 'finance officer']}, 'actors': ['approver', 'account owner', 'finance officer'], 'action_actors': {'create': ['approver'], 'confirm': ['approver'], 'cancel': ['account owner'], 'archive': ['account owner']}}

ACTION_CONTRACT: dict[str, Any] = {'rule': {'allowed_in_states': ['initiated', 'processing', 'succeeded', 'failed', 'cancelled'], 'transitions_to': None}, 'requires_action_comment': False, 'requires_reason_for_change': False, 'requires_evidence': False, 'is_disposition_action': False, 'creates_submission_snapshot': False, 'creates_official_copy': False, 'requires_signature': False}

def handle_confirm(payload: dict, context: dict | None = None) -> dict:
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
