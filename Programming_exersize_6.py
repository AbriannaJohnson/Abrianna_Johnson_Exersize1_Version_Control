# Abrianna Johnson
# 10/12/25

import re

def validate_phone(phone_number):
    pattern = r'\d\d\d[ -]\d\d\d[ -]\d\d\d\d'
    return re.fullmatch(pattern, phone_number)

def validate_ssn(ssn):
    pattern = r'\d\d\d[ -]\d\d[ -]\d\d\d'
    return re.fullmatch(pattern, ssn)

def validate_zip(zip_code):
    pattern = r'\d\d\d\d\d'
    return re.fullmatch(pattern, zip_code)

def main():
    phone_input = input('Enter your phone number: ')
    ssn_input = input('Enter your social security number: ')
    zip_input = input('Enter your zip code: ')

    if validate_phone(phone_input):
        print(f'{phone_input} is a valid phone number')
    else:
        print(f'{phone_input} is an invalid phone number')

    if validate_ssn(ssn_input):
        print(f'{ssn_input} is a valid social security number')
    else:
        print(f'{ssn_input} is an invalid social security number')

    if validate_zip(zip_input):
        print(f'{zip_input} is a valid zip code')
    else:
        print(f'{zip_input} is an invalid zip code')


if __name__=="__main__":
    main()
