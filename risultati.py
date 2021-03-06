#!/usr/bin/python3
import sys
import os
# i=siti siti_affidabili
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


filtro = "totali"
if len(sys.argv)>2:
    filtro = sys.argv[2]
    
# ./risultati.py "./latest_informaggio_csv" "ateneo=trieste,cdl=LT,annocorso=2"
def applicaFiltro(listarighe, mieifiltri = filtro):
    dothisfile = True
    if not mieifiltri == "totali":
        dothisfile = False
        for line in listarighe:
            listacolonne = line.split(",")
            for miofiltro in mieifiltri.split(","):
                if listacolonne[0] == miofiltro.split("=")[0]:
                    valorifiltro = miofiltro.split("=")[1].split("|")
                    if listacolonne[1] in valorifiltro:
                        dothisfile = True
                    else:
                        dothisfile = False
                        break
    return dothisfile

listarigheTotali = ["disclaimer", "annonascita", "sesso", "regione", "cdl", "annocorso", "nomecorso", "ateneo", "anniuso", "anniinternet", "interesse", "computerpersonale", "os", "altroos", "dispositivo", "altrodispositivo", "attivita", "altroattivita", "sostituzionehardware", "corsoit", "ecdl", "espertoliceo", "espertouniversita", "problemi", "competenza", "elaborazioneinformazioni", "creazionecontenuti", "comunicazione", "risoluzioneproblemi", "sicurezza"]

#Risposte domande anagrafiche
for nomeriga in listarigheTotali:
    ListaAtenei = [[],[]]
    for fileName in ListaCSV:
        text_file = open(fileName, "r", encoding='utf-8')
        lines = text_file.read()
        text_file.close()
        
        listarighe = lines.split("\n")
        if len(listarighe)>31:
            #dothisfile = applicaFiltro(listarighe)
            dothisfile = True
            for line in listarighe:
                listacolonne = line.split(",")
                if listacolonne[0] == nomeriga:
                    nomeateneo = listacolonne[1]
                    pasquale = 1
                    if dothisfile:
                        if nomeateneo in ListaAtenei[0]:
                            rigaateneo = ListaAtenei[0].index(nomeateneo)
                            pasquale = pasquale + ListaAtenei[1][rigaateneo]
                            ListaAtenei[1][rigaateneo] = pasquale
                        else:
                            ListaAtenei[0].append(nomeateneo)
                            ListaAtenei[1].append(pasquale)
                    
    #fname = cartella + "/risultati/anagrafica-"+ filtro +"-"+nomeriga+".csv"
    fname = cartella + "/risultati/anagrafica-"+nomeriga+".csv"
    text_file = open(fname, "w", encoding='utf-8')
    text_file.write("")
    text_file.close()
    
    for riga in range(len(ListaAtenei[0])):
        print("|"+ str(ListaAtenei[0][riga]) + " | " + str(ListaAtenei[1][riga]) + "|")
        with open(fname, "a", encoding='utf-8') as myfile:
            myfile.write(str(ListaAtenei[0][riga]) + ", " + str(ListaAtenei[1][riga]) +"\n")

rispostemultiple = {
"file_rar" : {"archivio compresso" : 1, "immagine" : -1, "installer": -1, "word": -1, "Non so": 0},
"creazione_pdf" : {"salvo da word" : 1, "ocr" : -1, "stampo e scansiono": -1, "Adobe Reader" : -1, "Non so" : 0},
"markup" : {"wordpress": -1, "javascript": -1, "html": 1, "xml":1, "latex": 1, "excel":-1, "jpeg":-1, "linux":-1,  "Non so":0},
"hardware" : {"hard disk":1,"stampante":1,"cloud computing":-1, "sistema operativo":-1, "supporti SSD":1, "cavo hdmi":1, "browser":-1, "indirizzo IP":-1, "Non so": 0},
"duckduckgo" : {"motorericerca":1, "ecommerce":-1, "p2p":-1, "virus":-1, "Non so":0},
"siti_affidabili" : {"ansa":1, "corrieredellasera":1, "treccani":1, "fattoquotidaino":-1, "wikipedia":-1, "retenews24":-1, "facebook":-1, "Non so":0},
"https" : {"pornhub":1, "musicagratis":1, "unicredit":1, "units":-1, "googlemail":-1, "Non so": 0},
"allinurl" : {"restringe risultati":1, "non esiste":-1, "carattere jolly":-1, "dark web":-1, "Non so": 0}, 
"social_network" : {"opzioni privacy":1, "tutto pubblico": -1, "tutto privato": -1, "rimozione definitiva": -1, "Non so":0},
"password" : {"cambio password":1, "stessa password":-1, "scrivo le password": -0.5, "nessuna":-1, "Non so":0},
"phishing" : {"controllo indirizzo":1, "apro link":-1, "cestino":0.5, "rispondo":-1, "Non so":0},
"google" : {"siti":1, "tutto":-1, "non indicizzati":-1, "illegali":1, "Non so": 0},
"inviocartella" : {"google drive":1, "vari messaggi email":-1, "cd":-1, "pendrive e posta":-1, "ftp":1, "Non so":0},
"collaborazione" : {"google docs":1, "via email":-0.5, "wordpress": -1, "pendrive": -0.5, "Non so":0},
"spyware" : {"antimalware":1, "formatto":-1, "tecnico": -0.5, "modalita provvisoria":1, "riavvio":-1, "altro browser":-1, "google":0.5, "Non so":0}
}

#Punteggi totali nelle varie domande
for domanda in rispostemultiple:
    ListaAtenei = [[],[]]
    for fileName in ListaCSV:
        text_file = open(fileName, "r", encoding='utf-8')
        lines = text_file.read()
        text_file.close()
        
        listarighe = lines.split("\n")
        if len(listarighe)>31:
            dothisfile = applicaFiltro(listarighe)
            if dothisfile == True:
                for line in listarighe:
                    listacolonne = line.split(",")
                    if listacolonne[0] == domanda:
                        punteggio = 0
                        for i in range(1,len(listacolonne)):
                            punteggio = punteggio + rispostemultiple[domanda][listacolonne[i]]
                        pasquale = 1
                        if punteggio in ListaAtenei[0]:
                            rigaateneo = ListaAtenei[0].index(punteggio)
                            pasquale = pasquale + ListaAtenei[1][rigaateneo]
                            ListaAtenei[1][rigaateneo] = pasquale
                        else:
                            ListaAtenei[0].append(punteggio)
                            ListaAtenei[1].append(pasquale)
    fname = cartella + "/risultati/quiz-" + filtro + "-" + domanda+".csv"
    text_file = open(fname, "w", encoding='utf-8')
    text_file.write("")
    text_file.close()
    
    print(domanda)
    for riga in range(len(ListaAtenei[0])):
        print("|"+ str(ListaAtenei[0][riga]) + " | " + str(ListaAtenei[1][riga]) + "|")
        with open(fname, "a", encoding='utf-8') as myfile:
            myfile.write(str(ListaAtenei[0][riga]) + ", " + str(ListaAtenei[1][riga]) +"\n")
            
categorie = {
"elaborazioneinformazioni" : ["file_rar", "duckduckgo", "siti_affidabili", "allinurl", "google"],
"creazionecontenuti": ["creazione_pdf", "markup", "collaborazione"],
"comunicazione": ["social_network", "inviocartella"],
"risoluzioneproblemi": ["spyware"],
"sicurezza": ["https", "password", "phishing"]
}
euroVal = ["base", "medio", "avanzato", "nessuno", "tutto"]
#Punteggi totali nelle varie categorie
for categoria in categorie:
    for valutazione in euroVal:
        miofiltro = categoria + "=" + valutazione
        ListaAtenei = [[],[]]
        for domanda in rispostemultiple:
            for fileName in ListaCSV:
                text_file = open(fileName, "r", encoding='utf-8')
                lines = text_file.read()
                text_file.close()
                
                listarighe = lines.split("\n")
                if len(listarighe)>31:
                    dothisfile = applicaFiltro(listarighe, miofiltro)
                    if dothisfile == True:
                        for line in listarighe:
                            listacolonne = line.split(",")
                            if listacolonne[0] == domanda and domanda in categorie[categoria]:
                                punteggio = 0
                                for i in range(1,len(listacolonne)):
                                    punteggio = punteggio + rispostemultiple[domanda][listacolonne[i]]
                                pasquale = 1
                                if punteggio in ListaAtenei[0]:
                                    rigaateneo = ListaAtenei[0].index(punteggio)
                                    pasquale = pasquale + ListaAtenei[1][rigaateneo]
                                    ListaAtenei[1][rigaateneo] = pasquale
                                else:
                                    ListaAtenei[0].append(punteggio)
                                    ListaAtenei[1].append(pasquale)
        fname = cartella + "/risultati/quiz-" + miofiltro + "-" + categoria+".csv"
        text_file = open(fname, "w", encoding='utf-8')
        text_file.write("")
        text_file.close()
    
        print(categoria)
        for riga in range(len(ListaAtenei[0])):
            print("|"+ str(ListaAtenei[0][riga]) + " | " + str(ListaAtenei[1][riga]) + "|")
            with open(fname, "a", encoding='utf-8') as myfile:
                myfile.write(str(ListaAtenei[0][riga]) + ", " + str(ListaAtenei[1][riga]) +"\n")
            
#punteggi dei vari utenti
ListaAtenei = [[],[]]
for fileName in ListaCSV:
    text_file = open(fileName, "r", encoding='utf-8')
    lines = text_file.read()
    text_file.close()
    punteggio = 0
    listarighe = lines.split("\n")
    if len(listarighe)>31:
        dothisfile = applicaFiltro(listarighe)
        for line in listarighe:
            listacolonne = line.split(",")
            domanda = listacolonne[0]
            if domanda in rispostemultiple:
                    for i in range(1,len(listacolonne)):
                        punteggio = punteggio + rispostemultiple[domanda][listacolonne[i]]
        if dothisfile:
            if punteggio in ListaAtenei[0]:
                rigaateneo = ListaAtenei[0].index(punteggio)
                pasquale = 1 + ListaAtenei[1][rigaateneo]
                ListaAtenei[1][rigaateneo] = pasquale
            else:
                ListaAtenei[0].append(punteggio)
                ListaAtenei[1].append(1)
    fname = cartella + "/risultati/punteggi-"+filtro+".csv"
    text_file = open(fname, "w", encoding='utf-8')
    text_file.write("")
    text_file.close()
    
    for riga in range(len(ListaAtenei[0])):
        print("|"+ str(ListaAtenei[0][riga]) + " | " + str(ListaAtenei[1][riga]) + "|")
        with open(fname, "a", encoding='utf-8') as myfile:
            myfile.write(str(ListaAtenei[0][riga]) + ", " + str(ListaAtenei[1][riga]) +"\n")

#risposte Non so
fileTot = 0
fileNonso = 0
nonsototali = 0
rispostetotali = 0
for fileName in ListaCSV:
    text_file = open(fileName, "r", encoding='utf-8')
    lines = text_file.read()
    text_file.close()
    
    listarighe = lines.split("\n")
    if len(listarighe)>31:
        fileTot = fileTot +1
        dothisfile = applicaFiltro(listarighe)
        if dothisfile:
            for line in listarighe:
                listacolonne = line.split(",")
                domanda = listacolonne[0]
                if domanda in rispostemultiple:
                    if "Non so" in listacolonne:
                        fileNonso = fileNonso + 1
                        break
            for line in listarighe:
                listacolonne = line.split(",")
                domanda = listacolonne[0]
                if domanda in rispostemultiple:
                    rispostetotali = rispostetotali + len(listacolonne) -1
                    if "Non so" in listacolonne:
                        nonsototali = nonsototali + 1
fname = cartella + "/risultati/nonso-"+filtro+".csv"
text_file = open(fname, "w", encoding='utf-8')
text_file.write("File totali: " + str(fileTot) +"\nFile con almeno un Non so: "+str(fileNonso)+"\nRisposte totali: "+str(rispostetotali)+"\nNon so totali: "+str(nonsototali))
text_file.close()
