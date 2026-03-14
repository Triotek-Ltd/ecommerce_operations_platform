"""Doc runtime hooks for catalog_change_log."""

class DocRuntime:
    doc_key = "catalog_change_log"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'archive']
