class User:
    def __init__(self, first_name: str, last_name: str, email: str, nickname: str, mailing_consent: bool, login_attempts: int = 0):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.full_name: str = last_name + ' ' + first_name
        self.email: str = email
        self.nickname: str = nickname
        self.mailing_consent: bool = mailing_consent
        self.login_attempts: int = login_attempts

    def describe_user(self):
        print(f'Full user name: {self.full_name}')

    def greeting_user(self):
        print(f'Our greetings, {self.full_name}!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
