import random

from faker import Faker

_LOCALES = ("fr_FR", "fr_BE", "fr_CH", "fr_CA", "es_ES", "hr_HR", "it_IT", "ru_RU", "en_US", "en_GB")

fr_locale = Faker(locale="fr_FR")

def get_random_locale() -> Faker:
    locale = random.choice(_LOCALES)
    return Faker(locale)