"""Doc runtime hooks for sales_activity_record."""

class DocRuntime:
    doc_key = "sales_activity_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'refresh', 'archive']
