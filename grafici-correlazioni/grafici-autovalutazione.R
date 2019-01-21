#!/usr/bin/Rscript
library(ggplot2);
require(gridSVG);
library(reshape2);

imported <- read.csv (file="./punteggi_per_autovalutazione.csv",  na.strings = "NA", nrows = -1, skip = 0, check.names = TRUE, strip.white = FALSE, blank.lines.skip = TRUE);
my.csv.data <- imported;
my.csv.melted <- melt(my.csv.data, id="X0");
grafico1 = ggplot(my.csv.melted, aes(x=variable, y=value, fill=factor(X0))) + geom_bar(stat="identity", width=1);
grafico1 = grafico1 + scale_fill_discrete();
grafico1 = grafico1 + labs(x = NULL, y = NULL, fill = NULL);
print(grafico1);
grid.export("./punteggi_per_autovalutazione1.svg",addClasses=TRUE);

my.csv.data2 <- my.csv.data
my.csv.data2$X0 <- my.csv.data$X0
my.csv.data2$insufficiente <- (my.csv.data$insufficiente*100)/sum(my.csv.data$insufficiente);
my.csv.data2$sufficiente <- (my.csv.data$sufficiente*100)/sum(my.csv.data$sufficiente);
my.csv.data2$scarsa <- (my.csv.data$scarsa*100)/sum(my.csv.data$scarsa);
my.csv.data2$buona <- (my.csv.data$buona*100)/sum(my.csv.data$buona);
my.csv.data2$ottima <- (my.csv.data$ottima*100)/sum(my.csv.data$ottima);

my.csv.melted2 <- melt(my.csv.data2, id="X0");
grafico2 = ggplot(my.csv.melted2, aes(x=variable, y=value, fill=factor(X0))) + geom_bar(stat="identity", width=1);
grafico2 = grafico2 + scale_fill_discrete();
grafico2 = grafico2 + labs(x = NULL, y = NULL, fill = NULL);
grafico2 = grafico2 + theme_classic() + theme(axis.line = element_blank(),
            axis.text.y = element_blank(),
            axis.text.x = element_text(angle = 270, hjust = 1),
            axis.ticks = element_blank(),
            plot.title = element_text(hjust = 0.5, color = "#666666"));
#Ribalto il grafico e imposto il rapporto altezza/larghezza
grafico2 = grafico2 + coord_flip();
grafico2 = grafico2 + coord_fixed(ratio = 0.1);
#Imposto il numero delle colonne in cui viene divisa la legenda
grafico2 = grafico2 + guides(fill=guide_legend(ncol=8))
print(grafico2);
grid.export("./punteggi_per_autovalutazione2.svg",addClasses=TRUE);
