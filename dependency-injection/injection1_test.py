from unittest.mock import Mock


class EmailService:
    def send_email(self, recipient, message):
        # Code to send email
        pass


class UserService:
    def __init__(self, email_service):
        self.email_service = email_service

    def register_user(self, username, email):
        # Code to register user
        self.email_service.send_email(email, "Welcome to our platform!")


def test_register_user_sends_email():
    # Create a mock email service
    email_service = Mock()

    # Create an instance of the UserService with the mock email service
    user_service = UserService(email_service)

    # Call the register_user method
    user_service.register_user("John", "john@example.com")

    # Assert that the email service's send_email method was called with the expected arguments
    email_service.send_email.assert_called_once_with("john@example.com", "Welcome to our platform!")

def test_send_email():
    # Create an instance of the EmailService
    email_service = EmailService()

    # Call the send_email method
    email_service.send_email("recipient@example.com", "Hello, world!")


"""
#Example of use:

# Create an instance of the EmailService
email_service = EmailService()

# Create an instance of the UserService and pass in the EmailService instance
user_service = UserService(email_service)

# Use the UserService to register a new user
user_service.register_user("John", "john@example.com")
"""