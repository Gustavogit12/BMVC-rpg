# ⚡ Demigod RPG: Portal de Acesso do Jogador

Aplicação web em **Python + Bottle** que autentica jogadores do **Demigod RPG** e mostra o personagem semideus ligado a cada conta. O projeto segue a arquitetura **BMVC** (Bottle Model-View-Controller) e aplica conceitos de **Orientação a Objetos**.

## Propósito

O portal é a porta de entrada do jogo. O jogador informa usuário e senha, o sistema confere as credenciais e carrega o objeto do personagem (`ChildOfZeus`, `ChildOfPoseidon` ou `ChildOfHades`), exibindo linhagem, nível, HP, energia, ataque, defesa, velocidade, poder da linhagem e habilidades desbloqueadas.

## Funcionalidades

- Tela de login com mensagem de erro quando usuário ou senha estão incorretos.
- Credenciais de teste na tela, com preenchimento automático ao clicar.
- Botão para mostrar e ocultar a senha.
- Validação no navegador antes do envio, avisando quando algum campo está vazio.
- Dashboard com os atributos do personagem e suas habilidades.
- Botão de logout que encerra a sessão.
- Sessão controlada por cookie assinado.

## Conceitos de Orientação a Objetos

| Conceito | Onde aparece |
|---|---|
| Herança | `Demigod` e `Enemy` herdam de `Entity`; `ChildOfZeus`, `ChildOfPoseidon` e `ChildOfHades` herdam de `Demigod` |
| Polimorfismo | `basic_attack` e `take_damage` são sobrescritos nas subclasses, e cada linhagem se comporta de um jeito |
| Encapsulamento | Cada classe reúne seus dados e métodos; o `UserModel` esconde como os usuários são guardados |
| Composição | Um `Demigod` possui uma lista de objetos `Ability` |
| `super()` | Usado nos construtores e nos métodos sobrescritos para reaproveitar a classe pai |

### Linhagens

| Classe | Característica |
|---|---|
| `ChildOfZeus` | Chance de acerto crítico, que dobra o dano |
| `ChildOfPoseidon` | Recebe 10% menos dano |
| `ChildOfHades` | Rouba 25% do dano causado para recuperar vida |

## Arquitetura BMVC

| Camada | Pasta | Responsabilidade |
|---|---|---|
| Model | `models/` | Classes do jogo (`rpg_engine.py`) e usuários (`user_model.py`) |
| View | `views/` | Templates `login.tpl` e `dashboard.tpl` |
| Controller | `controllers/` | Rotas, validação do login e sessão (`auth_controller.py`) |
| Estáticos | `static/` | `css/style.css` e `js/script.js` |

## Estrutura do projeto

```
demigod_rpg_simples/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── models/
│   ├── __init__.py
│   ├── rpg_engine.py
│   └── user_model.py
├── controllers/
│   ├── __init__.py
│   └── auth_controller.py
├── views/
│   ├── login.tpl
│   └── dashboard.tpl
└── static/
    ├── css/style.css
    └── js/script.js
```

## Como executar

Pré-requisito: Python 3.9 ou superior.

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Se o PowerShell bloquear a ativação do ambiente virtual, rode antes:
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Depois acesse **http://127.0.0.1:8080** no navegador.

## Credenciais de teste

| Usuário | Senha | Personagem |
|---|---|---|
| `thalia` | `raio123` | `ChildOfZeus("Thalia")` |
| `percy` | `mar123` | `ChildOfPoseidon("Percy")` |
| `nico` | `sombra123` | `ChildOfHades("Nico")` |

## Rotas

| Método | Rota | Descrição |
|---|---|---|
| GET | `/` | Redireciona para o login ou para o dashboard |
| GET | `/login` | Exibe o formulário de login |
| POST | `/login` | Confere as credenciais e cria a sessão |
| GET | `/dashboard` | Exibe o personagem (exige login) |
| POST | `/logout` | Encerra a sessão |
| GET | `/static/<arquivo>` | Serve o CSS e o JavaScript |

## Tecnologias

Python, Bottle, HTML5, CSS3 e JavaScript puro.

## Observações

- As senhas ficam em texto simples no Model e os usuários ficam na memória. Isso é só para fins didáticos; um sistema real usaria banco de dados e senhas com hash.
- Os dados do jogador voltam ao padrão sempre que o servidor é reiniciado.

## Autor

Gustavo, projeto acadêmico de BMVC I.