# Fidelity Test

> Um sistema de autenticação completo desenvolvido com Django, apresentando funcionalidade de registro, login e gerenciamento de usuários. O projeto foi arquitetado para ser seguro e robusto, incluindo:

-   **Validação de Formulários:** Tanto no lado do cliente (com JavaScript) quanto no servidor, para uma experiência de usuário aprimorada e segura.
-   **Segurança Anti-Bot:** Integração com Google reCAPTCHA na página de registro.
-   **Proteção Contra Força Bruta:** Implementação de um limite de tentativas de login (rate limiting) utilizando Django Cache com Redis.
-   **Ambiente Containerizado:** Toda a aplicação e seus serviços (PostgreSQL, Redis) são manuseados com Docker e Docker Compose, garantindo assim, um ambiente de desenvolvimento consistente e portável.

---

### 💻 Pré-requisitos

Antes de começar, garanta que você tenha os seguintes softwares instalados:

-   [Docker](https://www.docker.com/products/docker-desktop/)
-   [Docker Compose](https://docs.docker.com/compose/install/) (geralmente já vem com o Docker Desktop)

O Python não precisa ser instalado localmente, pois ele será executado dentro de um contêiner Docker.

---

### 🚀 Instalação e Execução

Para rodar o Fidelity Test em sua máquina, siga estas etapas:

**1. Clone o Repositório:**
```bash
git clone https://github.com/BenitesG/Fidelity_Test.git
cd Fidelity_Test
```

**2. Configure as Variáveis de Ambiente:**
O projeto utiliza um arquivo `.env` para gerenciar configurações sensíveis.
Navegue até a pasta dotenv_files/.
Renomeie o arquivo .env-example para `.env`.
Abra o arquivo .env e substitua os valores CHANGE-ME e placeholders pelas suas chaves e credenciais reais (SECRET_KEY, senhas do banco de dados, chaves do reCAPTCHA, etc.).

**3. Construa e Inicie os Contêineres:**
Este comando irá construir a imagem da aplicação Django e iniciar todos os serviços (web, banco de dados e cache).
```bash
docker-compose up --build -d 
``` 
(--build: Vai construir a imagem a partir do Dockerfile. -d: Roda os contêineres em segundo plano)

**4. Aplique as Migrações do Banco de Dados:**
Com os contêineres rodando, execute as migrações para criar as tabelas no banco de dados.

```bash
docker-compose exec web python manage.py migrate
``` 

```bash
docker-compose exec web python manage.py migrate
```


### ☕ Usando o Fidelity Test
Após a instalação, a aplicação estará rodando e acessível no seu navegador via: http://127.0.0.1:8000/

**Possíveis comandos Úteis do Docker Compose:**

Ver logs em tempo real: docker-compose logs -f web

Parar todos os serviços: docker-compose down

Executar qualquer comando manage.py: docker-compose exec web python manage.py <seu_comando>
