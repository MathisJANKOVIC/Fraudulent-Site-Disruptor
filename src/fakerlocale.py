from faker import Faker
import random as rand

LOCALES = ["fr_FR", "fr_BE", "fr_CH", "fr_CA", "es_ES", "hr_HR", "it_IT", "ru_RU", "en_US", "en_GB"]

random = Faker(locale=rand.choice(LOCALES))
fr = Faker(locale="fr_FR")