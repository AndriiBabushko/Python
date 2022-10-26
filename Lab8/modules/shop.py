class Shop:
    def __init__(self, shop_name: str, shop_type: str, shop_number_of_units: int = 0):
        self.name: str = shop_name
        self.type: str = shop_type
        self.number_of_units: int = shop_number_of_units

    def describe_shop(self):
        print(f'Shop name: {self.name}; Shop type: {self.type};')

    @staticmethod
    def open_shop():
        print('Online shop is opened!')

    def set_number_of_units(self, number_of_units: int):
        self.number_of_units: int = number_of_units

    def increment_number_of_units(self, increment: int):
        if increment > 0:
            self.number_of_units += increment
