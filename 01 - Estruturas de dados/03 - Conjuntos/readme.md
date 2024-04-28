
CRIAÇÃO e ACESSO AOS DADOS

Criando SET => Um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável.(ex.00)

Acessando os DADOS => Conjuntos em Python não suportam indexação e nem fatiamaneto, caso queira acessar os seus valoes é necessário converter o conjunto para lista(ex.01)

Iterar conjuntos => A forma mais comum para percorrer os dados de um conjunto é utilizando o comando FOR.(ex.02)

Função enumerate => Às vezes é necessário saber qual o índice do objeto dentro do laço FOR. Para isso podemos usar a função ENUMERATE.(ex.02)


METODOS DA CLASSE SET

.{}union => retorna um conjunto contendo a união de todos os conjuntos fornecidos.
.{}intersection => retorna um conjunto contendo os elementos comuns a dois ou mais conjuntos.
.{}difference => retorna um conjunto contendo os elementos presentes no primeiro conjunto, mas ausentes nos outros conjuntos.
.{}symmetric_difference => retorna um novo conjunto contendo elementos presentes em qualquer um dos conjuntos, mas não em ambos.
.{}issubset => verifica se um conjunto é um subconjunto de outro. Retorna True se todos os elementos do primeiro conjunto estão contidos no segundo conjunto, caso contrário, retorna False
.{}issuperset => Python verifica se um conjunto é um superconjunto de outro. Retorna True se o primeiro conjunto contiver todos os elementos do segundo conjunto, caso contrário, retorna False
.{}isdisjoint => verifica se dois conjuntos são disjuntos, ou seja, se não têm elementos em comum. Retorna True se não houver elementos compartilhados, caso contrário, retorna False
.{}add => é utilizado para adicionar algo na lista
.{}clear => é utilizado para limpar todos os elementos existente na lista
.{}copy => é utilizado para copiar/duplicar o set
.{}discard => é utilizado para discartar elementos que o usuário selecionar
.{}pop => é utilizado para remover indices da lista sem declaracao
.{}remove = é utilizado para remover indice já precisando de uma declaracao do que irá retirar
.{}len => é utilizado para ver o tamanho do set
.{}in => é utilizado para ver se tem X elemento dentro da lista