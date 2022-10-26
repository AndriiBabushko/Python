class Privileges:
    def __init__(self, privileges: list):
        self.privileges = privileges

    def show_privileges(self):
        print('Privileges:')
        for privilege in self.privileges:
            print('* ' + privilege)
