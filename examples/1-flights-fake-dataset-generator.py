from mimesis import Person
from mimesis import Address
from mimesis import Datetime
import pandas as pd
import random
import time

person = Person('en')

person = Person()
address = Address()
datetime = Datetime()


def create_rows_mimesis(num=1):
    output = [{"name": person.full_name(),
               "GEO": address.country(),
               "PARTNER": address.country(),
               "TIME": datetime.datetime(),
               "YEAR": datetime.year(),
               "MONTH": datetime.month(),
               "Value": random.randint(1, 10000)} for x in range(num)]
    return output


start = time.time()
# the code you want to test stays here
df_mimesis = pd.DataFrame(create_rows_mimesis(500))

# df.to_csv('../data/mimesis-file2.csv')

# end of the code you want to test
end = time.time()

print(end - start)

print(df_mimesis)
