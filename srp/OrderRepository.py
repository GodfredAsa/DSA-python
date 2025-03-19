from Order import Order
class OrderRepository:

    def save_order(self, order: "Order"):
        print(f"Order with ID {order.orderId} saved successfully")