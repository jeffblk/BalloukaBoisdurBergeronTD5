
import itertools
import pandas as pd

class Order:
    def __init__(self, type, quantity, price, id):
        self.__type = type
        self.__quantity = quantity
        self.__price = price
        self.__id =  id
        
    def type(self):
        return self.__type
        
    def quantity(self):
        return self.__quantity

    def price(self):
        return self.__price
    
    def id(self):
        return self.__id

    def Execute(self,counterparty): #Buy or Sell some (or the total) of our quantity
        if counterparty.quantity > self.quantity: #if the couterparty have (or want) more than we need
            counterparty.quantity -= self.quantity
            self.quantity = 0 #Our actual order is fully executed
        else: #Our order isn't fully executed
            self.quantity -= counterparty.quantity
            counterparty.quantity = 0
    
    


class Book:

    def __init__(self, name):
        self.__name = name  # The name of the ordered book
        self.__buy_orders = []  #buy orders
        self.__sell_orders = []  #sell orders
        self.__id_iter = 0

    def name(self):  # Getter
        return self.__name
    
    
    def execute_order(self): #On execute tous nos ordres executables
       #check si nos ordres peuvent s'executer
       for i in range(len(self.sell_orders)):
           for j in range(len(self.buy_orders)):
               if self.sell_orders[i].price <= self.buy_orders[j].price: #Si on trouve un acheteurs a notre prix ou plus
                   #on vend le plus possible
                   trade_quantity = min(self.sell_orders[i].quantity,self.buy_orders[j].quantity)
                   trade_price = self.buy_orders[j].price
                   self.sell_orders[i].Execute(self.buy_orders[j]) #On execute
                   self.remove_executed()
                   print("EXECUTE " + trade_quantity + " @ " + trade_price + " ON " + self.__name )

    # Inserting into the order book new orders
    def insert_order(self, type, quantity, price):
        if type == "BUY":
            self.print_infos("BUY", quantity, price, id_iter)
            self.buy_orders.append(Order("BUY",quantity, price,id_iter)
                                   
        else:
            self.print_infos("SELL", quantity, price, id)
            self.sell_orders.append(Order("SELL",quantity, price,id_iter))
          
        print("--- Insert " + type + " " + quantity, "@", price, " id =", id," on ", self.__name+"\n")
        self.execute_order() #We try to execute the new order
        self.print_infos() #e print the order book
        id_iter += 1


    
    def remove_executed(self): #We remove all fully executed orders
        for i in range(len(self.sell_orders)):
            if self.sell_orders[i] == 0:
                self.sell_orders.remove(self.sell_orders[i])
        for j in range(len(self.buy_orders)):
            if self.buy_orders[j]==0:
                self.buy_orders.remove(self.buy_orders[j])
                
    
    
    def print_infos(self): #Print the orderbook
        
        #We need to sort them by price then by id :
        #-------FALSE
        self.buy_orders.sort() 
        self.buy_orders.reverse()
        self.sell_orders.sort()
        self.sell_orders.reverse()
        #-------------
        
        print("Book on ", self.__name)
        for i in range(len(self.sell_orders)):
            print("          SELL "+ self.sell_orders[i].quantity()+ "@"+ self.sell_orders[i].price() + " id =", self.sell_orders[i].id()+"\n")
        for j in range(len(self.buy_orders)):
            print("          BUY "+ self.buy_orders[j].quantity()+ "@"+ self.buy_orders[j].price()+ " id =", self.buy_orders[j].id()+"\n")
        print("-------------------------")

