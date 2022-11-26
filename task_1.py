class Product:
    """Product class implementation"""

    def __init__(self, name: str, price: float) -> None:
        """Initialize a product instance"""

        self.name = name
        self.price = price

    def get_totalprice(self, quantity: float) -> float:
        """Return total price for a specified quantity of goods"""

        return round(self.price * quantity, 2)


class ShoppingCart():
    """ShoppingCart class implementation"""

    def __init__(self) -> None:
        """Initialize a shopping cart instance"""

        self.goods = []
        self.buyed_quantity = []

    def add_cartitem(self, product: Product, quantity: float) -> list:
        """Combine products instances and corresponding purchased quantities"""

        if product in self.goods:
            idx = self.goods.index(product)
            self.buyed_quantity[idx] += quantity
        else:
            self.goods.append(product)
            self.buyed_quantity.append(quantity)

    def get_cartprice(self) -> float:
        """Return the total price of entire cart"""

        priceOfCart = 0
        for product, quantity in zip(self.goods, self.buyed_quantity):
            priceOfCart += product.get_totalprice(quantity)
        return round(priceOfCart, 2)