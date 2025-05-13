# Dada a raiz de uma árvore binária, retorne uma lista contendo os nós de cada nível, da esquerda para a direita, nível por nível.
# """Montando a árvore do exemplo:
#        3
#       / \
#      9  20
#         / \
#       15   7"""


from collections import deque

class TreeNode:
    def __init__(self, val=0, esquerda=None, direita=None):
        self.val = val # valor armazenado no nó
        self.left = esquerda # filho à esquerda
        self.right = direita # filho à direita


raiz = TreeNode(3)
raiz.left = TreeNode(9)
raiz.right = TreeNode(20)
raiz.right.left = TreeNode(15)
raiz.right.right = TreeNode(7)

# Lista final de níveis
resultado = []

# Fila para armazenar os nós do nível atual
fila = deque()
fila.append(raiz)

# Enquanto houver nós na fila
while fila:
    nivel = []
    tamanho = len(fila)
    
    for _ in range(tamanho):
        no = fila.popleft()
        nivel.append(no.val)
        if no.left:
            fila.append(no.left)
        if no.right:
            fila.append(no.right)
    
    resultado.append(nivel)

# Mostra o resultado final
print(resultado)  # Saída esperada: [[3], [9, 20], [15, 7]]
