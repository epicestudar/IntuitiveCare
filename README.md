<br>
<br>
<br>
<p align="center">
   <img src="/img/logo/logo.png" alt="logo" width=250px>
</p>

<p align="center">
   <img src="https://img.shields.io/badge/Teste 1-CONCLUIDO-blue?style=for-the-badge" alt="TESTE 1" />
   <img src="https://img.shields.io/badge/Teste 2-CONCLUIDO-blue?style=for-the-badge" alt="TESTE 2" />
   <img src="https://img.shields.io/badge/Teste 3-CONCLUIDO-blue?style=for-the-badge" alt="TESTE 3" />
   <img src="https://img.shields.io/badge/Teste 4-CONCLUIDO-blue?style=for-the-badge" alt="TESTE 4" />
</p>
<hr>
<br>
<br><br><br>


<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=440&size=22&pause=1000&color=185DF7FF&center=false&vCenter=false&repeat=false&width=435&lines=Sumário 📰" alt="Typing SVG" /></a>

- [Teste 1](#teste1)
- [Teste 2](#teste2)
- [Teste 3](#teste3)
- [Teste 4](#teste4)
  
<br><br><br>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=440&size=22&pause=1000&color=185DF7FF&center=false&vCenter=false&repeat=false&width=435&lines=Introdução" alt="Typing SVG" /></a>
## Testes de Integração - Projeto IntuitiveCare

### Contexto Inicial
Este repositório descreve os quatro testes realizados para a avaliação técnica. Cada teste envolve uma etapa fundamental para o processamento, transformação e análise de dados relacionados às operadoras de planos de saúde.


<br><br><br>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=440&size=22&pause=1000&color=185DF7FF&center=false&vCenter=false&repeat=false&width=435&lines=Web Scraping" alt="Typing SVG" /></a>
## Teste 1

### Objetivo:
Automatizar a extração de arquivos PDF a partir do site da ANS (Agência Nacional de Saúde Suplementar), compactando-os em um único arquivo.

### Tarefas Executadas: 

   #### 1. Acesso ao site da ANS: 
   - URL: https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos


   #### 2. Download dos Anexos I e II:
   - Extração automatizada dos links dos anexos.
   - Download dos arquivos no formato PDF.


   #### 3. Compactação dos arquivos:
   - Os PDFs foram agrupados em um único arquivo ZIP/RAR para organização e otimização do armazenamento.


### Tecnologias utilizadas: 
- **Linguagem**: Python
- **Bibliotecas**: requests, BeautifulSoup, os, zipfile

<br><br><br>


<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=440&size=22&pause=1000&color=185DF7FF&center=false&vCenter=false&repeat=false&width=435&lines=Teste 2" alt="Typing SVG" /></a>
## 2. Teste de Transformação de Dados

### Objetivo:
Extrair dados tabulares do Anexo I baixado no Teste 1, estruturá-los e salvá-los em um arquivo CSV para posterior análise.

### Tarefas Executadas: 

   #### 1. Extração dos dados da tabela "Rol de Procedimentos e Eventos em Saúde"
   - Conversão de todas as páginas do PDF em texto estruturado.
   - Identificação e extração correta das colunas e linhas da tabela.


   #### 2. Armazenamento estruturado em CSV
   - Conversão dos dados extraídos para o formato tabular.
   - Salvamento em um arquivo .csv para facilitar a análise posterior.


   #### 3. Compactação do CSV
   - O arquivo CSV gerado foi compactado como "Teste_Vinicius.zip" para reduzir o tamanho e facilitar o compartilhamento.


   #### 4. Substituição de Abreviações
   - As colunas OD e AMB foram substituídas pelos seus nomes completos conforme a legenda no rodapé do PDF.


### Tecnologias utilizadas: 
- **Linguagem**: Python
- **Bibliotecas**: PyMuPDF, pandas, zipfile
<br><br><br>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=440&size=22&pause=1000&color=185DF7FF&center=false&vCenter=false&repeat=false&width=435&lines=Teste 3" alt="Typing SVG" /></a>
## 3. Teste de Banco de Dados

### Objetivo:
Baixar, estruturar e analisar dados financeiros das operadoras de planos de saúde utilizando um banco de dados SQL.

### Tarefas Executadas: 

   #### 1. Download dos arquivos necessários
   - **Demonstrações contábeis dos últimos 2 anos**: https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/
   - **Dados cadastrais das operadoras ativas**: https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/


   #### 2. Criação do Banco de Dados
   - Definição da estrutura das tabelas para armazenar os dados extraídos dos arquivos CSV.


   #### 3. Importação dos Dados
   - Inserção dos registros no banco de dados, garantindo a correta codificação dos caracteres.


   #### 4. Consultas Analíticas
   - **Consulta 1**: Identificação das 10 operadoras com maiores despesas em "**Eventos/Sinistros Conhecidos ou Avisados de Assistência à Saúde Médico-Hospitalar**" no último trimestre.
   - **Consulta 2**: Identificação das 10 operadoras com maiores despesas nessa mesma categoria no último ano.


### Tecnologias utilizadas: 
- **Banco de Dados**: PostgreSQL 10+
- **Linguagem**: SQL
- **Ferramenta**: pgAdmin
<br><br><br>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=440&size=22&pause=1000&color=185DF7FF&center=false&vCenter=false&repeat=false&width=435&lines=Teste 4" alt="Typing SVG" /></a>
## 4. Teste de API

### Objetivo:
Criar uma interface web utilizando Vue.js para buscar operadoras de saúde em um servidor Python, retornando os dados relevantes via API.


### Tarefas Executadas: 

   #### 1. Preparação dos Dados
   - Utilização do CSV baixado no Teste 3 para alimentar a API.


   #### 2. Criação da API com FastAPI
   - Implementação de um servidor backend em Python para fornecer um endpoint de busca textual na base de operadoras.


   #### 3. Desenvolvimento da Interface Web
   - Implementação de um formulário no Vue.js para permitir buscas interativas.
   - Exibição dos resultados em tempo real.


   #### 4. Testes com Postman
   - Criação de uma coleção no Postman para demonstrar o funcionamento da API e validar os retornos dos endpoints.


### Tecnologias utilizadas: 
- **Backend**: FastAPI (Python)
- **Frontend**: Vue.js
- **Ferramenta**: Postman, Axios
<br><br><br>
