from faker import Faker
from faker.providers import BaseProvider


class PersonNameProvider(BaseProvider):
    def person_name(self):
        return self.generator.last_name_male()


fake = Faker()
fake.add_provider(PersonNameProvider)

fake_person_names = [fake.person_name() for _ in range(10)]
for i in fake_person_names:
    print(i)
