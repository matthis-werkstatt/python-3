woerter = {"Germany" : "Deutschland", 
           "Spain" : "Spanien",
           "Greece" : "Griechenland"}
           
fobj = open("ausgabe.txt", "w")
for engl in woerter:
    fobj.write("{} {}\n".format(engl, woerter[engl]))
fobj.close()
