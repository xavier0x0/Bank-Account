class bankAccount:
    bank_title = "Cool Guy Bank"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number
        self.__routing_number = routing_number

    def deposit(self, amount):
        self.current_balance += amount
        print(f"Deposit of ${amount} complete. New Balance: ${self.current_balance}")

    def withdraw(self, amount):
        if self.current_balance - amount >= self.minimum_balance:
            self.current_balance -= amount
            print(f"Withdrawal of ${amount} complete. New Balance: ${self.current_balance}")
        else:
            print(f"Cannot withdraw ${amount}. Balance would fall below minimum (${self.minimum_balance}).")

    def print_customer_information(self):
        print(f"Customer Name: {self.customer_name}, "
              f"Balance: ${self.current_balance}, "
              f"Bank: {self.bank_title}, "
              f"Account Number: {self._account_number}")

    def get_routing_number(self):
        return self.__routing_number


account1 = bankAccount("Shinji", 1000000, 1000)
account2 = bankAccount("Asuka", 5000000, 1000)
account1.print_customer_information()
account2.print_customer_information()
account1.withdraw(100)
account2.withdraw(500)
account1.print_customer_information()
account2.print_customer_information()
account1.deposit(40000)
account2.deposit(90000)
account1.print_customer_information()
account2.print_customer_information()