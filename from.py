import re

class FormValidator:
    def __init__(self, data):
        self.data = data
        self.errors = {}

    def is_valid(self):
        self.errors.clear()
        self.validate_name()
        self.validate_email()
        self.validate_password()
        return len(self.errors) == 0

    def validate_name(self):
        name = self.data.get("name", "").strip()
        if not name:
            self.errors["name"] = "Name is required."
        elif not name.replace(" ", "").isalpha():
            self.errors["name"] = "Name must contain only letters."

    def validate_email(self):
        email = self.data.get("email", "").strip()
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not email:
            self.errors["email"] = "Email is required."
        elif not re.match(pattern, email):
            self.errors["email"] = "Invalid email format."

    def validate_password(self):
        password = self.data.get("password", "")
        if not password:
            self.errors["password"] = "Password is required."
        elif len(password) < 6:
            self.errors["password"] = "Password must be at least 6 characters long."

    def get_errors(self):
        return self.errors

# Example usage
form_data = {
    "name": "Alice",
    "email": "alice@example.com",
    "password": "secret123"
}

validator = FormValidator(form_data)

if validator.is_valid():
    print("✅ Form is valid!")
else:
    print("❌ Form has errors:")
    for field, error in validator.get_errors().items():
        print(f" - {field}: {error}")
