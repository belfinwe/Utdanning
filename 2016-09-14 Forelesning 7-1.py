# Program for å bestemme farge på ruletten.
# Steg 1, tester om tallet er gyldig.

# Brukeren oppgir tall på ruletten.

tall = int(input('Hva er tallet på ruletten? '))

# Tester på gyldig verdi

if tall >= 0 and tall <= 36: # Ståle tester konsekvent nedre og øvre grense på intervallet.
    print('Tallet er', tall, 'og er en gyldig verdi på ruletten.')
else:
    print('Tallet er', tall, 'og er en ugyldig verdi på ruletten.')

print('Programmet avsluttet.') # Bare for å se at alle fungerer.
