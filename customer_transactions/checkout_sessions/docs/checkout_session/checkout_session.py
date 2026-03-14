"""Doc runtime hooks for checkout_session."""

class DocRuntime:
    doc_key = "checkout_session"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'start', 'complete', 'abandon', 'fail', 'archive']
