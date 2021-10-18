countries_and_capitals = {'Poland': 'Warsaw',
                            'Czechia': 'Prague', 'Germany': 'Berlin'}

try:
    print(2 / 0)
    print(countries_and_capitals['USA'])
except KeyError:
    print("Nie ma klucz")
except  ZeroDivisionError:
    print("Pamiętaj ofermo nie można dzielić przez zero")

print("Jestem ziomek po error error")