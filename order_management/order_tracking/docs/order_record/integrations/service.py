"""Integration-service seed for order_record."""

from __future__ import annotations


DOC_ID = "order_record"
INTEGRATION_RULES = {'external_refs': [{'field_id': 'source_reference', 'kind': 'source', 'label': 'Source Reference'}], 'sync_rules': []}

class IntegrationService:
    def sync_rules(self) -> list:
        return INTEGRATION_RULES.get("sync_rules", [])

    def integration_profile(self) -> dict:
        return {'external_sync_enabled': True, 'tracks_external_refs': True}
