"""Doc runtime hooks for refund_case."""

class DocRuntime:
    doc_key = "refund_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'reject', 'refund', 'close', 'archive']
