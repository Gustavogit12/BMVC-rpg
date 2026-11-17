<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demigod RPG - Login</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <div class="caixa">
        <h1>Demigod RPG</h1>
        <p>Portal de acesso do jogador. Entre com sua conta para ver o seu semideus.</p>

        % if error:
        <p class="erro">{{error}}</p>
        % end

        <p id="aviso" class="aviso"></p>

        <form id="form-login" method="post" action="/login">
            <label for="usuario">Usuário</label>
            <input type="text" id="usuario" name="username" value="{{username}}">

            <label for="senha">Senha</label>
            <input type="password" id="senha" name="password">

            <button type="button" id="btn-mostrar" class="secundario">Mostrar senha</button>
            <button type="submit">Entrar</button>
        </form>

        <div class="teste">
            <p>Credenciais de teste (clique para preencher):</p>
            % for u in test_users:
            <button type="button" class="preencher secundario"
                    data-user="{{u['username']}}" data-pass="{{u['password']}}">{{u['username']}}</button>
            % end
        </div>
    </div>

    <script src="/static/js/script.js"></script>
</body>
</html>