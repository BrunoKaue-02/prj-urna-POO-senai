#  Urna Eletrônica em Python

Este projeto é uma simulação simples de **urna eletrônica**, desenvolvida em Python, com suporte a cadastro, listagem e exclusão de candidatos, utilizando persistência de dados em **JSON**.

---

##  Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Python 3.10+**
- **pip** (gerenciador de pacotes do Python)

Para verificar, execute no terminal:

```bash
python3 --version
pip --version



pip install -r requirements.txt

> Se você estiver em uma distribuição Debian/Ubuntu e o projeto usar bibliotecas gráficas (Tkinter), instale a dependência do sistema:

```bash
sudo apt-get update
sudo apt-get install python3-tk
```

## Variáveis de ambiente

O projeto usa um arquivo `.env` para apontar para os arquivos JSON que armazenam os dados. Existe um arquivo de exemplo `.env.example` na raiz com as variáveis necessárias.

Variáveis esperadas:

- `JSON_PATH_CANDIDATOS` — caminho para `data/candidatos.json`
- `JSON_PATH_ELEITORES` — caminho para `data/eleitores.json`
- `JSON_PATH_PARTIDO` — caminho para `data/partidos.json`
- `JSON_PATH_VOTOS` — caminho para `data/votos.json`

Como usar:

1. Copie o exemplo para `.env`:

```bash
cp .env.example .env
```

2. Ajuste os caminhos se necessário e execute o projeto.

Observação: o repositório ignora arquivos `.env` e outras configurações locais por segurança. Não versionamos variáveis sensíveis — copie e edite `.env.example` para criar seu `.env` local.

