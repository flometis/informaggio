#!/usr/bin/python3
# ./risultati.py "./latest_informaggio_csv" "ateneo=trieste,cdl=LT,annocorso=1"
# ./risultati.py "./latest_informaggio_csv" "ateneo=trieste,cdl=LT,annocorso=2"
def applicaFiltro(listarighe, mieifiltri = filtro):
    dothisfile = True
    if not mieifiltri == "totali":
        for miofiltro in mieifiltri.split(","):
            dothisfile = False
            for line in listarighe:
                listacolonne = line.split(",")
                if listacolonne[0] == miofiltro.split("=")[0]:
                    valorifiltro = miofiltro.split("=")[1].split("|")
                    for vf in valorifiltro:
                        if listacolonne[1] == vf:
                            dothisfile = True
            if dothisfile == False:
                break
    return dothisfile
