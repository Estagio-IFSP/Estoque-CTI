# Backlog

- Funcionalidades pontuais
  - [ ] Botões para marcar como devolvido
    - [ ] Por item
    - [ ] Por empréstimo (todos os itens)
  - [ ] Desativação de itens
  - [ ] Botões de voltar
  - [ ] [Implementar Messages](https://docs.djangoproject.com/en/4.2/ref/contrib/messages)
  - [ ] [Aplicar classes CSS nas mensagens de erro da validação de formulários](https://getbootstrap.com/docs/5.3/forms/validation)

- Funcionalidades amplas
  - [ ] Envio de emails
    - [ ] Adicionar campo de email no cadastro de requerentes
    - [ ] Disparar emails 5 dias úteis e 10 dias úteis antes do vencimento para CTI e para requerente
    - [ ] Disparar emails após atraso para a CTI e para requerente
  - [ ] Implementar busca
  - [ ] Implementar paginação

- Não-funcional
  - [ ] Refatorar templates para melhorar legibilidade

## Feito
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
