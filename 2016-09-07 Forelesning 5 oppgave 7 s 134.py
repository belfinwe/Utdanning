# Forelesning 5, oppgave 7 side 134

print('Alternativ: "Rød"(r), "blå" (b) eller "gul"(g).')


farge1 = input('Skriv inn primærfarge 1: ')
farge2 = input('Skriv inn primærfarge 2: ')

feilmelding = 'Ugyldig valg av primærfarge.'

if farge1 == 'r':
    if farge2 == 'b':
        print('Lilla.')
    else:
        if farge2 == 'g':
            print('Oransje.')
        else:
            feilmelding
else:
    if farge1 == 'b':
        if farge2 == 'r':
            print('Lilla.')
        else:
            if farge2 == 'g':
                print('Grønn.')
            else:
                feilmelding
    else:
        if farge1 == 'g':
            if farge2 == 'r':
                print('Oransje.')
            else:
                if farge2 == 'b':
                    print('Grønn.')
                else:
                    feilmelding
        else:
            feilmelding

