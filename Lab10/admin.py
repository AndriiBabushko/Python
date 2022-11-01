from privileges import Privileges
from user import User


class Admin(User):
    def __init__(self, first_name: str, last_name: str, email: str, nickname: str, mailing_consent: bool, admin_privileges: list) -> None:
        super().__init__(first_name, last_name, email, nickname, mailing_consent)
        self.admin_privileges: Privileges = Privileges(admin_privileges)

    def show_privileges(self) -> None:
        print(f'{self.full_name} admin\'s privileges:')
        for privilege in self.admin_privileges.privileges:
            print('* ' + privilege)
