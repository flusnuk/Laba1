#  закоментований код - це код для шифрування слова на англійській мові

import random
# alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_UA = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХ  ЦЧШЩЬЮЯАБВ'
shifr = random.randint(1,10)
message = input("Повідомлення для дешифровки: ").upper()
res = ''
lang = 'UA'
# lang = input('Виберіть мову UA/EU: ')
if lang == 'UA':
    for i in message:
        mr = alfavit_UA.find(i)
        new_mr = mr + shifr
        if i in alfavit_UA:
            res += alfavit_UA[new_mr]
        else:
            res += i
#else:
#    for i in message:
 #       mr = alfavit_EU.find(i)
  #      [new_mr = mr + shifr
   #     if i in alfavit_EU:
   #         res += alfavit_EU[[new_mr]
    #    else:
   #         res += i
print (res)
print(shifr)