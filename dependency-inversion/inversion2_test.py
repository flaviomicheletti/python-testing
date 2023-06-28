from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    # Abstract interface for a payment gateway
    @abstractmethod
    def process_payment(self, amount):
        pass  # pragma: no cover


class CreditCardGateway(PaymentGateway):
    # Concrete implementation of a credit card payment gateway
    def process_payment(self, amount):
        # Code to process payment using credit card gateway
        return f"Processing credit card payment of ${amount}"


class PayPalGateway(PaymentGateway):
    # Concrete implementation of a PayPal payment gateway
    def process_payment(self, amount):
        # Code to process payment using PayPal gateway
        return f"Processing PayPal payment of ${amount}"


class PaymentProcessor:
    # High-level module that depends on the PaymentGateway interface
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def process_payment(self, amount):
        return self.payment_gateway.process_payment(amount)


def test_payment_processor1():
    # Create an instance of the CreditCardGateway
    gateway = CreditCardGateway()

    # Create an instance of the PaymentProcessor and pass in the CreditCardGateway instance
    payment_processor = PaymentProcessor(gateway)

    # Use the PaymentProcessor to process a payment
    assert payment_processor.process_payment(100) == "Processing credit card payment of $100"


def test_payment_processor2():
    # Create an instance of the PayPalGateway
    gateway = PayPalGateway()

    # Create an instance of the PaymentProcessor and pass in the CreditCardGateway instance
    payment_processor = PaymentProcessor(gateway)

    # Use the PaymentProcessor to process a payment
    assert payment_processor.process_payment(100) == "Processing PayPal payment of $100"
