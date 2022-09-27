from faker import Faker
import pandas as pd
import random
import time

fake = Faker()


def create_rows_faker(num=1):
    output = [{"name": fake.name(),
               "address": fake.address(),
               "name": fake.name(),
               "email": fake.email(),
               # "bs":fake.bs(),
               "city": fake.city(),
               "state": fake.state(),
               "date_time": fake.date_time(),
               # "paragraph":fake.paragraph(),
               # "Conrad":fake.catch_phrase(),
               "randomdata": random.randint(1000, 2000)} for x in range(num)]
    return output


start = time.time()
# the code you want to test stays here

df = pd.DataFrame(create_rows_faker(5000))

# df.to_csv('../data/faker-file2.csv')

# end of the code you want to test
end = time.time()

print(end - start)
