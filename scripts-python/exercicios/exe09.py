#Obtendo valores cm e mm em metros

metros = int (input ('Digite uma metragem: '))

cm = 100
mm = 1000

scm = cm * metros
smm = mm * metros

print ('{}m corresponde a {}cm e {}mm'.format(metros, scm, smm))
