
#instalando bibliotecas
if (!require("BiocManager", quietly = TRUE)) install.packages("BiocManager")
if(!require("org.Hs.eg.db", quietly = TRUE))BiocManager::install("org.Hs.eg.db")
if(!require("pathview", quietly = TRUE))BiocManager::install("pathview")
if(!require("dplyr", quietly = TRUE))install.packages("dplyr")
if(!require("readxl", quietly = TRUE))install.packages("readxl")

#Carregando pacotes
library(org.Hs.eg.db) #Anotação dos dados em Homo sapiens
library("pathview") #Vias metabólicas do KEGG
library("dplyr") #Funcionalidades de transformação de dados
library("readxl") #ler arquivos excel

#Modificar diretório
setwd("D:\\DataScience\\Dge")

#Inserção de dados

#Output do EdgeR
LogFCdata = read.table("Galaxy139-[edgeR_High-Low].tabular", header = TRUE)
#Referência em tabela
refAnot = read_excel("D:\\DataScience\\UP000008143_8364.fasta\\AnotUP000008143_8364.xlsx")

#Junção de dados com anotação
LogFCdata = merge(LogFCdata, refAnot, all.x = TRUE, by.x = "GeneID", by.y = "sseqid")
LogFCdata = LogFCdata[,c("GeneId", "logFC")]

#Colocar a coluna GeneId em caixa alta (No banco de dados é em caixa alta)
LogFCdata$GeneId = toupper(LogFCdata$GeneId)

#Baixar dados de Homo sapiens com Enzimas que batem com o GeneId (Em Symbol)
Human_data = AnnotationDbi::select(org.Hs.eg.db, 
                    keys = LogFCdata$GeneId,
                    keytype = "SYMBOL",
                    columns = c("GENENAME", "SYMBOL", "ENTREZID", "ENZYME"))

#Juntar dados de Hsa com LogFC
merged_data = merge(LogFCdata, Human_data, all.x = T, by.x = "GeneId", by.y = "SYMBOL") 

#Transformações dos dados finais
merged_data$ENTREZID = as.integer(merged_data$ENTREZID)
gene_data = merged_data$logFC
names(gene_data) = merged_data$ENTREZID

#diretório de exportação
setwd("D:\\DataScience\\Dge\\NewResults")

#pathview propriamente dito, o pathway.id é trocado para obter outras vias
pathview(gene_data, pathway.id = "00010", species = "hsa")
