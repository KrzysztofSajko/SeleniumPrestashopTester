from __future__ import annotations

import string
from random import choice
from faker.proxy import Faker
from unidecode import unidecode

from utility.myTypes import Gender


class User:
    def __init__(self, gender: Gender, name: str, surname: str, email: str, password: str, birthday: str, address: str, postcode: str, city: str):
        self.gender: Gender = gender
        self.name: str = name
        self.surname: str = surname
        self.email: str = email
        self.password: str = password
        self.birthday: str = birthday
        self.address: str = address
        self.postcode: str = postcode
        self.city: str = city

    @classmethod
    def create_normal_user(cls) -> User:
        def random_password(length: int):
            letters: str = string.ascii_letters + string.digits + string.punctuation
            return ''.join(choice(letters) for _ in range(length))

        fake = Faker('pl_PL')
        gender: Gender = choice(list(Gender))
        if gender == Gender.FEMALE:
            name: str = fake.first_name_female()
            surname: str = fake.last_name_female()
        else:
            name: str = fake.first_name_male()
            surname: str = fake.last_name_male()
        return User(gender,
                    name,
                    surname,
                    f"{unidecode(name.lower())}.{unidecode(surname.lower())}@{fake.free_email_domain()}",
                    random_password(12),
                    str(fake.date_of_birth(minimum_age=16, maximum_age=90)),
                    fake.street_address(),
                    fake.postcode(),
                    fake.city())
