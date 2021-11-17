# it is a fun hangman game that users can predict each letter every round.

kelime = 'Cristiano'
liste = []
for harf in kelime:
    liste.append('-')
hangKelime = len(kelime) * '-'

i = 0
can = 3
print('Welcome to the hangman game'.center(100,'*'))
print(f'the letter you have to find has {len(kelime)} letter: {hangKelime} ')
while i < len(liste):
    if can > 0:
        newKelime = kelime.lower()
        harfTahmin = input('harf tahmin: ')
        if len(harfTahmin) == 1:
            if harfTahmin in newKelime:

                indeks = newKelime.index(harfTahmin)
                liste.pop(indeks)
                liste.insert(indeks,harfTahmin) == harfTahmin
                i += 1
            else:
                can -= 1
            print(liste)
        else:
            print('please enter one-letter: ')
    else:
        print(f'the word you failed to find is {kelime}')
        break










