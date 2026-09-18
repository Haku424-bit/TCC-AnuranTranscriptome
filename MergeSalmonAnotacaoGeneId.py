from Bio import SeqIO #Operações com dados de sequências biológicas
import pandas as pd #análise de dados
import os #Operações com o sistema operacional

#Mudança do diretório para o local onde está o arquivo fasta
os.chdir(r"D:\DataScience\UP000008143_8364.fasta")

#Listas para armazenar os dados extraídos do arquivo fasta
ids = []
GeneId = []
desc = []

#Iterar sobre cada sequência
for seq in SeqIO.parse("UP000008143_8364.fasta", "fasta"):
    name = seq.name
    description = seq.description

    #extraindo id
    ids.append(name[(name.find("|"))+1:name.rfind("|")]) 
   
    #extraindo gene id
    descGenePos = (description.find("GN="))
    GeneDesc = description[descGenePos:]
    GeneId.append(GeneDesc[3:GeneDesc.find(" ")])

    #extraindo descrição
    desc.append(description[(description.find(" "))+1:(description.find("OS=")-1)])

#Criação do Data Frame
df_final = pd.DataFrame({"sseqid": ids, "GeneId": GeneId, "stitle": desc})

#exportando dados para um arquivo excel
df_final.to_excel("AnotUP000008143_8364.xlsx", index=False)
print("Finalizado")
