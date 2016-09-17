#Beregning av bruttolønn.

#Først trenger vi input/inndata fra brukere.

timelonn = int(input('Hva er din timelønn? '))
antall_timer = int(input('Hvor mange timer har du arbeidet? '))

#Beregner vi bruttolønn
bruttolonn = timelonn * antall_timer

#Skriver ut lønnsberegning
print('Din bruttolønn er da', bruttolonn)

#Programmet kræsjet her (med vilje), skal gå igjennom på fredag? Fikset med å legge til int
#Variabelnavn notasjon, altså enten antall_timer eller antallTimer(<- "lowerCamelCase").
#Den med understrek som brukes mest, og i boka.
#Det bruker vi når det er variabelnavn som er sammensatt av flere ord
#jammenfør lærebok side 62.
