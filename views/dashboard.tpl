<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Painel - Demigod RPG</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <div class="caixa">
        <h1>{{personagem.name}}</h1>
        <p>{{personagem.lineage}}</p>

        <table>
            <tr><td>Nível</td><td>{{personagem.level}}</td></tr>
            <tr><td>HP</td><td>{{personagem.hp}}</td></tr>
            <tr><td>Energia</td><td>{{personagem.energy}}</td></tr>
            <tr><td>Ataque</td><td>{{personagem.attack}}</td></tr>
            <tr><td>Defesa</td><td>{{personagem.defense}}</td></tr>
            <tr><td>Velocidade</td><td>{{personagem.speed}}</td></tr>
        </table>

        <h2>Poder da linhagem</h2>
        <p>{{personagem.perk}}</p>

        <h2>Habilidades desbloqueadas</h2>
        <ul>
            % for ability in personagem.unlocked_abilities():
            <li>{{ability.name}} (custo {{ability.cost}}, poder {{ability.power}})</li>
            % end
        </ul>

        <form method="post" action="/logout">
            <button type="submit">Sair</button>
        </form>
    </div>

    <script src="/static/js/script.js"></script>
</body>
</html>