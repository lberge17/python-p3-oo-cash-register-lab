#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount = 0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = None
    
    def add_item(self, item, price, quantity = 1):
        self.total += price * quantity
        i = 0
        self.last_transaction = [item, price, quantity]
        while quantity > i:
          self.items.append(item)
          i += 1
    
    def apply_discount(self):
        if self.discount:
            self.total = self.total * (100 - self.discount) / 100
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction[1] * self.last_transaction[2]
        i = 0
        while i < self.last_transaction[2]:
          del self.items[-1]
          i += 1

