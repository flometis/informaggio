#!/usr/bin/Rscript
library(reshape2);
imported <- read.csv (file="/home/flo/Progetti/informaggio/grafici-correlazioni/punteggi_per_autovalutazione.csv",  na.strings = "NA", nrows = -1, skip = 0, check.names = TRUE, strip.white = FALSE, blank.lines.skip = TRUE);
my.csv.data <- imported;
my.csv.melted <- melt(my.csv.data, id="X0");
grafico1 = ggplot(my.csv.melted, aes(x=variable, y=value, fill=factor(X0))) + geom_bar(stat="identity", width=1);
grafico1 = grafico1 + scale_fill_discrete();
grafico1 = grafico1 + labs(x = NULL, y = NULL, fill = NULL);
print(grafico1);
grid.export("/home/flo/Progetti/informaggio/punteggi_per_autovalutazione1.svg",addClasses=TRUE);

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
print(grafico2);
grid.export("/home/flo/Progetti/informaggio/grafici-correlazioni/punteggi_per_autovalutazione2.svg",addClasses=TRUE);
