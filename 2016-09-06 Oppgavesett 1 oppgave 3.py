# Oppgavesett 1, oppgave 3.
# Author: Joakim Rønneberg Nilsen

poeng = float(input('Skriv inn poengsum: '))

if poeng >= 92:
    karakter = 'A'
else:
    if poeng >= 77:
        karakter = 'B'
    else:
        if poeng >= 58:
            karakter = 'C'
        else:
            if poeng >= 46:
                karakter = 'D'
            else:
                if poeng >= 40:
                    karakter = 'E'
                else:
                    karakter = 'F'


print('Karakteren er:', karakter)
