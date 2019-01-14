#!/usr/bin/python3
import sys
import os

i = 0
correttoTot = 0

cartella = "./latest_informaggio_csv"
if len(sys.argv)>1:
    cartella = sys.argv[1]

folderlist = os.listdir(cartella)

ListaCSV = []
for ApriFile in folderlist:
    if ApriFile[-4:] == ".csv":
        ListaCSV.append(cartella + "/" + ApriFile)

nomeriga = ""
if len(sys.argv)>2:
    nomeriga = sys.argv[2]

filtro = "totali"
if len(sys.argv)>3:
    filtro = sys.argv[3]
    
def applicaFiltro(listarighe, miofiltro = filtro):
    dothisfile = True
    if not miofiltro == "totali":
        dothisfile = False
        for line in listarighe:
            listacolonne = line.split(",")
            if listacolonne[0] == miofiltro.split("=")[0]:
                valorifiltro = miofiltro.split("=")[1].split("|")
                for vf in valorifiltro:
                    if listacolonne[1] == vf:
                        dothisfile = True
    return dothisfile

ListaAtenei = [[],[]]
for fileName in ListaCSV:
    text_file = open(fileName, "r", encoding='utf-8')
    lines = text_file.read()
    text_file.close()

    listarighe = lines.split("\n")
    if len(listarighe)>31:
        dothisfile = applicaFiltro(listarighe)
        for line in listarighe:
            listacolonne = line.split(",")
            if listacolonne[0] == nomeriga:
                for n in range(1,len(listacolonne)):
                    nomeateneo = listacolonne[n]
                    pasquale = 1
                    if dothisfile:
                        if nomeateneo in ListaAtenei[0]:
                            rigaateneo = ListaAtenei[0].index(nomeateneo)
                            pasquale = pasquale + ListaAtenei[1][rigaateneo]
                            ListaAtenei[1][rigaateneo] = pasquale
                        else:
                            ListaAtenei[0].append(nomeateneo)
                            ListaAtenei[1].append(pasquale)
                
fname = cartella + "/risultati/risposta-"+ filtro +"-"+nomeriga+".csv"
text_file = open(fname, "w", encoding='utf-8')
text_file.write("")
text_file.close()
    
for riga in range(len(ListaAtenei[0])):
    print("|"+ str(ListaAtenei[0][riga]) + " | " + str(ListaAtenei[1][riga]) + "|")
    with open(fname, "a", encoding='utf-8') as myfile:
        myfile.write(str(ListaAtenei[0][riga]) + ", " + str(ListaAtenei[1][riga]) +"\n")
