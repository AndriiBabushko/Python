class User:
    def __init__(self, first_name: str, last_name: str, email: str, nickname: str, mailing_consent: bool, login_attempts: int = 0) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.full_name: str = last_name + ' ' + first_name
        self.email: str = email
        self.nickname: str = nickname
        self.mailing_consent: bool = mailing_consent
        self.login_attempts: int = login_attempts

    def describe_user(self) -> str:
        return f'Full user name: {self.full_name}'

    def greeting_user(self) -> str:
        return f'Our greetings, {self.full_name}!'

    def increment_login_attempts(self) -> int:
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self) -> int:
        self.login_attempts = 0
        return self.login_attempts
