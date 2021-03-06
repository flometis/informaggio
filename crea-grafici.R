#!/usr/bin/Rscript

#Se lo script viene eseguito da amministratore (permessi di scrittura nella cartella delle librerie), installa le librerie
if (file.access(.libPaths()[1],2)==0) {
    install.packages("ggplot2",repos = "https://cran.stat.unipd.it/");
    install.packages("gridSVG",repos = "https://cran.stat.unipd.it/");
    print("Se ci sono stati errori, esegui sudo apt-get install libxml2-dev e riprova.")
    print("Sembra che tu sia amministratore, sarebbe meglio procedere solo da utente semplice. Vuoi comunque creare i grafici? [y/N]");
    choice <- readLines("stdin", 1);
    if (choice != "Y" && choice != "y") quit();
}

library(ggplot2);
require(gridSVG);


path <- "./latest_informaggio_csv/risultati/";
args <- commandArgs(trailingOnly=TRUE);
if (length(args)>0) path <- args[1];

filenames <- dir(path, pattern =".csv");
for(i in 1:length(filenames)){
    if (grepl("anagrafica-", filenames[i])) {
        fullpath <- paste(path, filenames[i], sep="");
        basename <- sub('\\.csv$', '', filenames[i]);
        file <- read.table(fullpath,header=FALSE, sep=",", col.names=c("Risposte" , "Utenti"), colClasses = c("character", "numeric"));
        # Pulisco la tabella
        file$Risposte <- as.character(file$Risposte);
        file$Risposte[file$Risposte==""] <- "NA";
        file$Risposte <- as.factor(file$Risposte);
        #Ordino la tabella in funzione della colonna degli utenti
        file <- file[order(file$Utenti),];
        # Scrivo i dati per debug
        print(basename)
        print(file);
        # Creo un barplot con legenda in ordine alfabetico
        #pie = ggplot(file, aes(x="", y=file$Utenti, fill=file$Risposte)) + geom_bar(stat="identity", width=1);
        # Creo un barplot seguendo l'ordine attuale della tabella ()
        pie = ggplot(file, aes(x="", y=file$Utenti, fill=factor(file$Risposte, levels = as.character(file$Risposte)))) + geom_bar(stat="identity", width=1);
        # Trasforma in torta (coordinate polari invece che cartesiane)
        pie = pie + coord_polar("y", start=0);
        # Percentuale o numero puro nelle etichette?
        #mylabels = paste0(round(file$Utenti*100/sum(file$Utenti)), "%");
        mylabels = file$Utenti;
        pie = pie + geom_text(aes(label = mylabels), position = position_stack(vjust = 0.5));
        # Abilita questa riga se vuoi specificare manualmente i colori
        #pie = pie + scale_fill_manual(values=c("#55DDE0", "#33658A", "#2F4858", "#F6AE2D", "#F26419", "#999999")) ;
        pie = pie + scale_fill_discrete(labels=paste0(file$Risposte, " (", file$Utenti, ")", sep=""));
        pie = pie + labs(x = NULL, y = NULL, fill = NULL, title = sub('-', ' ', basename));
        pie = pie + theme_classic() + theme(axis.line = element_blank(),
            axis.text = element_blank(),
            axis.ticks = element_blank(),
            plot.title = element_text(hjust = 0.5, color = "#666666"));
        #Esporto il grafico in un file SVG
        print(pie);
        grid.export(paste(path, "svg/", basename, ".svg", sep=""),addClasses=TRUE);
    }
    
    if (grepl("quiz-", filenames[i]) || grepl("punteggi-", filenames[i])) {
        fullpath <- paste(path, filenames[i], sep="");
        basename <- sub('\\.csv$', '', filenames[i]);
        file <- read.table(fullpath,header=FALSE, sep=",", col.names=c("Risposte" , "Utenti"), colClasses = c("numeric", "numeric"));
        # Ordino la tabella in base alla prima colonna (i punteggi calcolati con le risposte degli utenti)
        file <- file[order(file$Risposte),];
        file$Risposte <- as.factor(file$Risposte);
        # Scrivo i dati per debug
        print(basename)
        print(file);
        # Creo un istogramma
        histogram = ggplot(file, aes(x=file$Risposte, y=file$Utenti, fill=file$Risposte)) + geom_bar(stat="identity");
        # Percentuale o numero puro nelle etichette?
        #mylabels = paste0(round(file$Utenti*100/sum(file$Utenti)), "%");
        mylabels = file$Utenti;
        histogram = histogram + stat_count(aes(y=..count..,label=mylabels),geom="text",vjust=-1)
        histogram = histogram + labs(x = NULL, y = NULL, fill = NULL, title = sub('-', ' ', basename));
        histogram = histogram + theme_classic() + theme(axis.line = element_blank(),
            axis.text = element_blank(),
            axis.ticks = element_blank(),
            plot.title = element_text(hjust = 0.5, color = "#666666"));
        #Esporto il grafico in un file SVG
        print(histogram);
        grid.export(paste(path, "svg/", basename, ".svg", sep=""),addClasses=TRUE);
    }
    if (grepl("risposta-", filenames[i])) {
        fullpath <- paste(path, filenames[i], sep="");
        basename <- sub('\\.csv$', '', filenames[i]);
        file <- read.table(fullpath,header=FALSE, sep=",", col.names=c("Risposte" , "Utenti"), colClasses = c("character", "numeric"));
        # Ordino la tabella in base alla prima colonna (i punteggi calcolati con le risposte degli utenti)
        file <- file[order(file$Utenti),];
        file$Risposte <- as.factor(file$Risposte);
        # Scrivo i dati per debug
        print(basename)
        print(file);
        # Creo un istogramma
        histogram = ggplot(file, aes(x=file$Risposte, y=file$Utenti, fill=file$Risposte)) + geom_bar(stat="identity");
        # Percentuale o numero puro nelle etichette?
        #mylabels = paste0(round(file$Utenti*100/sum(file$Utenti)), "%");
        mylabels = file$Utenti;
        histogram = histogram + stat_count(aes(y=..count..,label=mylabels),geom="text",vjust=-1)
        histogram = histogram + labs(x = NULL, y = NULL, fill = NULL, title = sub('-', ' ', basename));
        histogram = histogram + theme_classic() + theme(axis.line = element_blank(),
            axis.text = element_blank(),
            axis.ticks = element_blank(),
            plot.title = element_text(hjust = 0.5, color = "#666666"));
        #Esporto il grafico in un file SVG
        print(histogram);
        grid.export(paste(path, "svg/", basename, ".svg", sep=""),addClasses=TRUE);
    }
} 
