import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+919548189368")
phone_number2 = phonenumbers.parse("+48504540176")
phone_number3 = phonenumbers.parse("+916398280858")

print("\nphone number location\n")
print(geocoder.description_for_number(phone_number1,"en"));
print(geocoder.description_for_number(phone_number2,"en"));
print(geocoder.description_for_number(phone_number3,"en"));