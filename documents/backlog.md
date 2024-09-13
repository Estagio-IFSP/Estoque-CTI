# Backlog

- Empréstimos
  - [ ] Avisar ao fazer um empréstimo para alguém com um empréstimo já em atraso
  - [ ] Poder determinar se um bem está emprestado ou não
      - [ ] Não marcar em vermelho a data passada de devolução para um bem que já foi devolvido
  - [ ] Não permitir que a quantidade de bens emprestados exceda a de bens disponíveis
  - [ ] Não pedir dados de garantia se o bem criado não é permanente

- Funcionalidades amplas
  - [ ] Implementar busca
  - [ ] Implementar paginação
  - [ ] Implementar autenticação

- Funcionalidades pontuais
  - [ ] Desenvolver uma página inicial na dashboard com os empréstimos em atraso
  - [ ] [Adicionar Mensagens](https://docs.djangoproject.com/en/4.2/ref/contrib/messages)
  - [ ] Aplicar classes CSS nas mensagens de erro da validação de formulários
      - <https://getbootstrap.com/docs/5.3/forms/validation/>

## Feito
- [x] Atualizar para o Django 5
- [x] Permitir emprestar múltiplos bens em um único empréstimo
- [x] Listar itens de um empréstimo no detalhe do empréstimo
- [x] Permitir excluir um item de empréstimo
- [x] Armazenar telefones como strings ou aumentar o tamanho máximo dos campos de inteiros
