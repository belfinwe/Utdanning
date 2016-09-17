# Program 3-2, beregning av overtid, side 109.

# Srkiv inn arbeidstimer
# Skriv inn timelønn

# Jobbet mer enn 40 timer?
# ja -> Beregn bruttolønn med overtid
# nei -> bergen bruttolønn uten overtid
# Vis lønn.

##############################

timer = float(input('Skriv inn antall timer: '))
timelonn = float(input('Skriv inn timelønn: '))
ot_multi = 1.5
grunn_timer = 40


if timer > grunn_timer:
    bruttolonn = timelonn * grunn_timer
    overtid_timer = (timer - grunn_timer) #Angir hvor mange timer overtid
    overtid = overtid_timer * (ot_multi * timelonn)  #Angir timesatsen for overtid
    bruttolonn += overtid
    print('Bruttolønn med overtid:', bruttolonn)

else:
    bruttolonn = timer * timelonn
    print('Bruttolønn uten overtid:', bruttolonn)
