""" Lab 10. Python. Andrii Babushko. Repository: https://github.com/AndriiBabushko/Python """
import sys
import unittest
from shop import Shop
from discount import Discount
from user import User
from admin import Admin

sys.path.insert(0, r'modules')


# task 1
class ShopDiscountCheck(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('Set up class')
        print('---------------')

    @classmethod
    def tearDownClass(cls) -> None:
        print('---------------')
        print('Tear down class')

    def setUp(self) -> None:
        print(f'Set up for ["{self.shortDescription()}"]')

    def tearDown(self) -> None:
        print(f'Tear down for ["{self.shortDescription()}"]\n')

    @staticmethod
    def create_shop() -> Shop:
        return Shop('All  store', 'store')

    @staticmethod
    def create_discount() -> Discount:
        return Discount('Store', 'stuff store', Car_Toy='10%', Doll_toy='20%', Mobile_phone='15%')

    def test_shop_describe_shop(self):
        shop: Shop = self.create_shop()
        print(f'Shop describe shop id: {self.id()}')
        self.assertMultiLineEqual(shop.describe_shop(), f'Shop name: {shop.name}; Shop type: {shop.type};')

    def test_shop_open_shop(self):
        shop: Shop = self.create_shop()
        print(f'Shop open shop id: {self.id()}')
        self.assertMultiLineEqual(shop.open_shop(), 'Online shop is opened!')

    def test_shop_set_number_of_units(self):
        shop: Shop = self.create_shop()
        print(f'Shop set number of units id: {self.id()}')
        self.assertEqual(shop.set_number_of_units(5), 5)
        self.assertEqual(shop.set_number_of_units(0), 0)
        self.assertEqual(shop.set_number_of_units(-5), 0)

    def test_shop_increment_number_of_units(self):
        shop: Shop = self.create_shop()
        print(f'Shop increment number of units id: {self.id()}')
        self.assertEqual(shop.increment_number_of_units(5), 5)
        self.assertEqual(shop.increment_number_of_units(-10), 5)
        self.assertEqual(shop.increment_number_of_units(0), 5)

    def test_discount_get_discounts_products(self):
        discount: Discount = self.create_discount()
        print(f'Shop get discounts products id: {self.id()}')
        self.assertIsNone(discount.get_discounts_products())


# task 2
class UserAdminPrivilegesCheck(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('Set up class')
        print('---------------')

    @classmethod
    def tearDownClass(cls) -> None:
        print('---------------')
        print('Tear down class')

    def setUp(self) -> None:
        print(f'Set up for ["{self.shortDescription()}"]')

    def tearDown(self) -> None:
        print(f'Tear down for ["{self.shortDescription()}"]\n')

    @staticmethod
    def create_user() -> User:
        return User('Andrii', 'Babushko', 'andriibabushko@gmail.com', 'AndriiRaccoon', True)

    @staticmethod
    def create_admin() -> Admin:
        return Admin('Andrii', 'Babushko', 'andriibabushko@gmail.com', 'AndriiRaccoon', True,
                     ['Allowed to block users', 'Allowed to delete messages', 'Allowed to send voices', 'Allowed to delete users'])

    def test_user_describe_user(self):
        user: User = self.create_user()
        print(f'User describe user id: {self.id()}')
        self.assertMultiLineEqual(user.describe_user(), f'Full user name: {user.full_name}')

    def test_user_greeting_user(self):
        user: User = self.create_user()
        print(f'User greeting user id: {self.id()}')
        self.assertMultiLineEqual(user.greeting_user(), f'Our greetings, {user.full_name}!')

    def test_user_increment_login_attempts(self):
        user: User = self.create_user()
        print(f'User increment login attempts id: {self.id()}')
        self.assertEqual(user.increment_login_attempts(), 1)

    def test_user_reset_login_attempts(self):
        user: User = self.create_user()
        print(f'User reset login attempt id: {self.id()}')
        self.assertEqual(user.reset_login_attempts(), 0)

    def test_admin_show_privileges(self):
        admin: Admin = self.create_admin()
        print(f'Admin show privileges id: {self.id()}')
        self.assertIsNone(admin.show_privileges())


if __name__ == '__main__':
    unittest.main()
