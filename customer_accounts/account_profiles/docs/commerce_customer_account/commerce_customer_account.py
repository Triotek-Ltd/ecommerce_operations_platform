"""Doc runtime hooks for commerce_customer_account."""

class DocRuntime:
    doc_key = "commerce_customer_account"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'suspend', 'archive']
