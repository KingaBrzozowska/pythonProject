class calculator():
   def __init__(self,in_1,in_2):
      self.a=in_1
      self.b=in_2

   def add_vals(self):
      return self.a + self.b

   def multiply_vals(self):
      return self.a * self.b

   def divide_vals(self):
      return self.a/self.b

   def subtract_vals(self):
      return self.a-self.b

input_1 = int(input("Wprowadź pierwszą liczbę: "))
input_2 = int(input("wprowadź drugą liczbę: "))

print(f"Wprowadzone liczby to {input_1} i {input_2} ")

my_instance = calculator(input_1,input_2)
choice=1
while choice!=0:
   print("0. Wyjście")
   print("1. Dodawanie")
   print("2. Odejmowanie")
   print("3. Mnożenie")
   print("4. Dzielenie")
   choice = int(input("Wybierz działanie (0-4): "))

   if choice == 1:
      print(input_1,"+", input_2, "=", my_instance.add_vals())

   elif choice == 2:
      print(input_1,"-", input_2, "=", my_instance.subtract_vals())

   elif choice == 3:
      print(input_1,"*", input_2, "=", my_instance.multiply_vals())

   elif choice == 4:
      print(input_1,"/", input_2, "=", round(my_instance.divide_vals(),2))

   elif choice == 0:
      print("Koniec")

   else:
      print("Błędny wybór!")
   print()