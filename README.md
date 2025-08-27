        # Remover Fundo — Projeto completo (Flask + rembg)

        Este projeto fornece uma pequena aplicação web que permite ao usuário selecionar uma imagem (JPG/PNG), visualizar imediatamente a prévia no navegador e baixar uma versão PNG **sem fundo** usando o `rembg` no servidor.

## Estrutura

```
projeto/
 ├─ app.py
 ├─ requirements.txt
 ├─ templates/index.html
 ├─ static/style.css
 ├─ static/script.js
```

## Rodando localmente (recomendado)

1. Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\\Scripts\\activate   # Windows
```
2. Instale dependências:

```bash
pip install -r requirements.txt
```

> Nota: `rembg` usa bibliotecas nativas e pode exigir `pip` com compiladores ou rodas (wheels). Em muitos ambientes, `pip install rembg` funciona; se tiver problemas, tente usar a imagem Docker fornecida.

3. Rode a app:

```bash
python app.py
```

Abra `http://127.0.0.1:5000` no navegador.

## Deploy

- **Vercel** não suporta apps Python diretamente. Use **Render**, **Railway**, **Heroku** ou Docker.

### Deploy com Docker (qualquer PaaS que aceite container)

1. Build:
```bash
docker build -t remover-fundo .
```
2. Run:
```bash
docker run -p 5000:5000 remover-fundo
```

## Dockerfile e Heroku

Incluí um `Dockerfile` e um `Procfile` no repositório para deploys mais fáceis.

## Avisos

- O processamento é feito no servidor com `rembg` (open-source). Imagens não são armazenadas permanentemente.
- Para produção, ajuste timeouts e limites de upload.

