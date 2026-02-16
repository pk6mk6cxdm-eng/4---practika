class Client:
    def __init__(self, name, account_number, initial_balance):
        self.name = name
        self.account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} теңге ақша қосылды.")
        else:
            print("Қосылатын ақша суммасы дұрыс емес!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} теңге ақша алынды.")
        else:
            print("Ақшаны алу мүмкін емес, баланс жеткіліксіз немесе дұрыс емес!")

    def show_balance(self):
        print(f"{self.name}-ның қазіргі балансы: {self.__balance} теңге")

    def get_balance(self):
        return self.__balance


class Bank:
    def __init__(self):
        self.clients = []

    def add_client(self, client):
        self.clients.append(client)
        print(f"{client.name} банкке қосылды.")

    def transfer(self, from_client, to_client, amount):
        if from_client.get_balance() >= amount:
            from_client.withdraw(amount)
            to_client.deposit(amount)
            print(f"{amount} теңге {from_client.name}-дан {to_client.name}-ға аударылды.")
        else:
            print("Аударым жасау мүмкін емес, жеткілікті ақша жоқ.")


name = input("Клиенттің аты: ")
account_number = input("Шот нөмірі: ")
initial_balance = float(input("Бастапқы баланс: "))

client = Client(name, account_number, initial_balance)

bank = Bank()
bank.add_client(client)

amount_to_deposit = float(input("Қосқыңыз келетін ақша суммасы: "))
client.deposit(amount_to_deposit)

amount_to_withdraw = float(input("Алатын ақша суммасы: "))
client.withdraw(amount_to_withdraw)

client.show_balance()
