from mimesis import Person
from mimesis import Address
from mimesis.enums import Gender
from mimesis import Datetime
import pandas as pd
import random
import time

person = Person('en')

person = Person()
address = Address()
datetime = Datetime()


def create_rows_mimesis(num=1):
    output = [{"name": person.full_name(gender=Gender.FEMALE),
               "address": address.address(),
               "name": person.name(),
               "email": person.email(),
               # "bs":person.bs(),
               "city": address.city(),
               "state": address.state(),
               "date_time": datetime.datetime(),
               # "paragraph":person.paragraph(),
               # "Conrad":person.catch_phrase(),
               "randomdata": random.randint(1000, 2000)} for x in range(num)]
    return output


start = time.time()
# the code you want to test stays here
df_mimesis = pd.DataFrame(create_rows_mimesis(5000))

# df.to_csv('../data/mimesis-file2.csv')

# end of the code you want to test
end = time.time()

print(end - start)
