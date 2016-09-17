# Farge på ruletten
# Minimalisere betingeslene for intervallet [1, 10] og [29, 36]
# Med inndatatest i begynnelsen på programmet

# Variabel til bruk av inndatatest
nytt_tall = 'ja'

# Løkke som sikrer oss gydlig verdi
while nytt_tall == 'ja':
    # Brukeren oppgir verdi på ruletten
    tall = int(input('Hva er tatllet på ruletten? '))

    # Tester om gyldig verdi
    if tall >= 0 and tall <= 36:
        nytt_tall = 'nei'
    else:
        print('Ugyldig verdi, prøv på nytt.')

if tall == 0:
    print('Tallet er markert grønt på ruletten.')
else:
    if ((tall <= 10 and (tall % 2) == 0)
    or (tall >= 11 and tall <= 18 and (tall % 2) != 0)
    or (tall >= 19 and tall <= 28 and (tall % 2) == 0)
    or (tall >= 29 and (tall % 2) != 0)):
        print('Tallet er markert svart på ruletten.')
    else:
        print('Tallet er markert rødt på ruletten.')

print('Program avsluttet.')
