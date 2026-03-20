"""Action handler seed for fulfillment_case:assign."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "fulfillment_case"
ACTION_ID = "assign"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['opened', 'assigned', 'in_progress', 'resolved', 'escalated'], 'transitions_to': 'in_progress'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['order_record', 'order_line', 'shipment_record', 'delivery_exception_case'], 'borrowed_fields': ['order/line context from linked records'], 'inferred_roles': ['account owner', 'operations coordinator', 'case owner']}, 'actors': ['account owner', 'operations coordinator', 'case owner'], 'action_actors': {'create': ['account owner'], 'assign': ['account owner'], 'review': ['operations coordinator'], 'close': ['account owner'], 'archive': ['account owner']}}

ACTION_CONTRACT: dict[str, Any] = {'rule': {'allowed_in_states': ['opened', 'assigned', 'in_progress', 'resolved', 'escalated'], 'transitions_to': 'in_progress'}, 'requires_action_comment': False, 'requires_reason_for_change': False, 'requires_evidence': False, 'is_disposition_action': False, 'creates_submission_snapshot': False, 'creates_official_copy': False, 'requires_signature': False}

def handle_assign(payload: dict, context: dict | None = None) -> dict:
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
