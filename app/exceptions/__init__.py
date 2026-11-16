from app.core.exceptions import BadRequest, ConflictError, Unauthorized


class UserAlreadyExistsError(ConflictError):
    def __init__(self, field: str, value: str):
        self.field = field
        self.value = value
        super().__init__(f"User with {field} '{value}' already exists.")

class PasswordMismatchError(BadRequest):
    def __init__(self, *args, **kwargs):
        super().__init__("Password Mismatch")

class NewPasswordSameAsOldPassword(BadRequest):
    def __init__(self, *args, **kwargs):
        super().__init__("New Password shouldn't be same as Old Password")

class AuthenticationError(Unauthorized):
    def __init__(self, username: str):
        super().__init__("Username and Password mismatch for user {username}")