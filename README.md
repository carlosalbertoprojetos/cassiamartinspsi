# CassiaMartinsPsi
 
-Projeto de desenvolvimento de um framework Django para criar uma **Landing Page** focada na **identidade profissional** no campo da Psicologia.
-A página oferece informações sobre a atuação, abordagens, experiência, artigos e formas de contato. O sistema possibilita a gestão de conteúdo de maneira prática, com uma estrutura que facilita a atualização das informações relacionadas à área de psicologia. A aplicação é uma solução personalizada para profissionais que desejam apresentar sua experiência e estabelecer uma presença online de forma eficiente.
+Projeto desenvolvido com Django para criar uma Landing Page voltada à identidade profissional em Psicologia.
 
 ## Funcionalidades
 
-- Exibição de informações sobre a profissional, sua abordagem e experiência.
-- Inclusão de artigos relevantes para a área de atuação.
-- Formulário de contato para interação com visitantes.
-- Layout responsivo com foco em uma apresentação clara e profissional.
+- **Página de apresentação profissional:** inclui informações sobre a abordagem e experiência.
+- **Listagem de artigos** relevantes, voltados à área de Psicologia.
+- **Formulário de contato**, permitindo interação direta com visitantes.
 
-## Aplicações
+## Estrutura do Projeto
 
-Este projeto é ideal para psicólogos e profissionais da área que desejam criar uma página pessoal ou institucional online, destacando suas competências, serviços e artigos.
+### Models
+
+1. **Profile**
+   - Armazena dados da psicóloga, como nome, especializações, descrição da abordagem e contato.
+   - É a base da apresentação profissional na landing page.
+
+2. **Article**
+   - Representa artigos ou publicações na área da Psicologia.
+   - Campos incluem título, conteúdo e data de publicação, oferecendo uma seção de blog para a profissional.
+
+3. **Contact**
+   - Modela mensagens enviadas por visitantes através do formulário de contato.
+   - Campos como nome, email, assunto e mensagem, para organizar as interações e respostas.
+
+### Funcionalidades no Sistema
+
+- **Exibição de Informações Profissionais:** O `Profile` é exibido na página principal, apresentando a psicóloga e suas qualificações.
+- **Publicação de Conteúdos:** `Article` permite adicionar e listar publicações relevantes, reforçando a autoridade da profissional.
+- **Comunicação com Visitantes:** `Contact` processa as mensagens do formulário, registrando no banco de dados para acompanhamento.
 
 ## Instalação
 
-1. Clone este repositório:
+1. Clone o repositório e instale as dependências:
    ```bash
    git clone https://github.com/carlosalbertoprojetos/cassiamartinspsi.git
-   ```
-
-2. Navegue até o diretório do projeto:
-   ```bash
    cd cassiamartinspsi
-   ```
-
-3. Instale as dependências:
-   ```bash
    pip install -r requirements.txt
    ```
 
-4. Rode as migrações do banco de dados:
+2. Rode as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```
 
-5. Inicie o servidor:
+3. Inicie o servidor:
    ```bash
    python manage.py runserver
    ```
 
-6. Acesse a página no navegador: `http://127.0.0.1:8000`
+4. Acesse `http://127.0.0.1:8000` no navegador.
 
 ## Licença
 
-MIT License. Veja o arquivo LICENSE para mais detalhes.
