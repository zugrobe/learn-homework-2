# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# Вывести количество букв "а" в слове
x = word.count('а')
print(x)

# Вывести количество гласных букв в слове
count = 0
vowel_letters = 'уеыаоэяиюё'
for letter in word.lower():
    if letter in vowel_letters:
        count += 1 
print('количество гласных:', count)
print(" ")

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
split_text = sentence.split(" ")
print('Количество слов:', len(split_text))

# Вывести первую букву каждого слова на отдельной строке
for i in split_text:
    print(i[0:1])

# Вывести усреднённую длину слова.
letters_sum = len(sentence) - sentence.count(" ")
letters_avg = letters_sum / len(split_text)
print('Средняя длина слова:', (letters_avg))