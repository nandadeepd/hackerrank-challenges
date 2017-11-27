# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
emailRegex = r'(.*)\@(.*)'
phoneRegex = r'(\+\d+\s)?\(?(\d+)\)?[\s.-]?(\d+)[\s.-]?(\d+)'
emails, phones = list()
def starGen(strForWhich):
    return "*" * len(strForWhich)

def maskPhone(phone):
    toReturnPhone = ''
    phone_search = re.search(phoneRegex, phone)
    if phone_search:
        international_code = phone_search.group(1).strip()
        area_code = phone_search.group(2).strip()
        numberPartOne = phone_search.group(3).strip()
        numberPartTwo = phone_search.group(4).strip()
        toReturnPhone = '+' + starGen(str(international_code)) + '-' + starGen(str(area_code)) + '-' + starGen(numberPartOne) + '-' + numberPartTwo
        # print toReturnPhone
    return toReturnPhone
    

def maskEmail(emailid):
    toReturnEmail = ''
    email_search = re.search(emailRegex, emailid, re.IGNORECASE)
    if email_search:
        e_name = email_search.group(1)
        e_name_len = len(e_name)
        stars = "*" * (e_name_len - 2)
        stars = ''.join(stars)
        e_domain = email_search.group(2)
        toReturnEmail = e_name[0] + stars + e_name[e_name_len - 1] + '@' + e_domain
        # print toReturnEmail
    return toReturnEmail

lines = str(input())
for line in lines:
    if 'E:' in line:
        temp = line.index('E:')
        emails.append(line[temp+1:].split(':')[1].strip())
    if 'P:' in line:
        temp = line.index("P:")
        phones.append(line[temp+1:].split(':')[1].strip())   
