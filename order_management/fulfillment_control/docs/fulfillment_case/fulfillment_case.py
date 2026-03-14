"""Doc runtime hooks for fulfillment_case."""

class DocRuntime:
    doc_key = "fulfillment_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'review', 'resolve', 'escalate', 'close', 'archive']
