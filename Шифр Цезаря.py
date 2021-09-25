alfavit = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВ ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789123'
shifr = 1
while True:
    message = str(input("Повідомлення для дешифровки: ")).upper()
    res = ''
    lang = 'UA'
    if lang == 'UA':
            for i in message:
                mr = alfavit.find(i)
                new_mr = mr + shifr
                if i in alfavit:
                    res += alfavit[new_mr]
                else:
                    res += i
    print(res)
