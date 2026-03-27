class Player:
    def __init__(self, name, attack):
        self.nome = name
        self.vida = 100
        self.ataque = attack


j2 = Player("zero210", 40)
print(j2.nome)
print(j2.ataque)