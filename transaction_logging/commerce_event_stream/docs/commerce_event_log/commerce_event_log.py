"""Doc runtime hooks for commerce_event_log."""

class DocRuntime:
    doc_key = "commerce_event_log"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'normalize', 'archive']
