class Order:
    def __init__(self, orderId: str, amount: int, qty: int, address: str):
        self.orderId = orderId
        self.amount = amount
        self.qty = qty
        self.address = address

    def __str__(self) -> str:
     return f"<Order owner: {self.orderId}, address: {self.address}, amount: GHS {self.amount}, qty: {self.qty}>"
    
