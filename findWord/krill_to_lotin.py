from uzwords import words

words2=["абадийлик",
    "абадия",
    "абадият",
    "абажур",
    "аббат",
    "аббосийлар",
    "аббревиатура",
    "абгорлик",
    "абдол",
    "аберрация",
    "абёт",
    "абжад"]

kirill_to_latin = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
    'е': 'e', 'ё': 'yo', 'ж': 'j', 'з': 'z', 'и': 'i',
    'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
    'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
    'у': 'u', 'ф': 'f', 'х': 'x', 'ц': 'ts', 'ч': 'ch',
    'ш': 'sh', 'ъ': "'", 'ь': '', 'э': 'e', 'ю': 'yu',
    'я': 'ya', 'ў': "o'", 'ғ': "g'", 'қ': 'q', 'ҳ': 'h','-': '-', ' ': ' '   
}

latin_words=[]
make_word=[]

for word in words:
    for letter in word:
        make_word.append(kirill_to_latin[letter])
    latin_words.append("".join(make_word))
    make_word.clear()

print(latin_words)