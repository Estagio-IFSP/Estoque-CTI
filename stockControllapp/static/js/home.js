// Capturando o botão "Registrar-se" e a caixa de registro
const signupButton = document.querySelector('.signup');
const signupBox = document.querySelector('.signupbox');
const closeSignupButton = document.querySelector('.back');

// Adicionando evento de clique ao botão "Registrar-se"
signupButton.addEventListener('click', function() {
    signupBox.classList.add('active'); // Adiciona a classe para mostrar a caixa
});

// Adicionando evento de clique ao botão "Fechar"
closeSignupButton.addEventListener('click', function() {
    signupBox.classList.remove('active'); // Remove a classe para esconder a caixa
});

