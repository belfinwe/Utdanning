# Forelesning #5, oppgave 15 side 137, alternativ #1.
# Fant oppgåva til å være litt uklar, så laga ein versjon for kvar tolkning
# eg hadde av den.

sek = float(input('Skriv inn antall sekunder: '))

if sek >= 60:
    if sek >= 3600:
        if sek >= 86400:
            dogn = sek / 86400
            print(sek, 'sekunder blir', dogn, 'døgn.')
        else:
            timer = sek / 3600
            print(sek, 'sekunder blir', timer, 'timer.')
    else:
        minutter = sek / 60
        print(sek, 'sekunder blir', minutter, 'minutter.')
