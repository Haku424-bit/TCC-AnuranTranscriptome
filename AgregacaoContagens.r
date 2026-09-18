if (!require("BiocManager", quietly = TRUE)) install.packages("BiocManager")
if(!require("tximport"))BiocManager::install("tximport")

library("tximport") #Agregação de dados de leituras

#Mudança do diretório
setwd("D:\\DataScience\\Cma")

#Importação dos dados

spc_code = "Cma"
Transcript2Gene = read.table("TranscriptToGene.tabular", header = TRUE, sep = "\t")
salmon = "CountsToTxImport.tabular"

#tximport
data2 = tximport(files = salmon, type = "salmon", countsFromAbundance = "no", tx2gene=Transcript2Gene)

#Transformação em DataFrame
counts_df = as.data.frame(data2$counts)
colnames(counts_df) = spc_code #Alterar nome da coluna
counts_df$sseqid = rownames(counts_df) #Inserir IDs
rownames(counts_df) = NULL #Resetar index
counts_df = counts_df[, c(2, 1)] #Alterar ordem do dataframe

write.table(counts_df, "SummarizedGeneCounts.tabular", row.names = FALSE)
