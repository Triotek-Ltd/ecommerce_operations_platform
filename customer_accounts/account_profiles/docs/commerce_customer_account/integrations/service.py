"""Integration-service seed for commerce_customer_account."""

from __future__ import annotations


DOC_ID = "commerce_customer_account"
INTEGRATION_RULES = {'external_refs': [{'field_id': 'source_customer_reference', 'kind': 'customer', 'label': 'Source Customer Reference'}], 'sync_rules': []}

class IntegrationService:
    def sync_rules(self) -> list:
        return INTEGRATION_RULES.get("sync_rules", [])

    def integration_profile(self) -> dict:
        return {'external_sync_enabled': False}
