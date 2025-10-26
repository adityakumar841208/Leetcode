class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def _valid_account(self, account: int) -> bool:
        return 1 <= account <= len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self._valid_account(account1) or not self._valid_account(account2):
            return False
        if self.balance[account1 - 1] < money:
            return False

        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._valid_account(account):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._valid_account(account) or self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)