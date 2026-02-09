class Wizard:
    def __init__(self, name, mana, strength):
        self.name = name
        self.__mana = mana        # Жабық атрибут
        self.strength = strength  # Ашық атрибут

    # Сиқыр қолдану әдісі
    def cast_spell(self, cost):
        if cost <= self.__mana:
            self.__mana -= cost
            print(f"{self.name} сиқыр жасады! Манадан {cost} азайды.")
            print(f"Қалған мана: {self.__mana}")
        else:
            print(f"{self.name} үшін жеткілікті мана жоқ! Қажет: {cost}, Қалған: {self.__mana}")

    # Қалған мананы көрсету
    def show_mana(self):
        print(f"{self.name}-ның қалдық манасы: {self.__mana}")


# Пайдаланушыдан мәліметтерді енгізу
name = input("Сиқыршының аты: ")
mana = int(input("Мана деңгейі: "))
strength = int(input("Күш деңгейі: "))

# Сиқыршы объектісін жасау
wizard = Wizard(name, mana, strength)

# Сиқыр қолдану
spell_cost = int(input("Сиқыр жасау үшін қанша мана жұмсалады: "))
wizard.cast_spell(spell_cost)

# Қалған мананы көрсету
wizard.show_mana()



