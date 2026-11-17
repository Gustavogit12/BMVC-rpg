var form = document.getElementById("form-login");

// Só roda na tela de login (no dashboard não existe formulário)
if (form) {
    var usuario = document.getElementById("usuario");
    var senha = document.getElementById("senha");
    var aviso = document.getElementById("aviso");
    var btnMostrar = document.getElementById("btn-mostrar");
    var botoesTeste = document.querySelectorAll(".preencher");

    // 1. Mostrar e ocultar a senha
    btnMostrar.addEventListener("click", function () {
        if (senha.type === "password") {
            senha.type = "text";
            btnMostrar.textContent = "Ocultar senha";
        } else {
            senha.type = "password";
            btnMostrar.textContent = "Mostrar senha";
        }
    });

    // 2. Validação antes de enviar o formulário
    form.addEventListener("submit", function (evento) {
        usuario.classList.remove("invalido");
        senha.classList.remove("invalido");
        aviso.textContent = "";

        if (usuario.value.trim() === "" || senha.value === "") {
            evento.preventDefault();
            aviso.textContent = "Preencha o usuário e a senha.";
            if (usuario.value.trim() === "") {
                usuario.classList.add("invalido");
            }
            if (senha.value === "") {
                senha.classList.add("invalido");
            }
        }
    });

    // 3. Preencher automaticamente com as credenciais de teste
    for (var i = 0; i < botoesTeste.length; i++) {
        botoesTeste[i].addEventListener("click", function () {
            usuario.value = this.getAttribute("data-user");
            senha.value = this.getAttribute("data-pass");
        });
    }
}