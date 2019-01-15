#!/bin/bash
rm ./latest_informaggio_csv/*
mkdir latest_informaggio_csv
mkdir latest_informaggio_csv/risultati
rm latest_informaggio_csv/risultati/*
mkdir latest_informaggio_csv/risultati/svg
rm latest_informaggio_csv/risultati/svg/*
rm ./latest_informaggio_csv/anziani/*
mkdir latest_informaggio_csv/anziani
mkdir latest_informaggio_csv/anziani/risultati
rm latest_informaggio_csv/anziani/risultati/*
rm latest_informaggio_csv/anziani/risultati/svg/*
mkdir latest_informaggio_csv/anziani/risultati/svg
unzip latest_informaggio_csv.zip -d latest_informaggio_csv
./puliscicsv.py "./latest_informaggio_csv"
./risultati.py "./latest_informaggio_csv"
./risultati.py "./latest_informaggio_csv/anziani"

listafiltri=("interesse=S" "competenza=insufficiente" "competenza=sufficiente" "competenza=scarsa" "competenza=buona" "competenza=ottima")
for i in ${listafiltri[@]}; do
    ./risultati.py "./latest_informaggio_csv" ${i}
done

#listafiltri=("elaborazioneinformazioni" "creazionecontenuti" "comunicazione" "risoluzioneproblemi" "sicurezza")
#for i in ${listafiltri[@]}; do
#    ./risultati.py "./latest_informaggio_csv" "${i}=base"
#    ./risultati.py "./latest_informaggio_csv" "${i}=medio"
#    ./risultati.py "./latest_informaggio_csv" "${i}=avanzato"
#    ./risultati.py "./latest_informaggio_csv" "${i}=nessuno"
#    ./risultati.py "./latest_informaggio_csv" "${i}=tutto"
#done
#cd "./latest_informaggio_csv/risultati/"
#ls | grep -P '^.*-elaborazioneinformazioni.*-(?!file_rar|duckduckgo|siti_affidabili|allinurl|google).*$' | xargs -d"\n" rm
#ls | grep -P '^.*-creazionecontenuti.*-(?!creazione_pdf|markup|collaborazione).*$' | xargs -d"\n" rm
#ls | grep -P '^.*-comunicazione.*-(?!social_network|inviocartella).*$' | xargs -d"\n" rm
#ls | grep -P '^.*-risoluzioneproblemi.*-(?!spyware).*$' | xargs -d"\n" rm
#ls | grep -P '^.*-sicurezza.*-(?!https|password|phishing).*$' | xargs -d"\n" rm
#cd "../../"

./estraidomanda.py "./latest_informaggio_csv" "allinurl"
./estraidomanda.py "./latest_informaggio_csv" "siti_affidabili"
./estraidomanda.py "./latest_informaggio_csv" "file_rar"
./estraidomanda.py "./latest_informaggio_csv" "hardware"
./estraidomanda.py "./latest_informaggio_csv" "hardware" "competenza=ottima"
./estraidomanda.py "./latest_informaggio_csv" "https"
./estraidomanda.py "./latest_informaggio_csv" "https" "ateneo=trieste"
./estraidomanda.py "./latest_informaggio_csv" "spyware"

rm "./Rplots.pdf"
./crea-grafici.R "./latest_informaggio_csv/risultati/"
./crea-grafici.R "./latest_informaggio_csv/anziani/risultati/"
