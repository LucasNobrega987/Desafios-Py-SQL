
# Meli Challenge

## Descrição
Este projeto implementa uma API Flask para o desafio Meli. A API permite adicionar interações entre personagens e consultar amigos em comum entre dois personagens.

## Configuração do Ambiente

### Requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Docker (opcional, se você quiser usar contêineres)

### Instalação

#### Clone o Repositório
```bash
git clone https://github.com/LucasNobrega987/meli-challenge.git
cd meli-challenge

------------------------------------------------
Configuração do Ambiente de Desenvolvimento
Para começar o desenvolvimento da minha API Flask, primeiro precisei configurar meu ambiente de desenvolvimento. Utilizei o Visual Studio Code (VSCode) como meu editor de código por sua versatilidade e suporte extensivo através de extensões.

Instalação do VSCode e Python:

Primeiramente, baixei e instalei o VSCode do site oficial Visual Studio Code.
Em seguida, instalei a última versão do Python do site oficial do Python, garantindo que o Python e o pip estivessem acessíveis pelo terminal, marcando a opção de adicionar o Python ao PATH durante a instalação.
Configuração do VSCode:

Abri o VSCode e instalei a extensão Python pela loja de extensões, o que facilita muito a execução e o debug de scripts Python diretamente no editor.
Configurei o interpretador Python selecionando a versão que havia instalado anteriormente, acessando o comando Python: Select Interpreter na paleta de comandos (Ctrl+Shift+P).
Criação do Projeto Flask
Estruturação do Projeto:

Criei uma nova pasta chamada FlaskAPI e abri essa pasta no VSCode.
Dentro desta pasta, criei um novo arquivo chamado app.py, que serviria como o coração da minha aplicação Flask.
Desenvolvimento da Aplicação:

Escrevi o código inicial do Flask no arquivo app.py, definindo as rotas e a lógica para lidar com requisições POST para interações entre personagens. Utilizei a rota /interaction para aceitar dados JSON especificando os detalhes da interação entre dois personagens.
Execução da API
Rodando a Aplicação:

Para executar a aplicação, usei o terminal integrado no VSCode. Naveguei até o diretório do projeto e executei o comando python app.py. Isso iniciou o servidor de desenvolvimento Flask, tornando a API acessível localmente no endereço http://127.0.0.1:5000.
Testando a API com Postman
Configuração do Postman:

Baixei e instalei o Postman, que usei para criar e enviar requisições HTTP para a API e verificar as respostas.
Configurei uma nova requisição POST no Postman para a URL http://127.0.0.1:5000/interaction. No corpo da requisição, inseri os dados JSON que representavam uma interação entre dois personagens do 4º livro, conforme especificado pelos requisitos da API.
Envio de Requisições e Análise de Respostas:

Ao enviar a requisição, verifiquei a resposta para garantir que a API estava processando os dados corretamente e retornando os status apropriados. Para interações válidas do 4º livro, a API deveria retornar um status 201 e uma mensagem de sucesso.
Conclusão
Este processo me permitiu desenvolver e testar uma API Flask robusta de maneira eficiente, utilizando as ferramentas do VSCode e do Postman.
