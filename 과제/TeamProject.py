from abc import ABC, abstractmethod

# Prototype Pattern
class UserPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class User(UserPrototype):
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def clone(self):
        return User(self.username, self.email)

# Builder Pattern
class UserProfileBuilder:
    def __init__(self):
        self.username = None
        self.email = None

    def set_username(self, username):
        self.username = username
        return self

    def set_email(self, email):
        self.email = email
        return self

    def build(self):
        return User(self.username, self.email)

# Factory Method Pattern
class UserFactory(ABC):
    @abstractmethod
    def create_user(self):
        pass

class RegularUserFactory(UserFactory):
    def create_user(self):
        builder = UserProfileBuilder()
        return builder.set_username("RegularUser").build()

class PremiumUserFactory(UserFactory):
    def create_user(self):
        builder = UserProfileBuilder()
        return builder.set_username("PremiumUser").set_email("premium@example.com").build()

# Example Usage
if __name__ == "__main__":
    regular_user_factory = RegularUserFactory()
    premium_user_factory = PremiumUserFactory()

    regular_user = regular_user_factory.create_user()
    premium_user = premium_user_factory.create_user()

    print("Regular User:", regular_user.username, regular_user.email)
    print("Premium User:", premium_user.username, premium_user.email if premium_user.email else "No email")
