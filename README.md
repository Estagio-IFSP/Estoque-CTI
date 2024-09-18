# estoque-CTI

## Índice
- [Contexto](#Contexto)
- [Instalação](#Instalação)
- [Documentação](#Documentação)

## Contexto
Um sistema de manejamento do estoque de bens consumíveis e permanentes para a CTI do Instituto Federal de Ciência e Tecnologia do Estado de São Paulo, Campus de Jacareí.

## Instalação

Para rodar o sistema, é necessário ter o Python 3.12.0 e o gerenciador de pacotes `pip`.

Primeiro, clone o repositório e crie um ambiente virtual:

```sh
git clone https://github.com/Estagio-IFSP/Estoque-CTI
cd Estoque-CTI
python -m venv .venv
source .venv/bin/activate
```

Após os comandos acima, o ambiente virtual deve estar habilitado.

Em seguida, instale as dependências:

```sh
pip install -r requirements.txt
```

Para a execução, é necessário ainda um banco de dados PostgreSQL disponível.

O comando abaixo pode ser utilizado para executar um container Docker com o PostgreSQL:

```sh
docker run --rm -d -e POSTGRES_DB=stock_control -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=password -p 5432:5432 postgres:16.3-alpine3.20 postgres
```

Se desejar ver a saída de log do banco de dados, retire o argumento `-d`. Se desejar preservar o container após a execução para poder executá-lo novamente, retire o argumento `--rm`. Com este argumento, o container será sempre apagado após a execução.

O comando acima foi testado apenas com o [Podman](https://podman.io/).

O ambiente de execução precisa ter as seguintes variáveis de ambiente configuradas. Os valores abaixo são para um ambiente de desenvolvimento.

```sh
export DJANGO_HOST="localhost"
export DJANGO_SECRET="4d2e7c5b600aa340df7cd4d9489594d6fd2178b2a97072e1f4036f0732ee0af3"
export DJANGO_DB_NAME=""
export DJANGO_DB_USER=""
export DJANGO_DB_PASSWORD=""
export DJANGO_DB_HOST="localhost"
```

O valor dado acima para a variável `DJANGO_SECRET` é apenas um exemplo. Ele pode ser qualquer valor aleatório e não precisa permanecer sempre o mesmo. No ambiente de produção, esta variável será configurada para um valor diferente do usado no desenvolvimento.

Para as variáveis que iniciam com o padrão `DJANGO_DB_`, os valores serão correspondentes ao nome do banco de dados, do nome de usuário, da senha e do endereço IP do servidor. Usando o comando Docker sugerido acima, a configuração seria:

```sh
export DJANGO_DB_NAME="stock_control"
export DJANGO_DB_USER="admin"
export DJANGO_DB_PASSWORD="password"
export DJANGO_DB_HOST="localhost"
```

No ambiente de desenvolvimento, é recomendo ainda configurar a variável de ambiente `DEBUG=TRUE` para que as mensagens de erro sejam mais úteis. Essa variável não deve ser usada no ambiente de produção.

Com o banco de dados disponível, é possível realizar as migrações para que o banco possua todas as tabelas necessárias:

```sh
python manage.py makemigrations
python manage.py migrate
```

Dependendo das alterações feitas, em particular mudanças nos modelos da aplicação (arquivo `stockControl/models.py`), o comando abaixo pode ser necessário para sincronizar o banco de dados com as migrações feitas:

```sh
python manage.py migrate --run-syncdb
```

Por fim, o comando abaixo inicializa o servidor da aplicação. Ela ficará acessível em <http://localhost:8000>

```sh
python manage.py runserver
```

### Imagem Docker

Para o ambiente de produção, os arquivos `Dockerfile` e `docker-compose.yaml` permitem que o sistema e um banco de dados sejam executados em conjunto através de containers utilizando o Docker.

Para subir ambos pode-se utilizar `docker compose up` estando na raiz deste repositório. O Docker se encarregará de subir o sistema apenas quando o banco de dados já estiver disponível.

Para que o comando `compose` funcione, é preciso que exista o diretório `/root/secrets` contendo os seguintes arquivos:

- `db_name.txt`
- `db_user.txt`
- `db_password.txt`
- `django_secret.txt`

Estes arquivos devem conter os respectivos valores que serão lidos para configurar as variáveis de ambientes descritas acima, na seção de instalação. É recomendável que as permissões adequadas sejam dadas a esses arquivos para que possam ser lidos ou sobrescritos apenas pelo usuário `root`.

Se desejar gerar a imagem apenas da aplicação Python a partir deste repositório de código ou sempre que o sistema for atualizado, pode-se usar o seguinte comando na raiz do repositório:

```sh
docker build -t estoque-cti .
```

Este comando irá gerar uma imagem chamada estoque-cti com a tag `:latest`.

## Documentação

### Requisitos

| Nº | Requisito                               | Tipo      | Prioridade | Descrição                                                                                           |
|----|-----------------------------------------|-----------|------------|-----------------------------------------------------------------------------------------------------|
| R1 | REALIZAR O CRUD DOS PRODUTOS | Funcional | # | Através da interface que seja possível a realização do processo de criação de novos produtos, leitura para serem mostrados na interface e também sua pesquisa pelo nome, atualização de novas informações dos produtos, sejam elas aumentar ou diminuir os números de produtos emprestados, ou armazenados, atualização de nomes e códigos dos produtos, e que seja possível realizar a remoção geral do produto do sistema.||
| R1.1 | DISPONIBILIZAR RECURSOS DE CRIAÇÃO DE PRODUTOS | Funcional | # |Na interface de exibição deve ser possível realizar o cadastro de um novo produto ainda não cadastrado, onde para isso seja necessário realizar o preenchimento do formulário quando solicitado o cadastro.|
| R1.1.1 | REALIZAR O FORMULÁRIO DE CRIAÇÃO DE PRODUTOS | Funcional | # | O formulário deve ser preenchido com as informações do produto como: ID, nome, marca, modelo, quantidade, forma que foi conseguido, com mês e ano, local de armazenamento, descrição, foto do produto para sua identificação e, caso seja um bem permanente, deverá possuir número de patrimônio.|
| R1.1.2 | CANCELAR O FORMULÁRIO | Funcional | # | Que seja disponível um botão para ser realizado o cancelamento do cadastro do produto a qualquer momento e te envie para a tela anterior.|
| R1.2 | DISPONIBILIZAR RECURSOS DE SELEÇÃO | Funcional | # | Na interface de exibição deve ser possível realizar a seleção de um tipo específico de produto e dentro de sua página realizar as devidas atualizações, onde se abra um formulário sobre as informações e o que deseja modificar.|
| R1.2.1 | ATUALIZAR O FORMULÁRIO DO PRODUTO | Funcional | # | Quando clicado no ícone de edição do produto, o formulário de edição com os itens do R1.1.1 será mostrado já preenchido, onde o usuário modificará uma ou mais informações do produto e será disponibilizado o botão “Salvar” para salvar as alterações.|
| R1.2.2 | CANCELAR ATUALIZAÇÕES DO FORMULÁRIO DO PRODUTO | Funcional | # | Durante a realização do formulário será possível realizar o cancelamento das alterações realizadas a qualquer momento clicando no botão “Cancelar”, voltando para a tela anterior abortando a operação.|
| R1.3 | DISPONIBILIZAR RECURSOS DE PESQUISA | Funcional | # | Na interface de exibição deve ser possível realizar a pesquisa de um produto, sendo ela pelo seu nome, código, patrimônio ou tipo do produto, onde será enviado para uma tela com os diversos produtos que atendam a pesquisa realizada.|
| R1.4 | DISPONIBILIZAR RECURSOS DE REMOÇÃO | Funcional | # | Ao lado do nome do produto deverá ter um botão para realizar sua remoção, apagando assim do banco de dados, como em casos de baixa patrimonial.|
| R1.4.1 | REALIZAR A DESCRIÇÃO DO MOTIVO DE REMOÇÃO | Funcional | # | Quando solicitada a remoção do produto, o usuário deverá preencher uma breve descrição do motivo, sendo confirmada clicando em “Ok”.|
| R1.4.1.1 | REALIZAR O CANCELAMENTO DE REMOÇÃO NA DESCRIÇÃO | Funcional | # | O usuário pode realizar o cancelamento da remoção do produto na página de descrição clicando no botão “Cancelar” a qualquer momento.|
| R1.4.2 | CONFIRMAR A REMOÇÃO DO PRODUTO | Funcional | # | Quando os critérios forem atendidos e preenchidos, deve-se realizar a confirmação de remoção do produto com a frase “Tem certeza que deseja deletar o produto?” com as opções “Sim” e “Não”, onde na primeira opção o produto será removido, caso contrário o processo é cancelado e retornará à tela anterior.|
| R2 | LISTAR DE E-MAILS | Funcional | # | Deve-se cadastrar todos os e-mails dos interessados para recebimento de notificações e outras funcionalidades que possam utilizar da lista.|
| R3 | REALIZAR A MANUTENÇÃO DO GERENCIAMENTO DE ESTOQUE | Funcional | # | Cada produto deve possuir em seu registro um número mínimo desejado em estoque, para que caso o estoque atinja este valor, um alerta será enviado, via e-mail ou sistema (pop-up), a todos os e-mails cadastrados, avisando sobre a necessidade de um re-estoque deste.|
| R4 | SOLICITAR REABASTECIMENTO DE PRODUTOS | Funcional | # | A interface possuirá um botão de cadastro de reabastecimento de produtos, que deverá ser informado a quantidade desejada, e um relatório de produtos que já foram solicitados previamente apagar?|
| R4.1 | REALIZAR SOLICITAÇÃO DE REABASTECIMENTO | Funcional | # | Deve possuir uma funcionalidade para ser possível realizar o cadastro de uma nova solicitação de pedido de produtos, onde será necessário o preenchimento do formulário solicitação.|
| R4.1.1 | REALIZAR FORMULÁRIO DE REABASTECIMENTO | Funcional | # | Ao ser solicitado o reabastecimento de um produto, o usuário precisará realizar o preenchimento do formulário do produto com a quantidade solicitada.|
| R4.2 | REALIZAR A CONFIRMAÇÃO DE REABASTECIMENTO | Funcional | # | Deve possuir uma funcionalidade para ser possível confirmar que o produto chegou, onde o usuário precisara realizar o preenchimento do formulário de confirmação.|
| R4.2.1 | REALIZAR O FORMULÁRIO DE CONFIRMAÇÃO | Funcional | # | Ao ser confirmado o reabastecimento de um produto, o usuário precisará realizar o preenchimento do formulário do produto com a data de chegada e método que foi conseguido o produto.|
| R4.3 | REALIZAR A EMISSÃO DE RELATÓRIO SOLICITAÇÃO DE REABASTECIMENTO | Funcional | Média | O relatório de reabastecimento deve conter a data de solicitação dos produtos, sendo indicado de alguma forma de fácil reconhecimento se o produto já foi recebido ou não e qual produto foi solicitado.|
| R5 | REALIZAR O EMPRÉSTIMO DE PRODUTOS | Funcional | # | O sistema deve possuir uma função para o cadastro de empréstimos de produtos realizados, onde para realizar o cadastro deve ser preenchido um formulário.|
| R5.1 | REALIZAR O FORMULÁRIO DE EMPRÉSTIMO DE PRODUTOS | Funcional | # | Ao ser realizado o cadastro de empréstimo, o formulário deve solicitar as informações como local de onde vai estar, data de solicitação de empréstimo e uma descrição opcional para informações adicionais|
| R5.2 | REALIZAR A DEVOLUÇÃO DE EMPRÉSTIMO DE PRODUTOS | Funcional | # |O sistema deve possuir uma função para a confirmação de devolução dos produtos que foram emprestados, onde deve solicitar o local onde vai ser armazenado o produto.|
| R6 | REALIZAR A EMISSÃO DE RELATÓRIO | Funcional | # | O sistema deve possuir uma função para a realização de emissão de relatórios de empréstimo de produtos e de solicitações de reabastecimento.|
| R6.1 | REALIZAR A EMISSÃO DE RELATÓRIO DE EMPRÉSTIMO | Funcional | # | O relatório de empréstimo deve conter a data de saída de devolução dos produtos, sendo indicado de alguma forma de fácil reconhecimento se saiu ou foi devolvido e qual produto foi emprestado/devolvido.|
| R6.2 | REALIZAR A EMISSÃO DE RELATÓRIO DE REABASTECIMENTO | Funcional | Média | O relatório de reabastecimento deve conter a data da aquisição dos produtos, sua origem e a quantia adquirida|

#### Legenda:
- **Tipo:**
  - Funcional: Descreve uma função específica do sistema.
- **Prioridade:**
  - Alta: Requisitos essenciais para o funcionamento básico do sistema ou que agregam alto valor ao usuário.
  - Média: Requisitos importantes, mas que podem ser implementados em fases posteriores ou têm menor impacto imediato.

### Diagramas

#### Diagrama de Caso de Uso
![image](./documents/diagrams/Diagrama%20de%20caso%20de%20uso.drawio.png)

#### Diagrama de Classes
![image](./documents/diagrams/Diagrama%20de%20classe%20Estagio.drawio.png)
