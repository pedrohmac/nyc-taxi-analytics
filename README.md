# nyc-taxi-analytics

## overview

Esse repositório contém um processo de ETL e análise de um conjunto de dados de viagens de taxi de New York;
O objetivo do projeto é exercitar habilidades em SQL, Python, linux e DataScience/Engineering.
Para alcançar esse objetivo foram criados a infraestrutura (infra-as-code) e também pipelines de dados que alimentam um banco PostgreSQL, tudo isso rodando com docker-compose.


## Para rodar o programa, devem ser executadas as seguintes etapas:

1. Baixar a pasta 'datasets' (https://drive.google.com/drive/folders/1vLqR3Dj_munm98huyDZH_fblGtY912Fu?usp=sharing) e colocá-la dentro do diretório worker, ela contém os datasets a serem usados na análise.

2. Inserir em um terminal (preferencialmente Ubuntu) dentro do diretório nyc-taxi-analytics o comando: "docker-compose up --build"

3. O primeiro quesito mínimo retorna o valor no terminal, os demais são apresentados em forma de gráficos no diretório "/nyc-taxi-analytics"

4. Depois de rodar o programa, as imagens para o arquivo "analise.ipynb" estarão disponíveis.