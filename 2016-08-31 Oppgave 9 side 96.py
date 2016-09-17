# Oppgave 9 side 96.

#Programkart
# Celsius til Fahrenheit, temperatur-konverterer.

# Program-start /E

# Les inn temp i Celsius /P

# Konverter Celsius til Fahrenheit /R

# Skriv ut temp i Fahrenheit /P

# Program-slutt /E

########################################################################

celsius = float(input('Skriv inn antall Celsius-grader:' ))

fahrenheit = (9/5)*celsius + 32

print(format(fahrenheit, '.1f'))
