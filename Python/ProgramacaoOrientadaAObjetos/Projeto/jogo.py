import random
class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
    
    
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.__nome} \nVida: {self.__vida} \nNivel: {self.__nivel}"
    
    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0    

    def ataque_normal(self, alvo):
        dano = self.__nivel * random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        self.receber_dano(dano)
        print(f"{self.get_nome()} atacou  {alvo.get_nome()} e causou {dano} de dano!")




class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"
        
    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)
        alvo.receber_dano(dano)
        print(f"{self.get_nome()} usou a habilidade especial em {alvo.get_nome()} e causou {dano} de dano!")
    
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo) -> None:
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\ntipo: {self.get_tipo()}\n"

    def get_tipo(self):
        return self.__tipo
    

class Jogo:
    def __init__(self) -> None:
        self.heroi = Heroi(nome="Guerreiro", vida=200,  nivel=5, habilidade="Ataque Forte")
        self.inimigo = Inimigo(nome="Hollow", vida=100, nivel=2, tipo="Normal")
    
    def iniciar_batalha(self):
        print("===Iniciando batalha!===")
        
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\n===Detalhes dos personagens!===")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar...")
            escolha = input("Escolha: ")
            print("\n1 - Ataque normal \n2 - Ataque especial \n")

            if escolha == '1':
                self.heroi.ataque_normal(self.inimigo)

            elif escolha == '2':
                self.heroi.ataque_especial(self.inimigo)
            
            else:
                print("Escolha inválida! Escolha novamente.")

            if self.inimigo.get_vida() > 0:
                self.inimigo.ataque_normal(self.heroi)

        if self.heroi.get_vida() > 0:
            print("\n Parabéns! Você venceu a batalha.")
        else:
            print("\n Você foi derrotado!")

jogo = Jogo()
jogo.iniciar_batalha()