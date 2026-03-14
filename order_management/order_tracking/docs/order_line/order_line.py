"""Doc runtime hooks for order_line."""

class DocRuntime:
    doc_key = "order_line"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'update_status', 'archive']
