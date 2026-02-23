from fizzbuzz import jugar_fizzbuzz

def test_numero_normal():
    assert jugar_fizzbuzz(1) == "1"

def test_multiplo_de_tres():
    assert jugar_fizzbuzz(3) == "Fizz"

def test_multiplo_de_cinco():
    assert jugar_fizzbuzz(5) == "Buzz"

def test_multiplo_de_tres_y_cinco():
    assert jugar_fizzbuzz(15) == "FizzBuzz"