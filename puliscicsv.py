#!/usr/bin/python3

import sys
import os
import re

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

for fileName in ListaCSV:
    text_file = open(fileName, "r", encoding='utf-8')
    lines = text_file.read()
    text_file.close()

    newCSV = ""

    listarighe = lines.split("\n")
    for line in listarighe:
        listacolonne = line.split(",")
        if listacolonne[0] == "ateneo":
            listacolonne[1] = listacolonne[1].lower()
            listacolonne[1] = re.sub(" $", "", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("università (degli|del|della|dell'|dei|di)* (studi )*(di )*", "", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("( )*di ", "", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("’", "'", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("( )*-( *)", "", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("statale", "milano", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("unimi", "milano", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("milano( )*milano", "milano", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("università milano", "milano", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("milano ", "milano", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("uniupo", "", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("upo", "vercelli", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("vercelli vercelli", "vercelli", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("piemonte orientale", "vercelli", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("ca' foscari", "venezia", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("federico ii", "napoli", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("venezia( )*venezia", "venezia", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("festa del perdono", "", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("unisalento", "salento", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("unisslento", "salento", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("lecce", "salento", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("uniurb", "urbino", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("unimc", "macerata", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("vebezia", "venezia", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("alma mater studiorum", "bologna", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("unibo", "bologna", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("^ ", "", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("( )baru( )", "bari", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("roma tor vergata", "tor vergata", listacolonne[1], flags=re.DOTALL)
            line = listacolonne[0] + "," + listacolonne[1]
            if listacolonne[1] == "s.sofia" or listacolonne[1] == "mainz" or listacolonne[1] == "lettere": 
                newCSV = ""
                break
        if listacolonne[0] == "nomecorso":
            listacolonne[1] = listacolonne[1].lower()
            listacolonne[1] = re.sub(" $", "", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("^ ", "", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("curriculum.*", "", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("\(.*", "", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("corso di ", "", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("laurea (magistrale )*in ", "", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("specializzata", "specialistica", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub(" di conferenza", "", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("comuniazione interlimguistica applicata", "comunicazione interlinguistica applicata", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub(":.*", "", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("l-10", "", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("lettere a( )*$", "lettere", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("-( )*$", "", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub(" $", "", listacolonne[1], flags=re.DOTALL)
            listacolonne[1] = re.sub("^ ", "", listacolonne[1], flags=re.DOTALL)
            line = listacolonne[0] + "," + listacolonne[1]
            if listacolonne[1] == "": 
                newCSV = ""
                break
        if listacolonne[0] == "annonascita":
            if listacolonne[1] == "": 
                #newCSV = ""
                #break
                text_file = open(fileName, "w", encoding='utf-8')
                text_file.write("")
                text_file.close()
                fileName = re.sub("(/[^/]*?)\.csv", "/anziani\g<1>-anziano.csv", fileName, flags=re.DOTALL)
            elif int(listacolonne[1]) <1993: 
                #newCSV = ""
                #break
                text_file = open(fileName, "w", encoding='utf-8')
                text_file.write("")
                text_file.close()
                fileName = re.sub("(/[^/]*?)\.csv", "/anziani\g<1>-anziano.csv", fileName, flags=re.DOTALL)
        newCSV = newCSV + line + "\n"
        
    text_file = open(fileName, "w", encoding='utf-8')
    text_file.write(newCSV)
    print(newCSV)
    text_file.close()
