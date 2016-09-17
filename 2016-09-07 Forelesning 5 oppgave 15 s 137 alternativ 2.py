# Forelesning #5, oppgave 15 side 137, alternativ #2.
# Fant oppgåva til å være litt uklar, så laga ein versjon for kvar tolkning
# eg hadde av den.

sek = float(input('Skriv inn antall sekunder: '))

if sek >= 60:
    minutter = sek / 60
    print(sek, 'sekunder blir', minutter, 'minutter.')
    if sek >= 3600:
        timer = sek / 3600
        print(sek, 'sekunder blir', timer, 'timer.')
        if sek >= 86400:
            dogn = sek / 86400
            print(sek, 'sekunder blir', dogn, 'døgn.')
