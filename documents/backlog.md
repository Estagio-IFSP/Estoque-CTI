# Backlog


- Funcionalidades amplas
  - [x] Implementar paginação
    - [ ] Possibilitar escolher quantidade de itens por página
  - [x] Envio de emails
    - [ ] Configurar emails para serem enviados às 8h da manhã
    - [x] Adicionar campo de email no cadastro de requerentes
    - [x] Enviar email 5 dias úteis e 10 dias úteis antes do vencimento
      - [ ] para CTI
      - [x] para requerente
    - [ ] Enviar email no ato do empréstimo
    - [ ] Enviar email no dia do vencimento
    - [ ] Enviar email 7 dias após o vencimento

- Funcionalidades pontuais
  - [ ] Desativação de itens
  - [ ] Botões para marcar como devolvido
    - [ ] Por empréstimo (todos os itens)
    - [ ] Por item
  - [ ] [Implementar Messages](https://docs.djangoproject.com/en/4.2/ref/contrib/messages)
  - [ ] [Aplicar classes CSS nas mensagens de erro da validação de formulários](https://getbootstrap.com/docs/5.3/forms/validation)
  - [ ] Botões de voltar

- Itens levantados no teste de 04/11
  - [x] Remover seleção de empréstimo ao adicionar novo item
  - [x] Ao desistir de criar um empréstimo, ele permanece vazio no sistema
  - [ ] Status do empréstimo na página de detalhe de requerente
  - [ ] Adicionar seção histórico na página de requerente
  - [ ] Filtrar bens por consumível ou permanente
  - [ ] Telefone mostra como `None` na listagem de requerente
  - [ ] Eliminar item consumível ao emprestar
  - [ ] Alertas quando um item está com estoque baixo
  - [ ] Histórico de quem (qual conta) realizou cada ação
  - [ ] Modelo "Processo" para saber como os bens foram adquiridos
    - [ ] Bem
    - [ ] Quantidade
    - [ ] Tipo da aquisição
      - [ ] Ata/carona
      - [ ] Ata/participante
      - [ ] Processo próprio
      - [ ] Doações
      - [ ] Almoxarifado
      - [ ] Troca entre campus
      - [ ] Receita federal
    - [ ] Número do processo (opcional)
  - [ ] Ordenação de colunas
  - [ ] Validação das datas (data de retirada deve ser menor que a de devolução)


- Não-funcional
  - [ ] Refatorar templates para melhorar legibilidade

## Feito
- [x] Implementar busca
- [x] Implementar autenticação
- [x] Avisar ao fazer um empréstimo para alguém com um empréstimo já em atraso
- [x] Status permanente na listagem de bens
- [x] Atualizar para o Django 5
- [x] Mostrar empréstimos em atraso na página inicial da dashboard
- [x] Permitir emprestar múltiplos bens em um único empréstimo
- [x] Listar itens de um empréstimo no detalhe do empréstimo
- [x] Permitir excluir um item de empréstimo
- [x] Armazenar telefones como strings ou aumentar o tamanho máximo dos campos de inteiros
- [x] Poder determinar se um bem está emprestado ou não
    - [x] Não marcar em vermelho a data passada de devolução para um bem que já foi devolvido
    - [x] Não permitir que a quantidade de bens emprestados exceda a de bens disponíveis
- [x] Não pedir dados de garantia se o bem criado não é permanente
- [x] Marcar em cinza uma data de devolução nos próximos 7 dias
- [x] Marcar em amarelo uma data de devolução igual ao dia atual
