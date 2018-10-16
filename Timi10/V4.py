def get_emails():
    k = input("Email address: ")
    listinn =[]
    while '@' in k:
        listinn.append(k)
        k = input("Email address: ")
    return listinn

def get_names_and_domains(email):
    b_list = []
    for x in email:
        a = tuple(x.split('@'))
        b_list.append(a)
    return b_list


# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)