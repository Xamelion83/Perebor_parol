import datetime
import random
print(datetime.datetime.today())

Chis = '1234567890'
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
abc = 'abcdefghijklmnopqrstuvwxyz'
symb = '!@#$%^&*()-+'
passw = [Chis,ABC,abc,symb]
password = ''
password+=random.choice(Chis)
password+=random.choice(ABC)
password+=random.choice(abc)
password+=random.choice(symb)
while len(password) < 12:
    password += random.choice(passw[random.randint(0,2)])
print(password)


