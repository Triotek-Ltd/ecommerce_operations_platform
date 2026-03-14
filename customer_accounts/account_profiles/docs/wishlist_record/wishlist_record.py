"""Doc runtime hooks for wishlist_record."""

class DocRuntime:
    doc_key = "wishlist_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'convert', 'remove', 'archive']
