Passo a Passo da Construção
Processamento dos Dados:

Inicialmente, criei uma função chamada carregar_dados, que abre e lê o arquivo CSV usando o módulo csv. Usei defaultdict da biblioteca collections para facilitar a manipulação dos dados, armazenando cada personagem e seus correspondentes amigos em um conjunto (set), o que permite fácil acesso e operações de conjunto.
Para cada linha lida do arquivo, adicionei os personagens aos conjuntos de interações um do outro, garantindo que todas as conexões fossem bidirecionais e corretamente representadas.

Identificação de Amigos em Comum:

Desenvolvi a função encontrar_amigos_em_comum que itera sobre cada par único de personagens, utilizando dois loops aninhados para garantir que todos os pares fossem considerados. Para cada par, calculei a interseção de seus conjuntos de amigos, identificando assim os amigos em comum.
Os resultados, formatados corretamente com TABs e vírgulas para separar os amigos em comum, foram então adicionados a uma lista para posterior gravação em arquivo.

Escrita dos Resultados:

No bloco principal do script, defini os caminhos de entrada e saída para os arquivos, carreguei as interações utilizando a função carregar_dados e encontrei os amigos em comum com encontrar_amigos_em_comum.
Abri o arquivo de saída e usei a função writer do módulo csv para escrever um cabeçalho seguido pelos resultados. Cada linha de resultado foi escrita no formato especificado, garantindo clareza e precisão nos dados de saída.
Execução do Script
Para executar o script, usei o prompt de comando para navegar até o diretório onde o script está localizado e executei o comando python nome_do_script.py.
Verifiquei o arquivo de saída amigos_comuns.csv para validar que os dados estavam corretos.
