import pandas as pd #Análise de dados tabulares
import os #Operações com o sistema operacional

#Input do arquivo

os.chdir(r"D:\DataScience\Cma")
arch = r".\Galaxy64-[blastp Cma TransDecoder on dataset 7_ Results (PEP_FASTA) vs _'XenTropOneProteinSeqPerGeneUniProtUP000008143_8364.fasta'_].tabular"

#Inserção e tratamento dos dados de anotação

#Dados de anotação BlastX com 12 colunas comuns + stitle, staxids e sscinames
df_anot = pd.read_table(arch, sep="\t", names=["qseqid", "sseqid", "pident", "length", "mismatch", "gapopen", "qstart", "qend", "sstart", "send", "evalue", "bitscore", "stitle",	"staxids",	"sscinames"])
#Garantir que o menor e value esteja aparecendo primeiro 
df_sorted = df_anot.sort_values(['qseqid', 'evalue'], ascending = True)

#Manter somente o top Blast Hit (anotação)
df_sorted.drop_duplicates(subset=["qseqid"], keep="first", inplace=True) 

#Remoção de caracteres desnecessários presentes nos códigos do banco de dados
for index, row in df_sorted.iterrows(): 
    valor = row["sseqid"]
    df_sorted.loc[index, "sseqid"] = valor[valor.find("|")+1:valor.rfind("|")]

#Número de ids query anotados
queryNum = df_sorted['qseqid'].nunique()
print(f"O número de queries anotadas foram {queryNum}")

#Número de ids do banco de dados encontrados
subjectNum = df_sorted['sseqid'].nunique()
print(f"O número de ids do banco de dados com match foram {subjectNum}")

df_sorted.to_excel("BlastpUniqueAnnotated.xlsx", index = False)

print("Finalizado")
