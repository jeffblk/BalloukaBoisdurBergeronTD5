
"""
Created on Tue Mar 22 15:22:21 2022

@author: arthu
"""
import itertools


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
