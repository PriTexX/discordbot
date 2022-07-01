class FailedToLoginException(Exception):
    def __init__(self, details: str):
        self.details = details


class WrongCredentials(Exception):
    def __init__(self, details: str):
        self.details = details


class ErrorSavingUser(Exception):
    def __init__(self, details: str):
        self.details = details