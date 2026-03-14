"""Doc runtime hooks for payment_attempt."""

class DocRuntime:
    doc_key = "payment_attempt"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'authorize', 'confirm', 'fail', 'cancel', 'archive']
