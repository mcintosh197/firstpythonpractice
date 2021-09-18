def main():
   # listExample()
   # dictionaryExample()
   dictionariesAndLists()

def listExample():

   students = ["Alastair", "Cameron", "Colin", "Conal", "Conor"]
  
   for student in students:
       print(student)

def dictionaryExample():

   favouriteFoods = {
       "Dylan Smith": "Beans",
       "Jack McGuigan": "Spaghetti Bolognese",
       "Jack McNaughton": "Ribs"
   }

   print(f"Dylan likes { favouriteFoods['Dylan Smith'] }")
   print(f"Jack McGuigan likes { favouriteFoods['Jack McGuigan'] }")
   print(f"Jack McNaughton likes { favouriteFoods['Jack McNaughton'] }")


def dictionariesAndLists():

   favouriteFoods = {
                   "Dylan Smith": [
                       "Beans",
                       "Lasagne",
                       "HP Sauce"
                   ],
                   "Jack McGuigan": [
                       "Spaghetti Bolognese",
                       "Steak",
                       "Pizza"
                   ],
                   "Jack McNaughton": [
                       "Ribs",
                       "Spaghetti Carbonara",
                       "Burgers"
                   ]
               }

   print("Dylan Likes:")

   dylansFavFoodsList = favouriteFoods["Dylan Smith"]
   #print(type(dylansFavFoodsList))
   for food in dylansFavFoodsList:
       print(food[1])

   print("Jack McGuigan Likes:")
  
   jack1FavFoodList = favouriteFoods["Jack McGuigan"]
   for food in jack1FavFoodList:
       print(food)

   print("Jack McNaughton Likes:")
   jack2FavFoodList = favouriteFoods["Jack McMcNaughton"]

   for food in jack2FavFoodList:
       print(food)


if __name__ == "__main__":  # if this is the file you pressed run on
   main()