
# Projeto de **pipeline** de dados

O projeto tem como principal objetivo combinar os arquivos da empresa **A** com os da empresa **B** e disponibilizar esse arquivo unido para a equipe de análise. Mas não apenas isso, é necessário fornecer uma solução que seja reproduzível para os meses seguintes.

Para tanto, é criado uma **pipeline** de dados que unam esses dados. As etapas da pipilene consiste em extrair, transformar e carregar os dados, como ilustrado na imagem abaixo.

<div align="center">
  <img src="figs/etapas-pipeline.png" alt="epatas da pipeline" width="300" height="200">
  <br>
  <em>Figura 1: Etapas do pipeline de dados</em>
</div>

## Tecnologias e dependências utilizadas
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

As bibliotecas utilizadas:
- json
- csv


## Estrutura do Projeto 

É ideializado que a construção do pipeline seja reutilizável em outros porcessos da empresa. Assim, a estrutura de trabalho é definida em: 
1. [jupter Notebook](/src/pipelinedata/testes.ipynb) para realização de testes e manipulações de dados
2. Estrutura de pastas que obedece às diretrizes de um bom desenvolvimento e engenharia de software
````
| pipeline-data/
|--docs/
|--src/: Contém todo o código fonte do projeto.
|-------data/: Contém as bases de dados
|------------raw/
|------------ready-processed/
|-----pipelinedata/: Contém os códigos fontes


````
3. Criação de um ambiente virtual Python
4. Utilizar os processo de ETL

## Referências 
1. Orientador: [Igor Nascimento Alves](https://cursos.alura.com.br/user/igor-nascimento-flipe)
2. Curso: [Alura - Pipeline de dados](https://cursos.alura.com.br/course/pipeline-dados-combinando-python-orientacao-objeto)