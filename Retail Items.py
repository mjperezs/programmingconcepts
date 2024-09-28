'''
Maria Jose Perez
U77568172
DESCRIPTION: The program prompts the user to enter the retail item and its price and t
hen, gives a summary of the items listed above.


'''

class Retail_Item():


    def __init__(self, item, amount, price):
        self.itemType = item
        self.amount = amount
        self.price = price


    def __str__(self):
        return '%-15s %-10s $%-10.2f' % (self.itemType, self.amount, self.price)

def main():
    item = input('Name of item 1:')
    
    amount = int(input('Amount of item 1:'))
    
    price = float(input('Price of item 1:'))
    
    object_1 = Retail_Item(item, amount, price)
    
    print("\n");
    
    item = input('Name of item 2:')
    
    amount = int(input('Amount of item 2:'))
    
    price = float(input('Price of item 2:'))
    
    object_2 = Retail_Item(item, amount, price)
    
    print("\n")
    
    print('Here is a summary of the items you added:')
    
    print('%-15s %-10s %-10s'%("Item", "Amount", "Price"))
    
    print("---------------------------------------")
    
    print(object_1)
    
    print(object_2)

if __name__ == '__main__':
    main()
