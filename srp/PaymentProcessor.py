from Order import Order
class PaymentProcessor:
    def process_payment(self, order: 'Order'):
        print(f"Processing order with ID {order.orderId} for an amount of {order.amount} payment...")