"""Doc runtime hooks for account_activity_log."""

class DocRuntime:
    doc_key = "account_activity_log"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'archive']
