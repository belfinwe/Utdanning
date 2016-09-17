# Program for å bestemme farge på ruletten.
# Steg 1, tester om tallet er gyldig.
# Steg 2, plasserer tallet i gyldig intervall.
# Steg 3, finn riktig farge for tall i intervall.

# Brukeren oppgir tall på ruletten.

tall = int(input('Hva er tallet på ruletten? '))

# Tester på gyldig verdi

if tall >= 0 and tall <= 36: # Ståle tester konsekvent nedre og øvre grense på intervallet.
    if tall == 0:
        print('Tallet er', tall, 'og er grønn på ruletten.')
    else:
        if tall <= 10:
            if (tall % 2) == 0:
                print('Tallet', tall, 'er partall og svart på ruletten.')
            else:
                print('Tallet', tall, 'er oddetall og rød på ruletten.')
        else:
            if tall <= 18:
                if (tall % 2) == 0:
                    print('Tallet', tall, 'er partall og rød på ruletten.')
                else:
                    print('Tallet', tall, 'er oddetall og svart på ruletten.')
            else:
                if tall <= 28:
                    if (tall % 2) == 0:
                        print('Tallet', tall, 'er partall og svart på ruletten.')
                    else:
                        print('Tallet', tall, 'er oddetall og rød på ruletten.')
                else:
                    if tall <= 36:
                        if (tall % 2) == 0:
                            print('Tallet', tall, 'er partall og rød på ruletten.')
                        else:
                            print('Tallet', tall, 'er oddetall og svart på ruletten.')                        
                    
                #Fortsette å indentifisere tallet.
else:
    print('Tallet er', tall, 'og er en ugyldig verdi på ruletten.')

print('Programmet avsluttet.') # Bare for å se at alle fungerer.

