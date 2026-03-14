"""Doc runtime hooks for catalog_product."""

class DocRuntime:
    doc_key = "catalog_product"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'publish', 'unpublish', 'archive']
