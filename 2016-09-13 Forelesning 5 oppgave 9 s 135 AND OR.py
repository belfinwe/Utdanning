tall = float(input('Skriv inn tall: '))

feilmelding = 'Skriv inn rett tall din n00b!!'
tall_1 = tall % 2 #Avgjør om tall er oddetall eller partall.

if tall < 0 or tall > 36:
    print(feilmelding)
    
elif tall == 0:
        print('Grønn.')
        
elif tall <= 10 or (tall > 18 and tall < 29):
    if tall_1 == 0:
        print('Svart (partall).')
    else:
        print('Rødt (oddetall).')
else:
    if tall_1 == 0:
        print('Rødt (partall).')
    else:
        print('Svart (oddetall).')

        
