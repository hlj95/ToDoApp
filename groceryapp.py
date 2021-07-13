
shopping_lists = [] 

class ShoppingList: 
  def __init__(self, name, address): 
    self.name = name
    self.address = address 
    self.items = [] 
  
  def add_item(self, item): 
    self.items.append(item)

class Item: 
  def __init__(self, price, quantity): 
    self.price = price 
    self.quantity = quantity 


store = ShoppingList("HEB", "1200")
item = Item(10, 2)


for item in store.items: 
  print(item.price)
try:
  while True: 
      index = 0
      print("1 - Add List")
      print("2 - Add Items")
      print("3 - View All Lists")
      print("4 - Delete A Store")
      print("5 - Delete An Item")
      print("q - Quit")

      choice = int(input("Enter choice: "))
      
      if choice == 1:
          store = input("What store is this list for?")
          address = input("What is this store's address?")
          list = ["Store: " + store, "Adress: " + address]
          shopping_lists.append(list)
            
            
      if choice == 2:
          while index < len(shopping_lists):
            perlist = shopping_lists[index]    
            print(index + 1, perlist)
            index += 1    
          chosenlist = int(input("Which list would you like to add an item to?"))
          item = input("Items to add:")
          new_list = (shopping_lists[chosenlist - 1])
          new_list.append("List: " + item)
          print(index + 1, new_list)
          index += 1   
            
      elif choice == 3:
        while index < len(shopping_lists):
          perlist = shopping_lists[index]
          print(index + 1, perlist)
          index += 1        

      elif choice == 4:
        while index < len(shopping_lists):
          perlist = shopping_lists[index]
          print(index + 1, perlist)
          index += 1        
        storetodelete = int(input("Which store do you want to delete?"))
        del shopping_lists[storetodelete - 1]
        print(shopping_lists)

      elif choice == 5:
        while index < len(shopping_lists):
          perlist = shopping_lists[index]
          print(index + 1, perlist)
          index += 1
        listofitem = int(input("What list do you want to edit?"))
        editlist = shopping_lists[listofitem - 1]
        print(editlist)
        itemtodelete = int(input("Which item do you want to delete?"))
        deleteitem = item[itemtodelete]
        del editlist[deleteitem - 1]
        print(editlist)
        
      else:
          if choice == int():
            print("\nGoodbye")

except ValueError:
  print("Goodbye")