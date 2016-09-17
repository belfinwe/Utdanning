# Oppgavesett 1, oppgave 2.

print('Oppgavesett 1, oppgave 2.')

km = float(input('Skriv inn antall kilometer: '))

alt_1 = 750
alt_2 = 300 + (2 * km)
alt_3 = 150 + (4 * km)

print('Alternativ 1:', alt_1)
print('Alternativ 2:', alt_2)
print('Alternativ 3:', alt_3)

# kunde_valg = min(alt_1, alt_2, alt_3)
print()

if alt_1 < alt_2:
    print('Alternativ 1 er billigst.')
else:
    if alt_2 < alt_3:
        print('Alternativ 2 er billigst.')
    else:
        print('Alternativ 3 er billigst.')

#if kunde_valg == alt_1:
#    svar = 'alternativ 1.'
#elif kunde_valg == alt_2:
#    svar = 'alternativ 2.'
#elif kunde_valg == alt_3:
#    svar = 'alternativ 3.'


#print('Det beste valget for kunden er alternativ', svar)
