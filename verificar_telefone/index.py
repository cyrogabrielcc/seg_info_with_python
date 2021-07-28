import phonenumbers

from phonenumbers import geocoder
from phonenumbers import phonenumber

phone = input('digite o telefone: +552140028922: ')

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))














