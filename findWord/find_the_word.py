from krill_to_lotin import latin_words
from random import choice

print(f"Keling siz bilan so'z topish o'yinini o'ynaylik!\n"
      f"Harflarini taxmin qiling")

real_word = list(choice(latin_words))
copy_word= real_word[:]
word = []
guess_error = []
for _ in range(len(real_word)):
    word.append('-')

print("".join(word))

while True:
    guess=input('>> ').lower()

    while guess in real_word:
        i = real_word.index(guess)
        word[i] = guess
        real_word[i]=0
        print("".join(word))
      
    guess_error.append(guess) 
    print("".join(word))
    print(f"Noto'g'ri taxminlaringiz:\n {"".join(guess_error)}") 

    if word == copy_word:
        print(f"{"".join(word)}\n Topdingiz!")
        break


