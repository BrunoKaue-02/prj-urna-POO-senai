# Urna Eletrônica em Python

Uma pequena simulação de urna eletrônica escrita em Python — permite cadastro, listagem e exclusão de Candidatos, Eleitores, Partidos e computação básica de votos. Os dados são mantidos em arquivos JSON na pasta `data/`.

---

## 🚀 Rápido — instalar e executar

1) Crie e ative um ambiente virtual (recomendado):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2) Instale dependências:

```bash
pip install -r requirements.txt
```

3) Copie as variáveis de ambiente de exemplo e ajuste, se necessário:

```bash
cp .env.example .env
# edite .env com os caminhos corretos para os arquivos JSON se precisar
```

4) Execute a aplicação:

```bash
python3 main.py
```

> Se você estiver em Debian/Ubuntu e o projeto usar Tkinter (ex.: plotagens com matplotlib usando o backend Tk), instale a dependência do sistema:

```bash
sudo apt-get update
sudo apt-get install python3-tk
```

---

## 🔧 Variáveis de ambiente

As variáveis de configuração estão no `.env` (existe `.env.example` com valores sugeridos). Variáveis usadas:

- `JSON_PATH_CANDIDATOS` — caminho para o JSON de candidatos (ex.: `data/candidatos.json`)
- `JSON_PATH_ELEITORES` — caminho para o JSON de eleitores (ex.: `data/eleitores.json`)
- `JSON_PATH_PARTIDO` — caminho para o JSON de partidos (ex.: `data/partidos.json`)
- `JSON_PATH_VOTOS` — caminho para o JSON de votos (ex.: `data/votos.json`)

O repositório ignora `.env` por segurança; mantenha apenas `.env.example` versionado.

---

## 📁 Estrutura do projeto

Principais pastas e arquivos:

- `main.py` — ponto de entrada (inicia o menu interativo)
- `controller/` — lógica das operações (cadastrar, apagar, listar, votar, resultados)
- `models/` — classes (Candidato, Eleitor, Partido, Voto)
- `utils/` — utilitários para leitura/gravação JSON, menu e validações
- `data/` — arquivos JSON com dados persistentes usados pelo app

---

## 🧭 Como os dados são armazenados

Os dados são salvos em JSON. Exemplos de campos esperados:

- Eleitor: `{ "nome": "Fulano", "idade": 30, "cpf": "11122233344", "ja_votou": false }`
- Candidato: `{ "nome": "Beltrano", "idade": 45, "cpf": "22233344455", "partido": "ABC", "numero": "12", "cargo": "Prefeito", "votos": 0, "ja_votou": false }`

O projeto já traz arquivos de exemplo em `data/` para testes.

---

## 🩺 Troubleshooting (erros comuns)

- ModuleNotFoundError: python-dotenv
	- Solução: `pip install python-dotenv` (já listado em `requirements.txt`).
- Erro ao salvar/ler arquivos JSON
	- Verifique as variáveis no `.env` apontando para arquivos existentes. Use caminhos relativos como `data/*.json`.
- Gráficos não abrem em Linux
	- Instale `python3-tk` no Debian/Ubuntu: `sudo apt-get install python3-tk`.

---

## ✅ Contribuindo

Contribuições são bem-vindas — abra issues e PRs. Para mudanças de função/assinatura, atualize exemplos e teste localmente.

---

## 📄 Licença

Projeto sem licença explicitada — adicione uma licença (ex.: MIT) se quiser tornar público e abrir contribuições.

