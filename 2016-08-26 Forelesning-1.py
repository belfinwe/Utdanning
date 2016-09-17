#Heltall og desimaltall variabler,ArithmeticError, og beregninger.

heltall1 = 15
heltall2 = 30

desimaltall1 = 2.5
desimaltall2 = 9.99

sum1 = heltall1 + heltall2
print('sum1 blir', sum1, 'og det er en heltallsvariabel.') #Arver egenskaper, blir en heltallsvariabel.

sum2 = desimaltall1 + desimaltall2
print('sum2 blir', sum2, 'og det er en desimaltallsvariabel.')

sum3 = heltall1 + heltall2 + desimaltall1 + desimaltall2
print('sum3 blir', sum3, 'og det er en desimaltallsvariabel.')

#Side 8: operations on ints produce ints.
#And operations on floats produce floats.

#Dersom vi har operasjoner som bruker variable av både heltall og desimaltall blir resultatet alltid deismaltall.
#Det gjelder uavhengig av matematisk operator.

desimaltall3 = float(input('Skriv inn et desimaltall: '))
print('Du skrev inn tallet: ', desimaltall3)
