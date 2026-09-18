import pandas as pd #Operação com tabelas
import os #Sistema operacional

#Mudança de diretório
os.chdir(r"D:\DataScience\AllSpeciesProteinAnnotated")

counter = 0

#Para cada arquivo que tabular no diretório, lê o arquivo e faz junção com base na coluna sseqid
for arch in os.listdir():
    if arch.endswith(".tabular"):
        if counter ==   0 :
            df_merged = pd.read_table(arch, sep="\t")
        else:
            df = pd.read_table(arch, sep="\t")
            df_merged = pd.merge(df_merged, df, on="sseqid", how="outer")
        counter += 1    

#susbtituir valores nulos por 0
df_merged.fillna(0, inplace=True)

#Criar um diretório para armazenar os resultados
os.makedirs(r".\\results", exist_ok=True)
os.chdir(r".\\results")

#exportar os dados das contagens juntas para um arquivo tabular
df_merged.to_csv("MergedCounts.tabular", index=False, sep="\t")

#Exportar os dados de cada contagem separadamente para arquivos tabulares
for column in df_merged.columns[1:]:
    df = df_merged[["sseqid", column]]
    df.to_csv(f"{column}_Counts.tabular", index=False, sep="\t")
