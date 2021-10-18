# ---Lista---

# names_list =[]
# names_list.append("Kamil")
# names_list.append("Adam")
# names_list.append("Mariusz")
# names_list.append("Wojciech")
# names_list.append("Wojciech")
# # names_list =["Kamil", "Mariusz", "Adam", "Wojciech"]

# # print(names_list)
# # names_list.reverse
# # print(names_list.pop(0))
# # print(names_list.remove("Mariusz"))
# names_list.sort(reverse=True)
# for name in names_list:
#     print(name)

# # print(names_list[0])

# print(names_list.count("Wojciech"))
# print(names_list.count("Marek"))
# print(len(names_list))

# names_list2 =[]
# names_list2.append("Kamil22")
# names_list2.append("Adam22")

# names_list3 = names_list + names_list2
# print(names_list3)

# ---Krotka---

# names_list = ("Marek1", "Marek2", "Marek3")
# person = ("Wojciech", "Jarczak", 23)
# print(names_list)
# print(person)


# ---Set---
# names_set = set() - Pusty set
# names_set = {"Marek1", "Marek1", "Marek2", "Marek3"}
# names_set.add("Kamil")
# print(names_set)

# Merge sets
# name_set3 = names_set.union(names_set2)

countries_and_captials = {"Poland":"Warsaw", "Germany":"Berlin"}
countries_and_captials['Czechia'] = 'Prague'
# print(countries_and_captials)
# for country in countries_and_captials.keys():
#     print(country)
# for capital in countries_and_captials.values():
#     print(capital)
# for country, capital in countries_and_captials.items():
#     print(country + "-" + capital)
print(countries_and_captials["Poland"])  
# if not found gets error
print(countries_and_captials.get("Poland")) 
# if not found gets "None"

if "Poland" in countries_and_captials.keys():
    print("Znaleziono!")
else:
    print("Słabo :(")

print("Poland" in countries_and_captials)