# Oppgavesett 1, oppgave 4.

tall_1 = float(input('Skriv inn tall 1: '))
tall_2 = float(input('Skriv inn tall 2: '))
tall_3 = float(input('Skriv inn tall 3: '))
tall_4 = float(input('Skriv inn tall 4: '))
tall_5 = float(input('Skriv inn tall 5: '))


if tall_1 < tall_2:
    minste = tall_1
else:
    minste = tall_2

if minste > tall_3:
    minste = tall_3
else:
    minste = minste

if minste > tall_4:
    minste = tall_4
else:
    minste = minste

if minste > tall_5:
    minste = tall_5
else:
    minste = minste

#laveste_tall = min(tall_1, tall_2, tall_3, tall_4, tall_5)

#print('Det laveste tallet er:', laveste_tall)
print('Det laveste tallet er:', minste)
