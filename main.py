from savings_account import SavingsAccount
from checking_account import CheckingAccount

if __name__ == "__main__":

    checking_user1 = CheckingAccount(
        customer_name="Alice",
        current_balance=1200,
        minimum_balance=100,
        account_number="CHK12345",
        routing_number="1100001",
        monthly_withdrawal_limit=500
    )

    checking_user2 = CheckingAccount(
        customer_name="Bob",
        current_balance=2000,
        minimum_balance=100,
        account_number="CHK67890",
        routing_number="1100002",
        monthly_withdrawal_limit=500
    )

    savings_user1 = SavingsAccount(
        customer_name="Charlie",
        current_balance=3000,
        minimum_balance=50,
        account_number="SAV11111",
        routing_number="2200001",
        interest_rate=0.03
    )

    savings_user2 = SavingsAccount(
        customer_name="Diana",
        current_balance=5000,
        minimum_balance=100,
        account_number="SAV22222",
        routing_number="2200002",
        interest_rate=0.05
    )

    print("---- Initial Information ----")
    checking_user1.print_customer_information()
    checking_user2.print_customer_information()
    savings_user1.print_customer_information()
    savings_user2.print_customer_information()

    print("\n---- Scenario: Checking Account Withdrawals ----")
    checking_user1.withdraw(300)
    checking_user1.withdraw(250)
    checking_user1.deposit(100)

    print("\n---- Scenario: Savings Account Interest ----")
    savings_user1.apply_interest()

    print("\n---- Another scenario for Checking and Savings ----")
    checking_user2.deposit(500)
    checking_user2.withdraw(400)
    savings_user2.withdraw(200)
    savings_user2.apply_interest()

    print("\n---- Final Information ----")
    checking_user1.print_customer_information()
    checking_user2.print_customer_information()
    savings_user1.print_customer_information()
    savings_user2.print_customer_information()

    print("\n(For demonstration) CheckingUser1's Routing Number:", checking_user1.get_routing_number())
