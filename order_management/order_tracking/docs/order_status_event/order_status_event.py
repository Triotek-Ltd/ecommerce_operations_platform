"""Doc runtime hooks for order_status_event."""

class DocRuntime:
    doc_key = "order_status_event"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'normalize', 'archive']
