food = ["Daal","Bhat","Terkari","Achar"]

food[2] = "Masu"

food.append("Papar")
food.insert(0,"cake")
food.remove("Daal")
food.pop()  #remove last item
# food.clear()   #clear list
 
for i in food:
    print(i)