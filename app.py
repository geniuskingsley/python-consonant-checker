VOWEL = ('a', 'e', 'i', 'o', 'u')

word = input('Type any word : ')
for letter in word :
  if letter.lower() not in VOWEL :
    print(letter, end ="")