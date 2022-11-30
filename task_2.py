class Product:
    """Product class implementation"""

    def __init__(self, name: str, price: float) -> None:
        """Initialize a product instance"""

        self.name = name
        self.price = price

    def __str__(self):
        """Implement a human readable string representation for Product class"""

        return f"{self.name}, {self.price})"

    def __eq__(self, other) -> bool:
        """Implement equality comparison for the Product instances. The products are equal in case both objects have the
         same name and price."""

        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price

    def __float__(self) -> float:
        """Implement type-casting for Product. Product cast to float type equals to its price"""

        return float(self.price)

    def __str__(self) -> str:
        """Implement type-casting for Product. Product cast to string type equals to its name"""

        return str(self.name)

    def get_total(self, quantity: float) -> float:
        """Return total price for a specified quantity of goods"""

        return round(self.price * quantity, 2)


class ShoppingCart():
    """ShoppingCart class implementation"""

    def __init__(self) -> None:
        """Initialize a shopping cart instance"""

        self.goods = []
        self.buyed_quantity = []
        self.cart = [self.goods, self.buyed_quantity]

    def add_product(self, product: Product, quantity: float) -> list:
        """Combine products instances and corresponding purchased quantities"""

        if product in self.goods:
            idx = self.goods.index(product)
            self.buyed_quantity[idx] += quantity
        else:
            self.goods.append(product)
            self.buyed_quantity.append(quantity)

    def add_cart(self, cart_1: object, *args: tuple) -> list:
        """Implement addition 'carts to carts' behavior for ShoppingCart class"""

        totalcart = cart_1.cart
        products = totalcart[0]
        quantities = totalcart[1]
        for obj in args:
            for product, quantity in zip(obj.goods, obj.buyed_quantity):
                if product in products:
                    idx = products.index(product)
                    quantities[idx] += quantity
                else:
                    products.append(product)
                    quantities.append(quantity)
        return totalcart

    def get_total(self) -> float:
        """Return the total price of entire cart"""

        totalprice = 0
        for product, quantity in zip(self.goods, self.buyed_quantity):
            totalprice += product.get_total(quantity)
        return round(totalprice, 2)

    def __float__(self) -> float:
        """Implement type-casting for ShoppingCart. ShoppingCart cast to float type equals to its total price"""

        return float(totalprice)

    def __str__(self):
        """Implement a human readable string representation for ShoppingCart class"""

        return 'goods: %s, quantity: %s, cart: %s' %(self.goods, self.buyed_quantity, self.cart)