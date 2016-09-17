# Skal kode etter programkartet vi laget i stad: 
# Beregning av bruttolønn, skattetrekk og netto utbetalt.

# Først trenger vi inpt/inndata fra brukeren.
timelonn = float(input('Hva er din timelønn? '))
antall_timer = float(input('Hvor mange timer har du arbeidet? '))

# Beregner bruttolønn.
bruttolonn = timelonn * antall_timer

# Print ut delberegninger underveis for å feilsøke.

# Finner riktig skattesats og beregner skatt & netto lønn.
if bruttolonn < 20000:
    skattesats = 28
else:
    if bruttolonn < 30000:
        skattesats = 35
    else:
        skattesats = 40

skattetrekk_kr = (bruttolonn * skattesats) / 100
nettolonn = bruttolonn - skattetrekk_kr

# Skriver ut bruttolønn, skattesats, skatt i kroner og nettolønn.
print('Bruttolønn:', format(bruttolonn, '.2f'))
print('Skatteprosenten er:', format(skattesats, '.2f'), '%, og skattetrekket i kroner er', format(skattetrekk_kr, '.2f'))
print('Du får utbetalt', format(nettolonn, '.2f'))
