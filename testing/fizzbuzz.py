def jugar_fizzbuzz(numero):

    if numero % 3 == 0 and numero % 5 == 0:
        return 'FizzBuzz'
    elif numero % 5 == 0:
        return 'Buzz'
    elif numero % 3 == 0:
        return 'Fizz'

    return str(numero)

if __name__ == '__main__':
    for i in range(1, 101):
        print(jugar_fizzbuzz(i))