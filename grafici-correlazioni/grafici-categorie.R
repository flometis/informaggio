#!/usr/bin/Rscript

library(ggplot2);
require(gridSVG);


path <- "../latest_informaggio_csv/risultati/";
euroVal = c("base", "medio", "avanzato", "nessuno", "tutto");
categorie <- c("elaborazioneinformazioni", "creazionecontenuti", "comunicazione", "risoluzioneproblemi","sicurezza");
#Valori minimi e massimi per ciascuna categoria
catMax <- c(8,5,3,2.5,5.5);
catMin <- c(-12,-10,-3,-2.5,-6.5);



for(ic in 1:length(categorie)){
tutti <- read.table(text = "", col.names=c("Risposte" , "Utenti"), colClasses = c("numeric", "numeric"));

for(iv in 1:length(euroVal)){
filename <- paste(path,"quiz-", categorie[ic], "=", euroVal[iv], "-", categorie[ic],".csv", sep="");
file <- read.table(filename,header=FALSE, sep=",", col.names=c("Risposte" , "Utenti"), colClasses = c("numeric", "numeric"));

#Aggiungo i valori minimi e massimi come punti di riferimento
tutti[nrow(tutti) + 1,] = list(catMin[ic], 0);
tutti[nrow(tutti) + 1,] = list(catMax[ic], 0);

for(it in 1:length(file$Risposte)){
if (is.element(file$Risposte[it], tutti$Risposte)) {
tutti$Utenti[tutti$Risposte==file$Risposte[it]] <- tutti$Utenti[tutti$Risposte==file$Risposte[it]] + file$Utenti[it];
} else {
tutti[nrow(tutti) + 1,] = list(file$Risposte[it], file$Utenti[it]);
}
}
}
#print(categorie[ic])
#print(tutti)

#Calcolo le percentuali
tutti$Utenti <- (tutti$Utenti*100)/sum(tutti$Utenti);
#Ordino in base al punteggio
tutti <- tutti[order(tutti$Risposte),];
tutti$Risposte <- as.factor(tutti$Risposte);

histogram = ggplot(tutti, aes(x=tutti$Risposte, y=tutti$Utenti, fill=tutti$Risposte)) + geom_bar(stat="identity");
mylabels = paste0(as.integer(tutti$Utenti), "%");
histogram = histogram + stat_count(aes(y=..count..,label=mylabels),geom="text",vjust=-1)
#histogram = histogram + scale_x_discrete(labels=tutti$Risposte);
histogram = histogram + labs(x = NULL, y = NULL, fill = NULL, title = categorie[ic]);
histogram = histogram + theme_classic() + theme(axis.line = element_blank(),
            axis.text.y = element_blank(),
            axis.ticks = element_blank(),
            plot.title = element_text(hjust = 0.5, color = "#666666"));
#Esporto il grafico in un file SVG
print(histogram);
grid.export(paste("./", categorie[ic], ".svg", sep=""),addClasses=TRUE);
}
