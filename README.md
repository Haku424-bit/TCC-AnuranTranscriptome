Estes códigos foram utilizados para um trabalho de conclusão de curso, de nome:
# Transcriptômica comparada para entender adaptações a ambientes de altitude em anuros da América do Sul.
E está disponível através do link: https://repositorio.ufpe.br/handle/123456789/69270

A referência do trabalho em ABNT:
FELIX, L. A. S. Transcriptômica comparada para entender adaptações a ambientes de altitude em anuros da América do Sul. Trabalho de Conclusão de Curso (Bacharelado em Ciências Biológicas) - Universidade Federal de Pernambuco, Recife, 2026.

Os códigos se utilizam de Python (versão 3.13.13) e R (4.6.0).
Informações com relação a versão dos pacotes utilizados seguem no Trabalho de Conclusão de Curso.

### Os códigos seguem uma ordem para execução da análise:

## [MelhoresHits](./MelhoresHits.py)
Este código foi pensado para selecionar os hits com menor e-value do output do BlastP. Ao atribuir o melhor hit, é possível inferir uma homologia dos transcritos gerados pelo Trinity.
Isto permite obter algum significado biológico para as sequências estudadas (que até então são desconhecidas).

## [ExtrairDadosFastaToTable](./ExtrairDadosFastaToTable.py)
O arquivo fasta do *Mus musculus* já tem o nome do gene no identificador de cada sequência. Com isso, este código itera sobre cada sequência no arquivo fasta e coloca estas informações em uma tabela, que será usada posteriormente.

## [MergeSalmonAnotacaoGeneId](./MergeSalmonAnotacaoGeneId.py)
Este código visa a junção de 3 tabelas: Expressão do Salmon, Anotação do BlastP com melhores Hits e Tabela com a descrição e GeneId de cada ID de referência.
A partir disso é possível identificar cada transcrito, sua expressão, sua anotação e seu GeneId correspondente.
Como resultado, são obtidas duas tabelas para cada espécie: uma que relaciona dados de ID do TransDecoder com o ID com hit no uniprot e outra com contagens (número de leituras) para cada ID do TransDecoder (oriundas do Salmon).

## [AgregacaoContagens](./AgregacaoContagens.r)
Com as duas tabelas da etapa anterior foi possível agregar as contagens dos transcritos com base no melhor hit, através do Tximport.
A agregação das contagens de leituras para cada espécie resultará 4 tabelas (equivalente as 4 espécies de estudo).

## [AgregandoTabelasContagens](./AgregandoTabelasContagens.py)
Neste código as tabelas serão mescladas (merged) e depois separadas, com a finalidade de manter a mesma quantidade de linhas em todas as tabelas, transformando em 0 aqueles genes que não foram encontrados em outras espécies (valores nulos).

## [EntrezIdPathview](./EntrezIdPathview.r)
Para permitir match com os ids do Pathview, foi necessária a transformação do símbolo do gene para o id do Entrez através do banco de dados de anotação genômica completa para humanos org.Hs.eg.db versão 3.23.1. Com isso, é possível o mapeamento das vias do KEGG para a espécie *Homo sapiens*.

Para contato e esclarescimentos, deixo a seguir meu e-mail:
Leandroasfelix@gmail.com


