light = input("Jakie jest światło? (red, green, yellow)")

if light == 'red':
    print('Czekaj')

elif light == 'yellow':
    print("Przygotuj się!")

elif light == 'green':
    print("Jedź")
    
else:
        print("Zła wartość")
    
# print("Jedź") if light == 'green' else print("Czekaj!")