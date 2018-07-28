# PyCalc para testes de cobertura ![7]

## Configuração

Ambiente utilizado:

- [Python 3.6][1]
- [coverage.py][2]
- [SonarCloud][3]
- pycalc

### Instalar o Python 3.6

Veja a documentação no [link][4]

### Instalação do `coverage.py`

Instale o `coverage.py` a partir do [PyPi][5]

`python -m pip install coverage`

### Instalação do sonar-scanner

Seguir as instruções em [link][6]

### Clonar o projeto

`git clone https://github.com/fabioqcorreia/pycalc.git`

### Cadastrar no sonarcloud.io e criar um arquivo sonar-project.properties

Preferencialmente conecte sua conta do SonarCloud com o GitHub

Exemplo:

```
sonar.projectKey=pycalc
sonar.organization=<sonar_github_organization>
sonar.sources=sub,sum,utils
sonar.host.url=https://sonarcloud.io 
sonar.projectVersion=1.0
sonar.login=<project_auth_key>
sonar.exclusions=venv/,__pycache__/,.idea/,tests/
sonar.python.coverage.reportPath=coverage.xml
```

## Gerando arquivo de cobertura

Após a configuração do ambiente, precisamos rodar os testes para gerar um arquivo que o `coverage.py` verificará.

`python -m coverage run --branch --source=sub,sum,utils -m tests.main_tests`

> --branch para verificar a cobertura por linhas. \
> --source para mapear o código fonte. \
> -m para executar um módulo de testes.

Após esta execução será criado um arquivo `.coverage`, para que o SonarCloud entenda o conteúdo do mesmo, iremos gerar um arquivo `.xml`.

`python -m coverage xml`

Será possível verificar que um arquivo chamado `coverage.xml` foi gerado na pasta raiz.

## Enviando dados para SonarCloud

Agora que temos o arquivo `coverage.xml` criado, podemos utilizá-lo para enviar à SonarCloud executando o comando abaixo na pasta raiz do projeto:

`sonar-scanner`

> Nota: Para esta etapa, foi configurado o sonar-scanner para a variável de ambiente, assim podemos executá-la sem precisar referenciar o caminho todo da pasta.

Após a execução concluída, poderá verificar no seu dashboard do SonarCloud.

[1]: https://www.python.org/downloads/release/python-366/
[2]: https://coverage.readthedocs.io/
[3]: https://sonarcloud.io/
[4]: https://docs.python.org/3.6/using/index.html
[5]: https://pypi.org/project/coverage/
[6]: https://docs.sonarqube.org/display/SCAN/Analyzing+with+SonarQube+Scanner
[7]: https://sonarcloud.io/api/project_badges/measure?project=pycalc&metric=alert_status