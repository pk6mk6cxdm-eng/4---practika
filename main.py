class Client:
    def __init__(self, name, account_number, initial_balance):
        self.name = name
        self.account_number = account_number
        self.__balance = initial_balance  # Жабық өріс

    # Ақша қосу әдісі
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} сом ақша қосылды.")
        else:
            print("Қосылатын ақша сомасы дұрыс емес!")

    # Ақша алу әдісі
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} сом ақша алынды.")
        else:
            print("Соманы алу мүмкін емес, баланс жеткіліксіз немесе дұрыс емес!")

    # Соңғы балансын шығару
    def show_balance(self):
        print(f"Қазіргі баланс: {self.__balance} сом")


# Пайдаланушыдан мәліметтерді енгізу
name = input("Клиенттің аты: ")
account_number = input("Шот нөмірі: ")
initial_balance = float(input("Бастапқы баланс: "))

# Клиент объектісін жасау
client = Client(name, account_number, initial_balance)

# Ақшаны қосу
amount_to_deposit = float(input("Қосқыңыз келетін ақша сомасы: "))
client.deposit(amount_to_deposit)

# Ақшаны алу
amount_to_withdraw = float(input("Алатын ақша сомасы: "))
client.withdraw(amount_to_withdraw)

# Соңғы баланс
client.show_balance()

