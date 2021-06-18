
referenz1 = 1337
referenz2 = referenz1
if True:
 print("referenz1 =") #Zur veranschaulichung welche variable gemeint ist
 print(referenz1) # variablen inhalt vor der veränderung ausgeben
 print("referenz2 =")   #Zur veranschaulichung welche variable gemeint ist
 print(referenz2) # gleich bleibenden variablen inhalt ausgeben
 referenz1 =12345  # variablen inhalt von Variable1 verändern
 print("referenz1 =") #Zur veranschaulichung welche variable gemeint ist
 print(referenz1) # veränderten variablen inhalt ausgeben
 print("referenz2 =") #Zur veranschaulichung welche variable gemeint ist
 print(referenz2) #gleichgebliebene referenz aus geben
 del referenz1 #die erste refernz löschen
 print("refernz1 =") #Zur veranschaulichung welche variable gemeint ist
 print(referenz1) #den letzten inhalt der ersten referenz1 ausgeben
