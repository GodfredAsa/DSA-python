class OrderProcessor:
    def __init__(self, payment_processor: 'PaymentProcessor', shipping_processor: 'ShippingProcessor'):
        self.payment_processor = payment_processor
        self.shipping_processor = shipping_processor

    def process_order(self, amount):
        self.payment_processor.process_payment(amount)
        self.shipping_processor.ship_order(order)

class PaymentProcessor:
    def process_payment(self, payment: int):
        print(f"Processing {payment} payment...")

class ShippingProcessor:
    def ship_order(self, address: str):
        print(f"Shipping to: {address}")

class Order:
    def __init__(self, name: str, address: str, amount: int) -> None:
        self.name = name
        self.address = address
        self.amount = amount
    def __str__(self) -> str:
        return f"<Order owner: {self.name}, address: {self.address}, amount: GHS {self.amount}>"

# STEP 1 MAKE ORDER 
order = Order("Stephens Mensah", "14th Street, Miami", 1000)
print(order)

# STEP 2 MAKE PAYMENT 
payment_processor = PaymentProcessor()
payment_processor.process_payment(order.amount)

# STEP 3 SHIPPING 
shipping_processor = ShippingProcessor()
shipping_processor.ship_order(address=order.address)

# ORDER PROCESSING 
order_processor = OrderProcessor(payment_processor, shipping_processor)