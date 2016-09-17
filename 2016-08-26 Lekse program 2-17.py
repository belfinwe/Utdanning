# Eget alternativ program for 2-17, side 78 i boka.

# Mål for programmet:
# Få et antall sekunder som input, og utrede hvor mange timer, minutter og sekunder det utgjør.

#Steg 1: Kunden skriver inn antall sekunder som skal konverteres til timer, min og sek.

sek_fra_kunde = float(input('Skriv inn antall sekunder: '))

timer = int(sek_fra_kunde / 3600) # Gir timer i heltall.

sek_etter_timer = sek_fra_kunde - (3600 * timer)
minutter = int(sek_etter_timer / 60)
sekunder = sek_etter_timer - (60 * minutter)

print('Antall sekunder som skal konverteres:', sek_fra_kunde)
print('Timer:', timer)
print('Minutter:', minutter)
print('Sekunder:', sekunder)

