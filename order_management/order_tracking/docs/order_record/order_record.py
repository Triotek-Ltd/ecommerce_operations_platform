"""Doc runtime hooks for order_record."""

class DocRuntime:
    doc_key = "order_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'confirm', 'update_status', 'cancel', 'close', 'archive']
