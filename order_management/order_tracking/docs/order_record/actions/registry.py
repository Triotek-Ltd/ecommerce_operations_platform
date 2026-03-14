"""Action registry seed for order_record."""

from __future__ import annotations


DOC_ID = "order_record"
ALLOWED_ACTIONS = ['create', 'confirm', 'update_status', 'cancel', 'close', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['placed', 'confirmed', 'partially_fulfilled', 'fulfilled', 'cancelled'], 'transitions_to': None}, 'confirm': {'allowed_in_states': ['placed', 'confirmed', 'partially_fulfilled', 'fulfilled', 'cancelled'], 'transitions_to': 'confirmed'}, 'update_status': {'allowed_in_states': ['placed', 'confirmed', 'partially_fulfilled', 'fulfilled', 'cancelled'], 'transitions_to': None}, 'cancel': {'allowed_in_states': ['placed', 'confirmed', 'partially_fulfilled', 'fulfilled', 'cancelled'], 'transitions_to': None}, 'close': {'allowed_in_states': ['placed', 'confirmed', 'partially_fulfilled', 'fulfilled', 'cancelled'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['placed', 'confirmed', 'partially_fulfilled', 'fulfilled', 'cancelled'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'

def get_action_handler_name(action_id: str) -> str:
    return f"handle_{action_id}"

def get_action_module_path(action_id: str) -> str:
    return f"actions/{action_id}.py"

def action_contract(action_id: str) -> dict:
    return {
        "state_field": STATE_FIELD,
        "rule": ACTION_RULES.get(action_id, {}),
    }
