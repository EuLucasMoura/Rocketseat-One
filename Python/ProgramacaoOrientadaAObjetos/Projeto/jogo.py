class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.nome = nome
        self.vida = vida
        self.nivel = nivel
    
    def get_nome(self):
        return self.nome
    
    def get_vida(self):
        return self.nome
    
    def get_nivel(self):
        return self.nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.nome} \nVida: {self.vida} \nNivel: {self.nivel}"
    
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"
        
    
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo) -> None:
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\ntipo: {self.get_tipo()}\n"

    def get_tipo(self):
        return self.__tipo
    
heroi = Heroi(nome="Guerreiro", vida=25,  nivel=5, habilidade="Ataque Forte")
print(heroi.exibir_detalhes())

inimigo = Inimigo(nome="Hollow", vida=12, nivel=2, tipo="Normal")
print(inimigo.exibir_detalhes())