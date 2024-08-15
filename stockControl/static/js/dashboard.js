document.addEventListener('DOMContentLoaded', function () {
  const consumableButton = document.querySelector('.consumable-button');
  const tableConsumable = document.querySelector('.tableconsumable');

  consumableButton.addEventListener('click', function () {
    // Alterna a visibilidade da tabela ao clicar no botão

    const styles = window.getComputedStyle(tableConsumable);

    if (styles.getPropertyValue("display") === 'none') {
      tableConsumable.style.display = 'block';
    } else {
      tableConsumable.style.display = 'none';
    }
  });
});
