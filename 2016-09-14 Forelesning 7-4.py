# Rulett.
# Løst med uavhengig if-tester som tester intervaller og talltype.

# Brukeren oppgir tall på ruletten

tall = int(input('Hva er tallet på ruletten? '))

# Tester om gyldig verdi
if tall >= 0 and tall <= 36:
    if tall == 0:
        print('Grønn på ruletten.')
    else:
        if tall >= 1 and tall <= 10 and (tall % 2) == 0:
            print('Tallet', tall, 'er partall og svart på ruletten.')
        if tall >= 1 and tall <= 10 and (tall % 2) != 0:
            print('Tallet', tall, 'er oddetall og rødt på ruletten.')
            
        if tall >= 11 and tall <= 18 and (tall % 2) == 0:
            print('Tallet', tall, 'er partall og rødt på ruletten.')
        if tall >= 11 and tall <= 18 and (tall % 2) != 0:
            print('Tallet', tall, 'er oddetall og svart på ruletten.')
            
        if tall >= 19 and tall <= 28 and (tall % 2) == 0:
            print('Tallet', tall, 'er partall og svart på ruletten.')
        if tall >= 19 and tall <= 28 and (tall % 2) != 0:
            print('Tallet', tall, 'er oddetall og rød på ruletten.')
            
        if tall >= 29 and tall <= 36 and (tall % 2) == 0:
            print('Tallet', tall, 'er partall og rødt på ruletten.')
        if tall >= 29 and tall <= 36 and (tall % 2) != 0:
            print('Tallet', tall, 'er oddetall og svart på ruletten.')
        

else:
    print('Du har ikke oppgitt en gyldig verdi på ruletten.')

print('Program avsluttet.')

# Til fredag:
# gjør ferdig 2016-09-14 Forelesning7-3, både intervaller og tilordning av verdi
# gjør ferdig 2016-09-14 Forelesning7-4 (dette programmet),
# dvs fortsette med uavhengige if-tester.
