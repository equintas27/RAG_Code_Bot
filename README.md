# RAG_Code_Bot

O RAG_Code_Bot é um chatbot, usando o Retrieval Augmented Generation(RAG) em Python.
Um chatbot é um programa de computador criado para simular conversas humanas por texto ou voz.

## RAG (Retrieval Augmented Generation)

Retrieval Augmented Generation (Geração Aumentada por Recuperação) ou simplesmente, RAG é uma técnica de Inteligência Artificial, que consiste na busca de informações em fontes  de dados externas (documentos, bancos de dados e outros), para permitir que um modelo responda com base nessas informações, ajudando a reduzir o risco de alucinações de um modelo de Inteligência artificial.

## Etapas de Desenvolvimento

### Data Ingestion e Chunking 

 **Objectivo**

Esta etapa é responsável por preparar os documentos que serão utilizados pelo sistema RAG.

O processo realizado até aqui é:

```text
Documento PDF
     ↓
Extração do texto
     ↓
Preservação de metadata
     ↓
Chunking
     ↓
Chunks preparados para embeddings
```

O documento utilizado para validação é o **Relatório Anual e Contas 2025 da Sonangol**.

#### Data Ingestion

Data Ingestion é o processo de entrada e preparação dos documentos para o sistema.

Nesta etapa, o documento Pdf é lido e o seu contéudo textual é extraído.

Além do texto, são preservadas informações importantes sobre a origem do conteúdo, como:

* Identificador do chunk;
* Documento de origem;
* Número da página.

Essas informações são armazenadas como **metadata**.

Exemplo conceptual:

```python
{
    "content": "Conteúdo do chunk...",
    "metadata": {
         "id": 0,
        "source": "Relatorio-2025.pdf",
        "page": 86
    }
}
```

A metadata não representa o conteúdo semântico do texto. Ela serve para identificar e contextualizar a origem de cada chunk.

---

#### Extração do PDF

A extração do conteúdo do PDF é realizada utilizando a biblioteca **PyMuPDF**.

Conceitualmente:

```text
PDF
 │
 ├── Página 1 → texto
 ├── Página 2 → texto
 ├── Página 3 → texto
 │      ...
 └── Página N → texto
```

Processar as páginas individualmente permite preservar a relação entre o contéudo e a página de origem.

Essa informação será útil posteriormente para identificar a fonte dos conteúdos recuperados pelo sistema RAG.

---

#### Chunking 

Depois da extração, o texto é dividido em partes menores chamadas **chunks**.

O objectivo é evitar trabalhar com um documento inteiro como uma única unidade de informação.

O processo é:

O processo é:

```text
Texto da página
      ↓
Text Splitter
      ↓
Chunk 1
Chunk 2
Chunk 3
...
```

Cada chunck possui um tamanho limitado.

No projecto foi utilizado:

```text
chunk_size = 1000
overlap = 200
```

Isso significa que o tamanho máximo utilizado como referência para um chunk é de aproximadamento 1000 caracteres, enquanto aproxidamente 200 caracteres do contéudo anterior são reutilizados no chunk seguintes sempre que possível.

---

#### Overlap

O **overlap** é a quantidade de conteúdo compartilhada entre duas chunks consecutivos.

Exemplo:

```text
Chunk 1
──────────────────────────────
A empresa apresentou resultados
positivos durante o exercício de
2025 e registou crescimento...
                    ↑
                    │
                 overlap
                    │
                    ↓
Chunk 2
──────────────────────────────
crescimento... A receita também
apresentou uma evolução positiva...
```

O objetivo do overlap é evitar que uma informação seja dividida de forma que o seu contexto fique perdido entre dois chunks.

Sem overlap:

```text
Chunk 1 → informação A
Chunk 2 → continuação da informação A
```

Com overlap:

```text
Chunk 1 → informação A + contexto
                    ↘
                     Chunk 2
                    ↗
             contexto repetido
```

---

#### Validação do chunking 

Depois da implementação do `text_splitter`, foram realizados testes para verificar se o processo estava funcionando corretamente.

Foram verificadas:

* quantidade de chunks;
* tamanho mínimo;
* tamanho máximo;
* tamanho médio;
* existência de overlap;
* tamanho dos overlaps;
* reconstrução do texto original.

Resultado obtido com o documento utilizado:

```text
Total de chunks: 781

Menor chunk: 790 caracteres
Maior chunk: 999 caracteres
Média: aproximadamente 960 caracteres

Menor overlap: 32 caracteres
Maior overlap: 199 caracteres
Média: aproximadamente 194 caracteres
```

Também foi realizada uma reconstrução do texto a partir dos chunks, removendo os conteúdos repetidos pelo overlap.

Resultado:

```text
Reconstrução: True
```

Isso confirmou que, para o documento utilizado, o processo de chunking preservou o conteúdo original.

---

#### Overlaps menores

Durante a validação foram encontrados alguns overlaps menores que os 200 caracteres configurados.

Foram identificadas 7 transições com overlap inferior a 150 caracteres.

Esses casos estavam associados principalmente a características da própria extração do PDF, como:

* cabeçalhos;
* rodapés;
* quebras de página;
* tabelas;
* alterações na estrutura do texto extraído.

Portanto, a existência desses casos não foi interpretada isoladamente como uma falha do algoritmo de chunking.

A maior parte dos overlaps permaneceu próxima do valor configurado.

--- 

#### Funções auxiliares de teste

Durante o desenvolvimento foram criadas funções auxiliares para validar o comportamento do chunking, incluindo funções para:

* detectar overlap entre chunks;
* reconstruir o texto original.

Essas funções foram utilizadas durante a fase de validação e posteriormente separadas do código principal.

A lógica de produção deve permanecer separada da lógica utilizada exclusivamente para testes.

Estrutura conceptual:

```text
src/
    código da aplicação

tests/
    código de validação e testes
```

---