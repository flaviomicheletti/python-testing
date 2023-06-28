"""
I noticed that you used "from abc import ABC, abstractmethod" in both 
examples. 

No, implementing dependency injection does not necessarily require the use of 
abstractmethod or abstract base classes (ABC). abstractmethod and abstract 
base classes are tools provided by the abc module in Python that can be 
useful when defining interfaces or contracts for dependencies in a more 
formalized manner. 

Dependency injection is a broader concept that focuses on the decoupling of 
dependencies and their injection into classes or objects from external 
sources. It can be implemented using various techniques, such as constructor 
injection, setter injection, or method injection. 

In Python, you can implement dependency injection without explicitly using 
abstractmethod or abstract base classes. You can use plain classes or 
interfaces to define contracts or interfaces for dependencies and apply 
dependency injection principles accordingly. 

Here's an example without using abstractmethod:
"""

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
