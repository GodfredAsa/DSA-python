from Order import Order
from PaymentProcessor import PaymentProcessor
order  = Order("12345", 200, 2, "New town")

print(order)


payment_process = PaymentProcessor()
payment_process.process_payment(order)