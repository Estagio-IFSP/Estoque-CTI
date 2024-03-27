
# Controle-de-Estoque
=======
# Sistema-de-Estoque-CTI

## Table of contents
* [Introduction](#Intro)
* [Requisitos](#Requisitos)
* [Installation](#Installation)
* [Start](#start)

## Intro
Um sistema de manejamento do estoque de bens consumivei e permanentes para a CTI do Instituto Federal de Ciencia e Tecnologia do Estado de São Paolo, Campus de Jacárei.

### Objetivos

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

### Legenda:
- **Tipo:**
  - Funcional: Descreve uma função específica do sistema.
- **Prioridade:**
  - Alta: Requisitos essenciais para o funcionamento básico do sistema ou que agregam alto valor ao usuário.
  - Média: Requisitos importantes, mas que podem ser implementados em fases posteriores ou têm menor impacto imediato.

### Funcionalidades


=======
## Diagramas

### Diagrama de Classes
![image](./documents/diagrams/Diagrama%20de%20classe%20Estagio.drawio.png)

### Diagrama Entidade Relacionamento
![image](./documents/diagrams/DER%20-%20Estoque.drawio.png)

## Installation
Project is created with:
* Python 3.7
* asgiref 3.7.2
* Django 4.2.7
* psycopg2 2.9.9
* sqlparse 0.4.4
* tzdata 2023.3
