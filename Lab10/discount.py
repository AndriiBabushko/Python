from shop import Shop


class Discount(Shop):
    def __init__(self, shop_name: str, shop_type: str, **kwargs) -> None:
        super().__init__(shop_name, shop_type)
        self.discount_products: dict = kwargs

    def get_discounts_products(self) -> None:
        discount_keys: list = list(self.discount_products.keys())
        discount_values: list = list(self.discount_products.values())

        print(f'Current discounts:')
        for iterator in range(0, len(self.discount_products)):
            print(f'{discount_keys[iterator]}: {discount_values[iterator]}')
