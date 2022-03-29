
import itertools
import pandas as pd

class Order:
    def __init__(self, type, quantity, price, id):
        self.type = type
        self.quantity = quantity
        self.price = price
        self.id =  id
        
    def type(self):
        return self.type
        
    def quantity(self):
        return self.quantity

    def price(self):
        return self.price
    
    def id(self):
        return self.id

    def Execute(self,counterparty): #Buy or Sell some (or the total) of our quantity
        if counterparty.quantity > self.quantity: #if the couterparty have (or want) more than we need
            counterparty.quantity -= self.quantity
            self.quantity = 0 #Our actual order is fully executed
        else: #Our order isn't fully executed
            self.quantity -= counterparty.quantity
            counterparty.quantity = 0
    
    


class Book:

    def __init__(self, name):
        self.name = name  # The name of the ordered book
        self.buy_orders = []  #buy orders
        self.sell_orders = []  #sell orders
        self.id_iter = 1

    def name(self):  # Getter
        return self.name
    
    
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
    def insert_buy(self, quantity, price):
        self.buy_orders.append(Order("BUY",quantity, price,self.id_iter))
        print("--- Insert BUY ", str(quantity), "@", str(price), " id =", str(self.id_iter)," on ", str(self.name))
        self.execute_order() #We try to execute the new order
        self.print_infos() #e print the order book
        self.id_iter += 1
        
    def insert_sell(self, quantity, price):
        self.sell_orders.append(Order("SELL",quantity, price,self.id_iter))
        print("--- Insert SELL ", str(quantity), "@", str(price), " id =", str(self.id_iter)," on ", str(self.name))
        self.execute_order() #We try to execute the new order
        self.print_infos() #e print the order book
        self.id_iter += 1
    
    
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
        
        print("Book on ", str(self.name))
        
        for i in range(len(self.sell_orders)):
            print('\tSELL ',self.sell_orders[i].quantity(),'@',self.sell_orders[i].price(),' id = ',self.sell_orders[i].id())
        
        for j in range(len(self.buy_orders)):
            print('\tBUY ',self.buy_orders[j].quantity(),'@',self.buy_orders[j].price(),' id = ',self.buy_orders[j].id())
        
        print("-------------------------")



def main():
    book = Book("TEST")
    book.insert_buy(10, 10.0)


if __name__ == "__main__":    
    main()
