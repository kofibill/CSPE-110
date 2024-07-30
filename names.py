import email


first_name=input('Please enter your first name:')
last_name=input('Please enter your last name:')
email_address=input('Please enter email address:')
phone_number=input('Please enter your phone number:')
job_title=input('Please enter your job title:')
ID_number=input('Please enter your id number:')
print('This card belongs to:')
print(f'{last_name.upper()} {first_name}')
print(f'{job_title.capitalize()}')
print(f'{email_address.lower()}')
print(f'{phone_number}')
print(f'{ID_number}')