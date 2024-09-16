# Backlog

- Empréstimos
  - [ ] Poder determinar se um bem está emprestado ou não
      - [ ] Não marcar em vermelho a data passada de devolução para um bem que já foi devolvido
  - [ ] Não permitir que a quantidade de bens emprestados exceda a de bens disponíveis
  - [ ] Não pedir dados de garantia se o bem criado não é permanente

- Funcionalidades pontuais
  - [ ] [Adicionar Mensagens](https://docs.djangoproject.com/en/4.2/ref/contrib/messages)
  - [ ] [Aplicar classes CSS nas mensagens de erro da validação de formulários](https://getbootstrap.com/docs/5.3/forms/validation)
  - [ ] Desativação de itens
  - [ ] Botões de voltar

- Funcionalidades amplas
  - [ ] Implementar busca
  - [ ] Implementar paginação
  - [ ] Implementar autenticação
  - [ ] Envio de emails
    - [ ] Adicionar campo de email no cadastro de requerentes
    - [ ] Disparar emails 5 dias úteis e 10 dias úteis antes do vencimento para CTI e para requerente
    - [ ] Disparar emails após atraso para a CTI e para requerente

- Não-funcional
  - [ ] Refatorar templates para melhorar legibilidade

## Feito
- [x] Avisar ao fazer um empréstimo para alguém com um empréstimo já em atraso
- [x] Status permanente na listagem de bens
- [x] Atualizar para o Django 5
- [x] Mostrar empréstimos em atraso na página inicial da dashboard
- [x] Permitir emprestar múltiplos bens em um único empréstimo
- [x] Listar itens de um empréstimo no detalhe do empréstimo
- [x] Permitir excluir um item de empréstimo
- [x] Armazenar telefones como strings ou aumentar o tamanho máximo dos campos de inteiros
