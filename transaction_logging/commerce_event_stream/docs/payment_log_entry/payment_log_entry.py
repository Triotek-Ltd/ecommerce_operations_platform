"""Doc runtime hooks for payment_log_entry."""

class DocRuntime:
    doc_key = "payment_log_entry"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'normalize', 'archive']
