"""Doc runtime hooks for purchase_history_snapshot."""

class DocRuntime:
    doc_key = "purchase_history_snapshot"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'refresh', 'archive']
