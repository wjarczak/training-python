countries_and_capitals = {'Poland': 'Warsaw',
                            'Czechia': 'Prague', 'Germany': 'Berlin'}

try:
    print(2 / 2)
    print(countries_and_capitals['USA'])
except KeyError:
    print("Nie ma klucz")
except  ZeroDivisionError:
    print("Pamiętaj ofermo nie można dzielić przez zero")

finally:
    print('jest git')

print("Jestem ziomek po error error")