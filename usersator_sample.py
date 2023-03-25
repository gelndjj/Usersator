import csv, pandas as pd, random as r
from faker import Faker

fake = Faker()
num_users = 1000

fieldnames = ('first_name', 'last_name', 'email', 'age', 'phone_number', 'city', 'state', 'zip_code', 'address','company')

with open('users_info.csv','w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(num_users):
        first_name = fake.first_name()
        last_name = fake.last_name()
        domain = fake.free_email_domain()
        email = f'{first_name}.{last_name}@{domain}'
        age = r.randint(19,62)
        phone_number = f'({r.randint(100,1000)}) {r.randint(100,1000)}-{r.randint(1000,10000)}'
        city = fake.city()
        state = fake.state()
        zip_code = fake.zipcode()
        address = fake.address()
        company = fake.company()
        writer.writerow({
            'first_name':first_name,
            'last_name':last_name,
            'email':email.lower(),
            'age': age,
            'phone_number':phone_number,
            'city':city,
            'state':state,
            'zip_code':zip_code,
            'address':address,
            'company':company
        })