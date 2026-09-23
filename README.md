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

Nesta etapa, o documento Pdf é lido e o seu conteúdo textual é extraído.

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

### Embeddings

Embeddings são representações numéricas, geralmente organizadas em vetores, de informações como textos, imagens ou outros tipos de dados. Essas representações permitem que sistemas de Inteligência Artificial comparem informações com base em características semânticas, sendo utilizadas em aplicações como busca semântica, sistemas de recomendação, chatbots e recuperação de informações.

#### Por que o RAG precisa de embeddings?

Em um sistema RAG, os embeddings permitem representar os conteúdos dos documentos em um espaço vetorial. Isso possibilita realizar cálculos de similaridade entre diferentes conteúdos e, posteriormente, recuperar informações semanticamente relevantes para serem utilizadas como contexto pelo modelo de IA.

#### Modelo utilizado

Para este projeto, foi escolhido o modelo:

`intfloat/multilingual-e5-base`

A escolha foi baseada nas necessidades do projeto, principalmente pelo suporte multilíngue e pela capacidade de gerar embeddings com **768 dimensões**. Como o corpus utilizado contém informações em português, o suporte multilíngue é importante para a representação semântica dos conteúdos.

#### Implementação

A implementação foi dividida em responsabilidades distintas.

Primeiro, foi criada uma classe responsável por inicializar e manter o modelo de embeddings. Dessa forma, o modelo é carregado uma vez e pode ser utilizado para processar vários chunks.

Em seguida, foi criada uma função responsável por gerar o embedding de um chunk. Como cada chunk possui diferentes informações, o processo utiliza apenas o conteúdo textual do chunk para gerar sua representação vetorial.

Para realizar essa transformação, foi utilizado o método `encode_document()`, disponibilizado pela biblioteca `sentence-transformers`, através do modelo `SentenceTransformer`.

O processo pode ser representado da seguinte forma:

```text
Chunk
  │
  ├── content ────────► encode_document()
  │                           │
  │                           ▼
  │                    Embedding
  │                           │
  │                           ▼
  │                 vetor de 768 dimensões
  │
  └── metadata ─────────► preservado
```

Depois da geração do embedding, o vetor foi integrado ao próprio chunk. Dessa forma, cada chunk mantém o seu conteúdo, os seus metadados e o embedding correspondente.

A estrutura resultante é aproximadamente:

```text
Chunk
├── content
├── metadata
│   ├── source
│   └── page
└── embedding
    └── 768 dimensões
```

#### Validação

Após a implementação, foram processados **885 chunks**, correspondentes aos IDs de `0` a `884`.

A validação confirmou que os chunks processados receberam embeddings e que cada embedding possui **768 elementos**, conforme a dimensão produzida pelo modelo `intfloat/multilingual-e5-base`.

```text
Chunk 0   → 768 dimensões
Chunk 1   → 768 dimensões
Chunk 2   → 768 dimensões
...
Chunk 883 → 768 dimensões
Chunk 884 → 768 dimensões
```

Com isso, cada conteúdo do documento possui agora uma representação vetorial que poderá ser utilizada nas próximas etapas do sistema RAG.


### Indexação

De forma simples, **indexar** significa organizar dados e criar uma estrutura que facilite a sua localização e recuperação posteriormente.

#### Indexação vetorial

A **indexação vetorial** é o processo de organizar vetores, como embeddings, utilizando uma estrutura de dados adequada para tornar mais eficiente a busca por vetores semelhantes.

É importante distinguir alguns conceitos:

* **Embedding** → é a representação vetorial de um determinado conteúdo.
* **Indexação vetorial** → é o processo de organizar esses vetores para facilitar a busca.
* **Índice vetorial** → é a estrutura resultante utilizada para organizar e consultar os vetores.
* **Busca por similaridade** → é a operação que compara um vetor de consulta com os vetores armazenados para encontrar os mais semelhantes.

Portanto, **indexação vetorial não é o vetor em si nem é a busca**. É o processo que prepara e organiza os vetores para que a busca por similaridade possa ser realizada de forma eficiente.

### Armazenamento dos embeddings

Em uma aplicação RAG, os embeddings podem ser armazenados em um **banco de dados vetorial**, como o Chroma.

Além do próprio embedding, é necessário manter informações que permitam relacioná-lo ao conteúdo original. No nosso projeto, cada embedding está associado ao **ID do chunk** que originou esse embedding.

O fluxo pode ser representado da seguinte forma:

```text
Chunk
  ↓
Embedding
  ↓
Embedding + Chunk ID
  ↓
Índice vetorial
  ↓
Busca por similaridade
```

### Estrutura criada no projeto

Para compreender a lógica da indexação vetorial antes de utilizar uma solução especializada, foi criada uma classe `EmbeddingIndex`.

Essa classe representa uma estrutura responsável por manter os embeddings e os IDs dos chunks correspondentes.

Estrutura simplificada:

```text
EmbeddingIndex
│
├── _embeddings
│      ├── embedding 0
│      ├── embedding 1
│      ├── embedding 2
│      └── ...
│
└── _chunk_ids
       ├── chunk ID 0
       ├── chunk ID 1
       ├── chunk ID 2
       └── ...
```

Existe uma correspondência entre as duas listas:

```text
_embeddings[0] ↔ _chunk_ids[0]
_embeddings[1] ↔ _chunk_ids[1]
_embeddings[2] ↔ _chunk_ids[2]
```

Dessa forma, quando um embedding é identificado durante a busca, podemos saber a qual chunk ele pertence através do seu ID correspondente.

### Métodos

A classe possui dois métodos principais:

#### `add`

Responsável por adicionar um novo embedding juntamente com o ID do chunk correspondente.

```text
embedding + chunk_id
        ↓
     add()
        ↓
armazenamento no índice
```

#### `search`

Responsável por realizar a busca entre o embedding da consulta e os embeddings armazenados.

O objetivo é:

```text
Query
  ↓
Query Embedding
  ↓
search()
  ↓
comparação com embeddings armazenados
  ↓
métrica de similaridade/distância
  ↓
chunks mais semelhantes
```

A implementação da comparação entre os vetores será desenvolvida posteriormente.

### Próximo passo

O próximo conceito a estudar é a **comparação entre vetores**, começando pela **similaridade de cosseno** e posteriormente analisando outras métricas, como:

* Distância Euclidiana;
* Produto escalar (Dot Product);
* Similaridade de Cosseno.

O objetivo é compreender matematicamente como determinar se dois embeddings são semelhantes antes de implementar essa lógica no método `search()`.

