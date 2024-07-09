Descrição da Minha Consulta SQL para Análise de Interações
Para este projeto, criei uma consulta SQL, que tem como objetivo analisar as interações entre personagens, calculando o número total de interações que cada personagem teve em cada livro e também um total geral. Esta análise é feita a partir de dados armazenados no Google BigQuery.

Estrutura e Funcionamento da Minha Consulta
A minha consulta SQL é organizada da seguinte maneira:

Criação da Tabela: Iniciei a consulta com um comando para criar uma nova tabela chamada interacoes_resultados dentro do dataset chamado Dataset. Se essa tabela já existisse, ela seria substituída por uma nova com os dados atualizados.

Processamento de Dados: Na sequência, executei uma seleção detalhada para somar as interações de cada personagem por livro, utilizando condições específicas para filtrar os dados por livro (1, 2 e 3). Além disso, calculei a soma total das interações de cada personagem.

União de Dados de Duas Colunas: Usei uma subconsulta para combinar dados de duas colunas diferentes (PERSONAGEM A e PERSONAGEM B) em uma única coluna chamada personagem. Isso foi necessário para garantir que as interações de ambos os personagens fossem consideradas de forma equitativa.

Agrupamento e Ordenação: Agrupei os resultados pelo nome do personagem e ordenei-os de acordo com o total de interações, do maior para o menor.

Preparação do Ambiente e Execução
Para executar esta consulta, segui vários passos essenciais:

Configuração no BigQuery: Garanti que eu tinha acesso ao Google BigQuery e que meu projeto estava configurado com a faturação ativada.

Criação e Configuração do Dataset e da Tabela: Criei um dataset chamado Dataset e uma tabela dataset1 dentro dele. Importei os dados necessários para esta tabela, assegurando-me de que todas as colunas estivessem corretamente nomeadas e formatadas.

Execução da Consulta: Inseri a consulta SQL no console do BigQuery e executei-a, criando assim a tabela interacoes_resultados com os dados processados.

Análise dos Resultados: Após a execução, analisei os resultados na tabela interacoes_resultados para verificar a corretude e a integridade dos dados.

Documentação e Revisões
Durante o projeto, fiz questão de documentar cada etapa e cada ajuste na consulta, para garantir que qualquer membro da equipe ou revisor futuro possa entender e replicar o processo sem dificuldades. Além disso, mantive todas as informações acessíveis para que qualquer pessoa envolvida pudesse operar eficientemente dentro do ambiente configurado.
