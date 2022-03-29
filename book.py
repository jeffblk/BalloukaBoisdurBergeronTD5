
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
    
    def set_quantity(self, quantity):
        self.__quantity = quantity
        
    def __lt__(self, other):
        return other and self.__price <= other.price()
        # Return, if the other object exists, whether the price of the current object is lower than the price of the
        # other one The three following are getters since the attributesare private

    def Execute(self,counterparty): #Buy or Sell some (or the total) of our quantity
        if counterparty.quantity() > self.__quantity: #if the couterparty have (or want) more than we need
            counterparty.set_quantity(counterparty.quantity()- self.__quantity)
            self.__quantity = 0 #Our actual order is fully executed
        else: #Our order isn't fully executed
            self.__quantity -= counterparty.quantity()
            counterparty.set_quantity(0)
    
    def __str__(self):
        return "\t"+ str(self.__type)+" "+str(self.__quantity)+"@"+str(self.__price)+" id = "+str(self.__id)


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
       for sell in self.sell_orders:
           for buy in self.buy_orders:

               if sell.price() <= buy.price() and sell.quantity() != 0: #Si on trouve un acheteurs a notre prix ou plus
                   #on vend le plus possible
                   trade_quantity = min(sell.quantity(),buy.quantity())
                   trade_price = buy.price()
                   sell.Execute(buy) #On execute       
                   print("EXECUTE " + str(trade_quantity) + " @ " + str(trade_price) + " ON " + self.name )
                   self.remove_executed()

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
    
    
    def remove_executed(self): #We remove all fully executed order
        for order in self.sell_orders:
            if order.quantity() == 0:
                self.sell_orders.remove(order)
        for order in self.buy_orders:
            if order.quantity()==0:
                self.buy_orders.remove(order)
                
    
    
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
            print(self.sell_orders[i])
        
        for j in range(len(self.buy_orders)):
            print(self.buy_orders[j])
        
        print("-------------------------")
        
  
    
    def create_dataframe(self):
        # Contains "SELL" if it is a selling order and "BUY" if not
        action_list = []

        # The list of all the information
        quantity_list = []
        price_list = []
        id_list = []
      

        # Creating the lists (with all the data)
        for element in self.buy_orders:
            action_list.append(element.type())
             
            quantity_list.append(element.quantity())
            price_list.append(element.price())
            id_list.append(element.id())
            
        for element in self.sell_orders:
            action_list.append(element.type())
             
            quantity_list.append(element.quantity())
            price_list.append(element.price())
            id_list.append(element.id())

        # Coverting the lists to a panda dataframe
        data_to_be_converted = {  'ID': id_list, 'Action': action_list, 'Quantity': quantity_list,
                                'Price': price_list}
        df = pd.DataFrame(data=data_to_be_converted)
        return df


