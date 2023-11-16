document.addEventListener('DOMContentLoaded', function () {
    const consumableButton = document.querySelector('.consumable-button');
    const tableConsumable = document.querySelector('.tableconsumable');

    
    consumableButton.addEventListener('click', function () {
      // Alterna a visibilidade da tabela ao clicar no botão
      if (tableConsumable.style.display === 'none') {
        tableConsumable.style.display = 'block';
      } else {
        tableConsumable.style.display = 'none';
      }
    });
  });