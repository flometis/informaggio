#!/bin/bash
rm ./latest_informaggio_csv/*
mkdir latest_informaggio_csv
mkdir latest_informaggio_csv/risultati
mkdir latest_informaggio_csv/risultati/svg
rm ./latest_informaggio_csv/anziani/*
mkdir latest_informaggio_csv/anziani/risultati
mkdir latest_informaggio_csv/anziani/risultati/svg
unzip latest_informaggio_csv.zip -d latest_informaggio_csv
./puliscicsv.py "./latest_informaggio_csv"
./risultati.py "./latest_informaggio_csv"
./risultati.py "./latest_informaggio_csv/anziani"

./estraidomanda.py "./latest_informaggio_csv" "allinurl"
./estraidomanda.py "./latest_informaggio_csv" "siti_affidabili"
./estraidomanda.py "./latest_informaggio_csv" "file_rar"
./estraidomanda.py "./latest_informaggio_csv" "hardware"
./estraidomanda.py "./latest_informaggio_csv" "https"
./estraidomanda.py "./latest_informaggio_csv" "https" "ateneo=trieste"
./estraidomanda.py "./latest_informaggio_csv" "spyware"

rm "./Rplots.pdf"
./crea-grafici.R "./latest_informaggio_csv/risultati/"
./crea-grafici.R "./latest_informaggio_csv/anziani/risultati/"
