# Fidelity Test

> Desafio técnico de um sistema de autenticação em Django com login, registro e autentificação de usuários.
Protege o acesso contra usuários indevidos, impedindo registros duplicados e acessos não autorizados, com envio de E-mail no login.

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Você instalou a versão mais recente de `<Python 3.9> / Bibliotecas presentes em requirements.txt / Docker, Docker-Compose>`
- Você ter uma máquina `<Windows / Linux / Mac>`.

## 🚀 Instalando Fidelity Test

Para instalar o Fidelity Test, siga estas etapas:

Linux e macOS:

```
# Clone o repositório
git clone https://github.com/BenitesG/fidelity_test.git
cd fidelity_test

# Configure o ambiente virtual e instale as dependências
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Windows:

```
# Clone o repositório
git clone https://github.com/BenitesG/fidelity_test.git
cd fidelity_test

# Configure o ambiente virtual e instale as dependências
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## ☕ Usando Fidelity Test

Para usar Fidelity Test, siga estas etapas:

```
# Configure o arquivo docker-compose e .env, trocando CHANGE-ME por suas informações.

# Suba o banco de dados
docker-compose up -d

# Faça as migrações
python manage.py migrate

# Inicie o servidor Django
python manage.py runserver

# Após iniciar o servidor, acesse o sistema pelo navegador:
http://127.0.0.1:8000/
```