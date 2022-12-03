class Product:
    """Product class implementation"""

    def __init__(self, name: str, price: float) -> None:
        """Initialize a product instance"""

        self.name = name
        self.price = price

    def __repr__(self):
        """Implement a human readable string representation for Product class"""

        return f'name = {self.name} and price = {self.price}'

    def __eq__(self, other) -> bool:
        """Implement equality comparison for the Product instances. The products are equal in case both objects have the
         same name and price."""

        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price

    def __float__(self) -> float:
        """Implement type-casting for Product. Product cast to float type equals to its price"""

        return self.price

    def __str__(self) -> str:
        """Implement type-casting for Product. Product cast to string type equals to its name"""

        return self.name

    def get_total(self, quantity: float) -> float:
        """Return total price for a specified quantity of goods"""

        return round(self.price * quantity, 2)


class ShoppingCart():
    """ShoppingCart class implementation"""

    def __init__(self) -> None:
        """Initialize a shopping cart instance"""

        self.goods = []
        self.buyed_quantity = []

    def add_product(self, product: Product, quantity: float) -> list:
        """Combine products instances and corresponding purchased quantities"""

        if product in self.goods:
            idx = self.goods.index(product)
            self.buyed_quantity[idx] += quantity
        else:
            self.goods.append(product)
            self.buyed_quantity.append(quantity)

    def __add__(self, other):
        """Implement addition 'carts to carts' behavior for ShoppingCart class"""

        if isinstance(other, Product):
            self.add_product(other, 1)
            return self

        elif isinstance(other, ShoppingCart):
            cart_obj = ShoppingCart()
            for product, quantity in zip(self.goods + other.goods,
                                         self.buyed_quantity + other.buyed_quantity):
                cart_obj.add_product(product, quantity)
            return cart_obj

    def get_total(self) -> float:
        """Return the total price of entire cart"""

        totalprice = 0
        for product, quantity in zip(self.goods, self.buyed_quantity):
            totalprice += product.get_total(quantity)
        return round(totalprice, 2)

    def __float__(self) -> float:
        """Implement type-casting for ShoppingCart.ShoppingCart cast to float type equals to its total price"""

        return totalprice

    def __repr__(self):
        """Implement a human readable string representation for ShoppingCart class """

        return f"Your cart contains goods = {self.goods}, appropriate quantities = {self.buyed_quantity}"