class FailedToLoginException(Exception):
    def __init__(self, details: str):
        self.details = details


class UserAlreadyExists(Exception):
    def __init__(self, details: str):
        self.details = details


class ErrorSavingUser(Exception):
    def __init__(self, details: str):
        self.details = details


class ServerNotResponds(Exception):
    def __init__(self, details: str):
        self.details = details
