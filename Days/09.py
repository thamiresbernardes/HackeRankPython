#runner-up score

n = int(input())  #quantidade de numeros
arr = map(int, input().split())  #array de numeros separados por espaço
print(sorted(set(arr))[-2])

# A função map() serve para aplicarmos uma função a cada um dos elementos passados em lista como argumento a ela.
# A função split() Python, que significa divisão, é um método utilizado para dividir o conteúdo de uma string. string.split(separator, maxsplit)
# A função sorted ordena
# Um set em Python é uma coleção de itens únicos (distintos).
