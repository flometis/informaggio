#!/bin/bash
curl http://www.zorbaproject.org/informaggio/list.php > /dev/null
rm latest_informaggio_csv.zip
wget http://www.zorbaproject.org/informaggio/latest_informaggio_csv.zip
rm -r ./latest_informaggio_csv
mkdir latest_informaggio_csv
mkdir latest_informaggio_csv/risultati
unzip latest_informaggio_csv.zip -d latest_informaggio_csv 
