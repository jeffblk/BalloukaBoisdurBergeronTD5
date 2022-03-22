
import itertools

class Order:
    id_iter = itertools.count()
    
    def __init__(self, quantity, price):
        self.__quantity = quantity
        self.__price = price
        self.__id =  next(self.id_iter) +1
        
    def quantity(self):
        return self.__quantity

    def price(self):
        return self.__price
    
    def id(self):
        return self.__id


class Book:
    def __init__(self, name):
        self.__name = name  # The name of the ordered book
        self.buy_orders = []  #buy orders
        self.sell_orders = []  #sell orders
        self.executed_orders = []
        

    def name(self):  # Getter
        return self.__name

    # Inserting into the order book new orders
    def insert_buy(self, quantity, price,id):
        self.print_infos(True, quantity, price, id)
        self.buy_orders.append(Order(quantity, price))

    def insert_sell(self, quantity, price,id):
        self.print_infos(False, quantity, price, id)
        self.sell_orders.append(Order(quantity, price))

    def sort_b(self):
        self.buy_orders.sort()
        self.buy_orders.reverse()
        self.sell_orders.sort()
        self.sell_orders.reverse()
        

    def print_infos(self, buy,quantity,price,id):
        self.sort_book()
        
        if(buy):
            print("--- Insert BUY "+quantity, "@", price, " id =", id," on ", self.__name+"\n")
        else :
            print("--- Insert SELL " + quantity + "@"+ price, " id =", id," on ", self.__name+"\n")
            
        print("Book on ", self.__name)

        for i in range(len(self.sell_orders)):
            print("          SELL "+ self.sell_orders[i].quantity()+ "@"+ self.sell_orders[i].price() + " id =", self.sell_orders[i].id()+"\n")
        for j in range(len(self.buy_orders)):
            print("          BUY "+ self.buy_orders[j].quantity()+ "@"+ self.buy_orders[j].price()+ " id =", self.buy_orders[j].id()+"\n")
        print("-------------------------")

