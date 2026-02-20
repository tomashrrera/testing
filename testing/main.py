# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    from descuentos.calcular_descuentos import calcular_descuento

    if calcular_descuento(100,10) == 90.0:
        print ('ok')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
