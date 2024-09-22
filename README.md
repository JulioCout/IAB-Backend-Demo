

<a  name="readme-top"></a>

  

# REST API IAB

  

<p  align="center">

<img  src="http://img.shields.io/static/v1?label=Python&message=3.12&color=red&style=for-the-badge&logo=Python"/>

<img  src="https://img.shields.io/static/v1?label=Django&message=framework&color=blue&style=for-the-badge&logo=Django"/>

<img  src="https://img.shields.io/static/v1?label=SQL Server&message=database&color=blue&style=for-the-badge&logo=SQLServer"/>

<img  src="http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge"/>

<img  src="http://img.shields.io/static/v1?label=TESTES&message=100%&color=GREEN&style=for-the-badge"/>

<img  src="http://img.shields.io/static/v1?label=License&message=EULA&color=green&style=for-the-badge"/>

  





| :sparkles: Nome | **REST-API IAB**

| :label: Tecnologias | Django, SQL Server, JWT

| :rocket: URL | https://webapp-financeira.herokuapp.com/



  

![rest-api-imagem](https://github.com/thomazcm/rest-api-financeira/blob/master/github/rest-api.png#vitrinedev)

  

### Tópicos

  

:small_blue_diamond: [Descrição do projeto](#descrição-do-projeto)

  

:small_blue_diamond: [Acesso](#acesso)

  

:small_blue_diamond: [Funcionalidades](#funcionalidades)

  

:small_blue_diamond: [Pré-Requisitos e como Rodar o Servidor](#pré-requisitos)

  

:small_blue_diamond: [Tecnologias](#tecnologias)

  

:small_blue_diamond: [Autor](#autor)

  
  

## Descrição do projeto

  

<p  align="justify">

API RESTful desenvolvida sob medida para servir como camada de back-end do sistema de gerenciamento de dados do Instituto dos Advogados Brasileiros.<br/>

API desenvolvida em Python com o framework Django, utiliza um sistema de autenticação stateless e banco de dados SQL Server.

</p>

  

## Acesso

A demonstração das funcionalidades da API podem ser acessadas [através do aplicativo web](https://iab-backend-demo-iwdw.vercel.app/) que utiliza os endpoints para seu funcionamento.

Caso queira rodar o servidor localmente [siga os passos listados aqui](#pré-requisitos).

## Funcionalidades

:heavy_check_mark: Cadastro de novos membros do instituto.

  

:heavy_check_mark: Consulta, edição e exclusão de membros já cadastrados

  

:heavy_check_mark: Cadastro de novas despesas e receitas

  

:heavy_check_mark: Consulta, edição e exclusão de despesas e receitas já cadastradas

  

:heavy_check_mark: Consulta de um resumo das despesas, receitas e saldo de cada mês

 

:heavy_check_mark: Cadastro de novas indicações feitas pelos membros



:heavy_check_mark: Consulta, edição e exclusão de indicações já cadastradas



:heavy_check_mark: Cadastro de novos processos



:heavy_check_mark: Consulta, edição e exclusão de processos já cadastrados
  

### API REST

Os endpoints da API REST estão descritos abaixo.

#### Membros

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /membros &nbsp;&nbsp;→&nbsp;&nbsp; Listar membros<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`POST` /membros &nbsp;&nbsp;→ &nbsp;&nbsp;Criar membro<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`GET` /membros/id &nbsp;&nbsp;→ &nbsp;&nbsp;Consultar um membro<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`PATCH` /membros/id &nbsp;&nbsp;→ &nbsp;&nbsp;Editar um membro<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`DELETE` /membros/id &nbsp;&nbsp;→ &nbsp;&nbsp;Apagar um membro<br/>


#### Indicações

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /indicacoes &nbsp;&nbsp;→ &nbsp;&nbsp;Listar indicações<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`POST` /indicacoes &nbsp;&nbsp;→ &nbsp;&nbsp;Criar indicação<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`GET` /indicacoes/id &nbsp;&nbsp;→ &nbsp;&nbsp;Consultar uma indicação<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`PATCH` /indicacoes/id &nbsp;&nbsp;→ &nbsp;&nbsp;Editar uma indicação<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`DELETE` /indicacoes/id &nbsp;&nbsp;→ &nbsp;&nbsp;Apagar uma indicação<br/>

#### Processos

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /processos &nbsp;&nbsp;→ &nbsp;&nbsp;Listar processos<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`POST` /processos &nbsp;&nbsp;→ &nbsp;&nbsp;Criar processo<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`GET` /processos/id &nbsp;&nbsp;→ &nbsp;&nbsp;Consultar um processo<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`PATCH` /processos/id &nbsp;&nbsp;→ &nbsp;&nbsp;Editar um processo<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`DELETE` /processos/id &nbsp;&nbsp;→ &nbsp;&nbsp;Apagar um processo<br/>

#### Receitas

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /receitas &nbsp;&nbsp;→ &nbsp;&nbsp;Listar receitas<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`POST` /receitas &nbsp;&nbsp;→ &nbsp;&nbsp;Criar receita<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`GET` /receitas/id &nbsp;&nbsp;→ &nbsp;&nbsp;Consultar uma receita<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`PATCH` /receitas/id &nbsp;&nbsp;→ &nbsp;&nbsp;Editar uma receita<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`DELETE` /receitas/id &nbsp;&nbsp;→ &nbsp;&nbsp;Apagar uma receita<br/>

#### Despesas despesas

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /despesas &nbsp;&nbsp;→ &nbsp;&nbsp;Listar despesas<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`POST` /despesas &nbsp;&nbsp;→ &nbsp;&nbsp;Criar despesa<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`GET` /despesas/id &nbsp;&nbsp;→ &nbsp;&nbsp;Consultar uma despesa<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`PATCH` /despesas/id &nbsp;&nbsp;→ &nbsp;&nbsp;Editar uma despesa<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`DELETE` /despesas/id &nbsp;&nbsp;→ &nbsp;&nbsp;Apagar uma despesa<br/>
  

<p  align="right">(<a  href="#readme-top">voltar para o início</a>)</p>

## Pré-Requisitos

Para rodar o servidor localmente você precisa ter instalado as seguintes ferramentas: [Python](https://www.python.org/downloads/) e [Git](https://git-scm.com/).

### Como rodar a aplicação

1. Clone este repositório:

```

git clone https://github.com/JulioCout/IAB-Backend-Demo

```
  

2. Crie um ambiente virtual:

  ```

python -m venv venv

```

3. Ative o ambiente vietual :

  ```

venv\Scripts\activate

```

4. Instale as dependências com o o ambiente virtual ativado:

```

pip install -r requirements.txt

```


6. Execute o comando:

```

python manage.py runserver

```

  

6. Por fim, o servidor inciará na porta:8000 - acesse as endpoints por :

```
http://127.0.0.1:8000

```

  

<p  align="right">(<a  href="#readme-top">voltar para o início</a>)</p>

  

## Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

  

#### Tecnologias

- [Python 3.12](https://www.python.org/) - Framework

- [Django 5.1](https://www.djangoproject.com/) - Framework

- [Django Rest Framework 3.15.2](https://www.django-rest-framework.org/) - Framework

 

  

#### Ferramentas

- [Postman](https://www.postman.com/) - Testes de API

- [VSCode](https://code.visualstudio.com/) - Editor de código

  
  

<p  align="right">(<a  href="#readme-top">voltar para o início</a>)</p>

  

## Licença

  

Este projeto esta sob a licença [MIT](./LICENSE). Consulte o arquivo LICENSE.md para mais informações.

  

<p  align="right">(<a  href="#readme-top">voltar para o início</a>)</p>

  

## Autor

<b>Julio Coutinho</b><br  />

<img  style="border-radius: 50%;"  src="https://avatars.githubusercontent.com/u/90656852?v=4"  width="100px;"  alt=""/><br  />

Projeto desenvolvido por Julio Coutinho. Entre em contato!

  

[LinkedIn](https://www.linkedin.com/in/juliocscoutinho//)

[E-mail](mailto:contact@juliocoutinho.com)

<p  align="right">(<a  href="#readme-top">voltar para o início</a>)</p>


