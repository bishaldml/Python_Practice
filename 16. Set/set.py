utensils = ["fork","spoon","knife"]
dishes = ["bowl","plate","cup","knife"]

utensils.append("napkin")
#utensils.remove("fork")
#utensils.clear()

utensils.extend(dishes)

for i in utensils:
    print(i)

# Set Methods
print(utensils.difference(dishes))