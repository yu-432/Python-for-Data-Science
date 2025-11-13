ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}
# your code here

# List
# list is mutable
ft_list[1] = "World"
# ft_list.pop()
# ft_list.append("World")
# ft_list.insert(1, "42Tokyo")

# Tuple
# tuple is imutable, tuple -> list -> modify -> tuple
temp_list = list(ft_tuple)
temp_list[1] = "Tokyo"
ft_tuple = tuple(temp_list)

# ft_tuple = ft_tuple[:1] + ("42Tokyo",)
# add elemnt to tuple
# ft_tuple += ("42Tokyo",)

# Set
# set is mutable, unique elements, no indexing
ft_set.remove("tutu!")
ft_set.add("Shinjuku")

# to avoid error if element not found
# ft_set.discard("tutu!")
# ft_set.difference_update({"tutu!"})
# ft_set.update({"Shinjuku", "additional Ikebukuro"})

# Dictionary
# dictionary is mutable, key-value pairs
ft_dict["Hello"] = "42Tokyo"
# ft_dict.update({"Hello": "42Nagoya"})

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
