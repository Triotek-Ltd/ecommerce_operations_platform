"""Doc runtime hooks for adjustment_record."""

class DocRuntime:
    doc_key = "adjustment_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'apply', 'archive']
