from faker import Faker

f = Faker('ru_RU')
# city_address = 'Санкт-Петербург, Есенина, д1'
# entrance = 7
# floor = 3
# apartment = 456
#
# full_name = f.name(),
# email = f.email(),
# phone_number = f.phone_number()

ORDER_CONTACT_INFO = {
    'city_address': 'Санкт-Петербург, Есенина, д1',
    'entrance': 7,
    'floor': 3,
    'apartment': 456,
    'full_name': f.name(),
    'email': f.email(),
    'phone_number': f.phone_number(),
}