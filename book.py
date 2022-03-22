# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 15:22:21 2022

@author: jeffb
"""

class Order:
    def __init__(self, quantity, price):
        self.__quantity = quantity
        self.__price = price
        
    def quantity(self):
        return self.__quantity

    def price(self):
        return self.__price


class Book:
    def __init__(self, name):
        self.__name = name  # The name of the ordered book
        self.buy_orders = []  #buy orders
        self.sell_orders = []  #sell orders

    def name(self):  # Getter
        return self.__name

    # Inserting into the order book new orders
    def insert_buy(self, quantity, price):
        self.buy_orders.append(Order(quantity, price))

    def insert_sell(self, quantity, price):
        self.sell_orders.append(Order(quantity, price))
        
    def print_infos(self, sell):
        if(sell):
            print("--- Insert SELL ", self.sell_orders[-1].quantity(), "@", self.sell_orders[-1].price(), " id =", self.sell_orders[-1].id()," on ", self.__name)
        else :
            print("--- Insert BUY ", self.buy_orders[-1].quantity(), "@", self.buy_orders[-1].price(), " id =", self.buy_orders[-1].id()," on ", self.__name)
        self.sort_book()

        print("Book on ", self.__name)

        for i in range(len(self.sell_orders)):
            print("         SELL ", self.sell_orders[i].quantity(), "@", self.sell_orders[i].price(), " id =", self.sell_orders[i].id())
        for j in range(len(self.buy_orders)):
            print("         BUY ", self.buy_orders[j].quantity(), "@", self.buy_orders[j].price(), " id =", self.buy_orders[j].id())
        print("------------------------")