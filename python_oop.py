class Item:
    payrate=0.8
    def __init__(self,name:str,price:int,quantity:int):
        print('INSTANCE WAS CREATED')
        # Run validations to the received arguments
        assert price>=0, f"price {price} ia not greater than 0"
        assert quantity>=0  # we use assert keyword to check validations

        # Assign to self objects
        self.name=name # Assigning the attributes dynamically in __init__
        self.price=price
        self.quantity=quantity

    def calculate_price(self): # methods , self parameter takes object itself as argument i.e item1
        return self.price*self.quantity

item1=Item('NOKIA',900,5) # creating instance of the class i.e object , WHEN WE CREATE THIS INSTANCE THEN PYTHON EXECUTES THE INIT METHOD AUTOMATICALLY
#item1.name='NOKIA'
#item1.price=900
#item1.quantity=5 # we should avoid initializing attributes like that and do dynamic instead 
#x=item1.calculate_price(900,5) # to avoid giving parameters give self.price*self.quantity
x=item1.calculate_price()
print(x)
print(item1.name)
#item2=Item('XOLO','500',9) # to avoid printing of a string multiple times we can validate using price: int in init ,int is the type of the datatype we expect to receive
print(Item.__dict__) # shows all the attributes for class level
print(item1.__dict__) # shows all the attributes for instance level
