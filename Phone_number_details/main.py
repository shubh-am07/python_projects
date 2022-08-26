import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter your number with +: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number()