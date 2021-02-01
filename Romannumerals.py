class romannum:
    def convert(self, no):
        digit = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romanNO = ['M', 'CM', 'D', 'CD', 'C', 'XC',
                   'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        romandigit = ''
        k = 0
        while no > 0:
            for _ in range(no//digit[k]):
                romandigit += romanNO[k]
                no -= digit[k]
            k += 1
        return romandigit


print(romannum().convert(50))
print(romannum().convert(1000))
print(romannum().convert(1))
print(romannum().convert(5))
print(romannum().convert(6))


##https://www.youtube.com/watch?v=qVIF9g1zq00 helped me with this project 