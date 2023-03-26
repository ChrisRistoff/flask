class Bank():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_amount(self):
        while True:
            try:
                amount = int(input("Enter amount: "))
            except ValueError:
                print("Please enter a valid amount")
                continue
            if amount < 0:
                print("Please enter a valid amount")
                continue
            return amount


    def deposit(self):
        self.balance += self.get_amount()
        return self.balance


    def withdraw(self):
        amount = self.get_amount()
        if self.balance < amount:
            print("Insufficient funds")
            return self.balance
        else:
            self.balance -= amount
            return self.balance


    def choice_prompt(self):
        choice = ""
        valid_choices = ["D", "W", "B", "Q"]
        while choice not in valid_choices:
            choice = input("Enter D for deposit, W for withdraw, B "
                           +"for balance, Q to quit: ").upper()
        return choice


    def __repr__(self):
        return f"{self.name} has a balance of {self.balance}"


    def main(self, bank):
        while True:
            choice = bank.choice_prompt()
            if choice == "D":
                bank.deposit()
                print(f"your new balance is {bank.balance}")
            elif choice == "W":
                bank.withdraw()
                print(f"your new balance is {bank.balance}")
            elif choice == "B":
                print(bank.__repr__())
            elif choice == "Q":
                break

if __name__ == "__main__":
    bankomat = Bank("Kris", 0)
    bankomat.main(bankomat)
