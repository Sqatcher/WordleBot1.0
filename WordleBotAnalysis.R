setwd("D:/WordleBot/WordleBot1.0/WordleBot1.0")
data <- read.csv("results.txt", sep=':', header = FALSE)
colnames(data) <- c("case", "word", "count")
head(data)
summary(data$count)

library(ggplot2)
library(plotly)
library(dplyr)

WORD_COUNT <- length(unique(data$word))

# General analysis
E <- list()
uniqWords <- unique(data$word)
for (j in 1:WORD_COUNT){
  E[[j]] <- 0
  wordToAnalyze <- uniqWords[j]
  word_data <- data %>%
    group_by(word) %>%
    filter(word == wordToAnalyze)
  for (i in 1:length(word_data$case)){
    pX <- word_data[i,]$count / WORD_COUNT
    if (pX != 0){
      E[[j]] = E[[j]] - (pX * log(pX, base=2))
    }
  }
  print(paste(round(j/WORD_COUNT, 4)*100, "%", sep=""))
}
Emin = min(unlist(E))
print(Emin)
wordEmin = unique(data$word)[which.min(E)]
print(wordEmin)
wordEmax = unique(data$word)[which.max(E)]
print(wordEmax)
max(unlist(E))

# One word
wordToPlot <- wordEmin #"esses"
wordToPlot <- wordEmax #"esses"
wordToPlot <- "crane"
gr_data <- data %>%
  group_by(word) %>%
  filter(word == wordToPlot)

gr_data <- gr_data[order(gr_data$count, decreasing = TRUE),]
gr_data["no"] <- seq(1:length(gr_data$case))

EBits = 0
for (i in 1:length(gr_data$case)){
  pX <- gr_data[i,]$count / WORD_COUNT
  if (pX != 0){
    EBits = EBits - (pX * log(pX, base=2))
  }
}
EBits <- round(EBits, digits = 2)

wordCountsPlot <- ggplot(data=gr_data, aes(x=no, y=count, text=case))+
  geom_bar(stat="identity")+
  annotate("text", x = 175, y = 3/4*max(gr_data$count), label = paste("E(x) =", EBits, sep = ' '), size=10)+
  theme_void()

wordEntropyPlot <- ggplot(data=gr_data, aes(x=case, y=-(count/WORD_COUNT)*log((count/WORD_COUNT), 2)))+
  geom_bar(stat="identity")+
  annotate("text", x = 175, y = 0.5, label = paste("E(x) =", EBits, sep = ' '), size=10)+
  theme_void()

ggplotly(wordCountsPlot, tooltip = c("count", "text"))
ggplotly(wordEntropyPlot)