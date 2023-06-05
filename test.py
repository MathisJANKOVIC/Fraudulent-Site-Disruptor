import faker
t = faker.Faker(locale="fr_FR")
for i in range(10):
    a = t.credit_card_number()
    print(a,len(a))