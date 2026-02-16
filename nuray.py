class Wizard:
    def __init__(self, name, mana, strength):
        self.name = name
        self.__mana = mana
        self.strength = strength

    def cast_spell(self, cost):
        if cost <= self.__mana:
            self.__mana -= cost
            print(f"{self.name} сиқыр жасады! Манадан {cost} азайды.")
            print(f"Қалған мана: {self.__mana}")
        else:
            print(f"{self.name}-да жеткілікті мана жоқ! Қажет: {cost}, Қалған: {self.__mana}")

    def show_mana(self):
        print(f"{self.name}-ның қалдық манасы: {self.__mana}")

    def get_mana(self):
        return self.__mana


class Game:
    def __init__(self):
        self.players = []

    def add_wizard(self, wizard):
        self.players.append(wizard)
        print(f"{wizard.name} ойынға қосылды.")

    def player_cast(self, wizard_index, spell_cost):
        if 0 <= wizard_index < len(self.players):
            wizard = self.players[wizard_index]
            wizard.cast_spell(spell_cost)
        else:
            print("Қате: дұрыс ойыншы индексін көрсетіңіз.")


name = input("Сиқыршының аты: ")
mana = int(input("Мана деңгейі: "))
strength = int(input("Күш деңгейі: "))

wizard = Wizard(name, mana, strength)

game = Game()
game.add_wizard(wizard)

spell_cost = int(input("Сиқыр жасау үшін қанша мана жұмсалады: "))
game.player_cast(0, spell_cost)

wizard.show_mana()
