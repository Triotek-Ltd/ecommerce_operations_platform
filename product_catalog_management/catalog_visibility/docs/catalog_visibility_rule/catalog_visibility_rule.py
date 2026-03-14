"""Doc runtime hooks for catalog_visibility_rule."""

class DocRuntime:
    doc_key = "catalog_visibility_rule"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'activate', 'deactivate', 'archive']
