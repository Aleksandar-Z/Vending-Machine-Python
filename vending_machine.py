
class Vending_Machine:
    def __init__(self):
        self.coca_cola = 10
        self.fanta = 10
        self.pepsi = 10
        self.pringles = 10
        self.doritos = 10
        self.m_and_m = 10
        self.oreo = 10
        self.kit_kat = 10
        self.twix = 10
        self.__coca_cola_price = 2
        self.__fanta_price = 2
        self.__pepsi_price = 2
        self.__pringles_price = 5
        self.__doritos_price = 4
        self.__m_and_m_price = 3
        self.__oreo_price = 5
        self.__kit_kat_price = 1
        self.__twix_price = 1

    def get_coca_cola_price(self):
          return self.__coca_cola_price

    def get_fanta_price(self):
          return self.__fanta_price
           
    def get_pepsi_price(self):
          return self.__pepsi_price
           
    def get_pringles_price(self):
          return self.__pringles_price
           
    def get_doritos_price(self):
          return self.__doritos_price
          
    def get_m_and_m_price(self):
          return self.__m_and_m_price
          
    def get_oreo_price(self):
          return self.__oreo_price
          
    def get_kit_kat_price(self):
          return self.__kit_kat_price
          
    def get_twix_price(self):
          return self.__twix_price   


    def set_coca_cola_price(self, x):
      if x != int:
        print("Error")
      else:
          self.__coca_cola_price = x
          return self.__coca_cola_price

    def set_fanta_price(self, x):
      if x != int:
        print("Error")
      else:
          self.__fanta_price = x
          return self.__fanta_price
           
    def set_pepsi_price(self, x):
      if x != int:
        print("Error")
      else:
          self.__pepsi_price = x
          return self.__pepsi_price
           
    def set_pringles_price(self, x):
      if x != int:
        print("Error")
      else:
          self.__pringles_price = x
          return self.__pringles_price
           
    def set_doritos_price(self, x):
      if x != int:
        print("Error")
      else:
          self.__doritos_price = x
          return self.__doritos_price
          
    def set_m_and_m_price(self, x):
      if x != int:
        print("Error")
      else:
          self.__m_and_m_price = x
          return self.__m_and_m_price
          
    def set_oreo_price(self, x):
      if x != int:
        print("Error")
      else:
          self.__oreo_price = x
          return self.__oreo_price
          
    def set_kit_kat_price(self, x):
      if x != int:
        print("Error")
      else:
          self.__kit_kat_price = x
          return self.__kit_kat_price
          
    def set_twix_price(self, x):
      if x != int:
        print("Error")
      else:
        self.__twix_price = x
        return self.__twix_price      
                               

    def fill_the_machine(self):
        # Adding all items to machine and setting amount to 10 for each item
        self.coca_cola  = 10
        self.fanta = 10
        self.pepsi = 10
        self.pringles = 10
        self.doritos = 10
        self.m_and_m = 10
        self.oreo = 10
        self.kit_kat = 10
        self.twix = 10

    def inventory(self):
        # Prints amount for each item in machine
        print(f'Amount of Coca Cola is: {self.coca_cola}\nAmount of Fanta is: {self.fanta}\nAmount of Pepsi is: {self.pepsi}\nAmount of Pringles is: {self.pringles}\nAmount of Doritos is: {self.doritos}\nAmount of M&M is: {self.m_and_m}\nAmount of Oreo is: {self.oreo}\nAmount of Kit Kat is: {self.kit_kat}\nAmount of Twix is: {self.twix}')

    def empty_inventory(self):
        # Empty all items from machine
        self.coca_cola  = 0
        self.fanta = 0
        self.pepsi = 0
        self.pringles = 0
        self.doritos = 0
        self.m_and_m = 0
        self.oreo = 0
        self.kit_kat = 0
        self.twix = 0

    def order(self):
      
      #Ask user to insert mony in machine
      while True:
        try:
          amount_of_money = int(input("Please insert your money: "))
        except Exception as e:
          print("Please try again")
          print(e)
          continue
        break

      # Printing amount of items left in machine and asking for order 
      while True:

        print(f'Please select order from following list:\nAmount of Coca Cola is: {self.coca_cola}\nAmount of Fanta is: {self.fanta}\nAmount of Pepsi is: {self.pepsi}\nAmount of Pringles is: {self.pringles}\nAmount of Doritos is: {self.doritos}\nAmount of M&M is: {self.m_and_m}\nAmount of Oreo is: {self.oreo}\nAmount of Kit Kat is: {self.kit_kat}\nAmount of Twix is: {self.twix}\n')
        
        order = input('Please enter your order: ')
        order = order.lower()

        if order == 'exit':
          print(f"Your change is: {amount_of_money}\nEnjoy your order!")
          break

        #Checking if input mach's any item from list
        elif order == 'coca cola':
          if self.coca_cola > 0:
            if amount_of_money >= self.__coca_cola_price:
              self.coca_cola -= 1
              amount_of_money -= self.__coca_cola_price
              print(f'Amount money left is: {amount_of_money} if you want any oder item please enter your order if not enter "EXIT"\n')
            else:
              print("You don't have enough money for selected item")
          else:
            print('Selected item is out of stock')

        elif order == 'fanta':
          if self.fanta > 0:
            if amount_of_money >= self.__fanta_price:
              self.fanta -= 1
              amount_of_money -= self.__fanta_price
              print(f'Amount money left is: {amount_of_money} if you want any oder item please enter your order if not enter "EXIT"\n')
            else:
              print("You don't have enough money for selected item")
          else:
            print('Selected item is out of stock')

        elif order == 'pepsi':
          if self.pepsi > 0:
            if amount_of_money >= self.__pepsi_price:
              self.pepsi -= 1
              amount_of_money -= self.__pepsi_price
              print(f'Amount money left is: {amount_of_money} if you want any oder item please enter your order if not enter "EXIT"')
            else:
              print("You don't have enough money for selected item")
          else:
            print('Selected item is out of stock')

        elif order == 'pringles':
          if self.pringles > 0:
            if amount_of_money >= self.__pringles_price:
              self.pringles -= 1
              amount_of_money -= self.__pringles_price
              print(f'Amount of money left is: {amount_of_money} if you want any oder item please enter your order if not enter "EXIT"')
            else:
              print("You don't have enough money for selected item")
          else:
            print('Selected item is out of stock')

        elif order == 'doritos':
          if self.doritos > 0:
            if amount_of_money >= self.__doritos_price:
              self.doritos -= 1
              amount_of_money -= self.__doritos_price
              print(f'Amount of money left is: {amount_of_money} if you want any oder item please enter your order if not enter "EXIT"')
            else:
              print("You don't have enough money for selected item")
          else:
            print('Selected item is out of stock')

        elif order == 'm&m':
          if self.m_and_m > 0:
            if amount_of_money >= self.__m_and_m_price:
              self.m_and_m -= 1
              amount_of_money -= self.__m_and_m_price
              print(f'Amount of money left is: {amount_of_money} if you want any oder item please enter your order if not enter "EXIT"')
            else:
              print("You don't have enough money for selected item")
          else:
            print('Selected item is out of stock')

        elif order == 'oreo':
          if self.oreo > 0:
            if amount_of_money >= self.__oreo_price:
              self.oreo -= 1
              amount_of_money -= self.__oreo_price
              print(f'Amount of money left is: {amount_of_money} if you want any oder item please enter your order if not enter "EXIT"')
            else:
              print("You don't have enough money for selected item")
          else:
            print('Selected item is out of stock')

        elif order == 'kit kat':
          if self.kit_kat > 0:
            if amount_of_money >= self.__kit_kat_price:
              self.kit_kat -= 1
              amount_of_money -= self.__kit_kat_price
              print(f'Amount of money left is: {amount_of_money} if you want any oder item please enter your order if not enter "EXIT"')
            else:
              print("You don't have enough money for selected item")
          else:
            print('Selected item is out of stock')

        elif order == 'twix':
          if self.twix > 0:
            if amount_of_money >= self.__twix_price:
              self.twix -= 1
              amount_of_money -= self.__twix_price
              print(f'Amount of money left is: {amount_of_money} if you want any oder item please enter your order if not enter "EXIT"')
            else:
              print("You don't have enough money for selected item")
          else:
            print('Selected item is out of stock')

        else:
          print("Sorry we don't have entered item in our machine, please try entering any item form our list or enter 'EXIT' to leave")