class Privileges:
    def __init__(self, privileges: list) -> None:
        self.privileges = privileges

    def show_privileges(self) -> None:
        print('Privileges:')
        for privilege in self.privileges:
            print('* ' + privilege)
