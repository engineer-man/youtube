with open('contacts.vcf') as f:
    contacts = f.read().strip().split('\n')

names = []

name = ''
email = ''
for contact in contacts:
    if 'EMAIL' in contact:
        email = contact.split(':')[-1]
    if 'FN' in contact:
        name = contact.split(':')[-1]
    if contact == 'END:VCARD':
        names.append('{},{}'.format(name, email))

for name in names:
    print(name)
