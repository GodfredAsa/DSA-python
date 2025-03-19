from Order import Order
from PaymentProcessor import PaymentProcessor
from OrderRepository import OrderRepository
order = Order("12345", 200, 2, "New town")

print(order)

payment_process = PaymentProcessor()
payment_process.process_payment(order)

order_repository = OrderRepository()
order_repository.save_order(order)