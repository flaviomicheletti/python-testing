""" Easier than the last one """

class Logger:
    def log(self, message):
        return f"Logging: {message}"


class UserService:
    def __init__(self, logger):
        self.logger = logger

    def register_user(self, username):
        return self.logger.log(f"User '{username}' registered.")


def test_user_service():
    # Create an instance of the Logger
    logger = Logger()

    # Create an instance of the UserService and pass in the Logger instance
    user_service = UserService(logger)

    # Use the UserService to register a new user
    assert user_service.register_user("John") == "Logging: User 'John' registered."
