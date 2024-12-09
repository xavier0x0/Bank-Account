from bank_account import bankAccount

class CheckingAccount(bankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number,
                 monthly_withdrawal_limit=1000):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.monthly_withdrawal_limit = monthly_withdrawal_limit
        self.amount_withdrawn_this_month = 0

    def withdraw(self, amount):
        if self.amount_withdrawn_this_month + amount > self.monthly_withdrawal_limit:
            print(f"Withdrawal denied. Monthly limit of ${self.monthly_withdrawal_limit} exceeded.")
            return

        before_balance = self.current_balance
        super().withdraw(amount)

        if self.current_balance < before_balance:
            self.amount_withdrawn_this_month += amount
