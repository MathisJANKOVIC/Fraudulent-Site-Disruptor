from faker import Faker
import random

COUNTRIES = ["fr_FR", "fr_BE", "fr_CH", "fr_CA", "es_ES", "hr_HR", "it_IT", "ru_RU", "en_US", "en_GB"]

random_country = Faker(locale=random.choice(COUNTRIES))
fr = Faker(locale="fr_FR")