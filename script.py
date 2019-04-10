#ShoppingBasket
INVENTORY = [["A0001", 12.99], ["A0002", 3.99], ...]

class Goodies(object):
    def __init__(self, name, price):
        self.name = object_name
        self.price = object_price



class Basket(object): 

    def __init__(self):
        self.total = dict()

    def __init__ (self, new, scan):
        self.new = basket
        self.scan = content_basket
        
    
    
    def voucherone(self): #buyonegetonefree
        if self.total == 3:
            new_value = del self.total[-1] 
            return new_value
            #remove last item
        return self.total
        else:
            pass
        
    def rabatt(self): #10% Rabatt
        for sum in self.total 
            discount = 10 * self.total // 100
            new_total = self.total - discount
            return new_total


