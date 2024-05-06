set_1 = { "A", "E", "I", "O", "U", "L", "N", "S", "T", "R", "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т",}
set_2 = {'D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'}
set_3 = {'B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'}
set_4 = {'F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'}
set_5 = {'K', 'Ж', 'З', 'Х', 'Ц', 'Ч'}
set_8 = {'J', 'X', 'Ш', 'Э', 'Ю'}
set_10 = {'Q', 'Z', 'Ф', 'Щ', 'Ъ'}

word = input('Please, type the world: \n').upper()
# print(word)
price_word = 0
for item in word:
    if item in set_1:
        price_word += 1
    if item in set_2:
        price_word += 2
    if item in set_3:
        price_word += 3
    if item in set_4:
        price_word += 4
    if item in set_5:
        price_word += 5
    if item in set_8:
        price_word += 8
    if item in set_10:
        price_word += 10

print(price_word)
    
