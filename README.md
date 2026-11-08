# Log Analyzer

Projeto de estudos em Python para praticar conceitos de programação por meio da leitura e análise de arquivos de log.

## Objetivo

Explorar e aplicar conceitos como:
- variáveis e tipos de dados
- estruturas de controle
- funções e módulos
- listas e manipulação de texto
- leitura e escrita de arquivos
- organização de código
- lógica de análise e filtragem de dados

## Funcionalidades

- selecionar um arquivo de log disponível na pasta `logs/`
- exibir o conteúdo completo do log
- exibir mensagens de erro
- filtrar mensagens por categoria: `INFO`, `WARNING` ou `ERROR`
- pesquisar um texto nas mensagens do log
- gerar um relatório com a quantidade de ocorrências por categoria

O relatório é salvo em `reports/report.txt`.

## Estrutura

```text
log_analyzer/
├── lib/
│   ├── iterface.py
│   ├── logs.py
│   └── shows.py
├── logs/       # Arquivos de log usados na análise
├── reports/    # Relatórios gerados pelo programa
└── main.py     # Ponto de entrada
```

## Como executar

1. Tenha o Python 3 instalado.
2. No terminal, acesse a pasta do projeto.
3. Execute:

```bash
python main.py
```

O programa apresentará os arquivos `.log` disponíveis e, após a seleção, abrirá um menu interativo. Não são necessárias dependências externas.

## Observação

Este repositório foi criado como espaço de estudo e prática. A ideia é aprender fazendo, aplicando conceitos de Python em um projeto simples de análise de logs.