from unittest.mock import Mock

class Logger:
    def log(self, message):
        print(f"Logging: {message}")


class UserService:
    def __init__(self):
        self._logger = None

    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, logger):
        self._logger = logger

    def register_user(self, username):
        self.logger.log(f"User '{username}' registered.")


def test_register_user():
    # Create a mock logger
    logger = Mock()

    # Create an instance of the UserService
    user_service = UserService()

    # Set the mock logger as the logger for the UserService
    user_service.logger = logger

    # Call the register_user method
    user_service.register_user("John")

    # Add your assertions here, if applicable
    logger.log.assert_called_once_with("User 'John' registered.")


def test_log():
    # Create an instance of the Logger
    logger = Logger()

    # Call the log method
    logger.log("Test message")

    # No assertions needed since the log method simply prints the message


"""
# Create instances of Logger and UserService
logger = Logger()
user_service = UserService()

# Inject the Logger instance into the UserService
user_service.logger = logger

# Use the UserService to register a new user
user_service.register_user("John")
"""
