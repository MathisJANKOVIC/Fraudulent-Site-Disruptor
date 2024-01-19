from faker import Faker
import random

COUNTRIES = [
    "fr_FR",
    "fr_BE",
    "fr_CH",
    "fr_CA",
    "es_ES",
    "hr_HR",
    "it_IT",
    "ru_RU",
    "en_US",
    "en_GB"
]

faker_random = Faker(locale=COUNTRIES[random.randint(0, len(COUNTRIES) - 1)])
fake_fr = Faker(locale="fr_FR")