# Rulett alternativ 3
# Tar utgangspunkt i hvilke farger som gjelder

# Brukeren oppgir verdi på ruletten

tall = int(input('Hva er tallet på ruletten: '))

# Tester på gyldig verdi og beregner riktig farge for gyldige verdier

if tall >= 0 and tall <= 36:
    if tall == 0:
        print('Tallet er markert grønt på ruletten.')
    else:
        # Hele if-setningen deles over flere linjer, må da stå i ekstra ()
        if ((tall >= 1 and tall <= 10 and (tall % 2) == 0)
        or (tall >= 11 and tall <= 18 and (tall % 2) != 0)
        or (tall >= 19 and tall <= 28 and (tall % 2) == 0)
        or (tall >= 29 and tall <= 36 and (tall % 2) != 0)):
            print('Tallet er markert svart på ruletten.')
        else:
            print('Tallet er markert rødt på ruletten.')
else:
    print('Du har ikke oppgitt gyldig verdi på ruletten.')

print('Program avsluttet.')
print()
print()
