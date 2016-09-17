# Program for å bestemme farge på ruletten.
# Steg 1, tester om tallet er gyldig.
# Steg 2, plasserer tallet i gyldig intervall.

# Brukeren oppgir tall på ruletten.

tall = int(input('Hva er tallet på ruletten? '))

# Tester på gyldig verdi

if tall >= 0 and tall <= 36: # Ståle tester konsekvent nedre og øvre grense på intervallet.
    if tall == 0:
        print('Tallet er', tall, 'og er grønn på ruletten.')
    else:
        if tall <= 10:
            print('Tallet er', tall, 'og er i intervallet [1, 10].')
        else:
            if tall <= 18:
                print('Tallet er', tall, 'og er i intervallet [11, 18].')
            else:
                print('Tallet er', tall, 'og er i intervallet [19, 36].')
                #Fortsette å indentifisere tallet.
else:
    print('Tallet er', tall, 'og er en ugyldig verdi på ruletten.')

print('Programmet avsluttet.') # Bare for å se at alle fungerer.
