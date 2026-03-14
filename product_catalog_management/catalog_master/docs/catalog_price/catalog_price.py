"""Doc runtime hooks for catalog_price."""

class DocRuntime:
    doc_key = "catalog_price"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'activate', 'supersede', 'archive']
