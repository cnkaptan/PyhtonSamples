"""
    yield deyimi, return deyimi gibi fonksiyonlarda kullanılır, ancak, fonksiyon bir generator döndürür.
"""

"""
    Yield is a keyword that is used like return, except the function will return a generator.
    it's handy when you know your function will return a huge set of values that you will only need to read once.
"""
def creategeneratorSquare(l):
    for x in l:
        yield x * x


generator = creategeneratorSquare([1, 2, 3, 4, 5])

for k in generator:
    print(k)

"""
Ekrana şunu basar:
1
4
9
16
25
"""

"""
    Yukarıdaki kod parçacığında, creategeneratorSquare isimli bir fonksiyon oluşturduk.
    Bu fonksiyonun, normal fonksiyonlardan farkı, bir generator döndürmesi.
    Bu fonksiyonu çağrıdığımızda, normal fonksiyonlardan beklediğimiz gibi, fonksiyonun gövdesi çalışmıyor,
    bunun yerine fonksiyon bir generator döndürüyor. Bu generator for döngüsü içinde kullanıldığında,
    fonksiyon içinde yazdığımız kod, yield görene kadar çalışıyor. Burada, yield deyimi "x * x" döndürüyor ve beklemeye başlıyor.
    Daha sonra,12. satırdaki döngü, bir sonraki elemanı istedikçe, beklemedeki kod bloğu tekrar yield görene kadar çalışıp,
    yield gördüğünde sıradaki elemanı döndürüyor. Böylece, bu kod bloğu tamamlanıncaya kadar,
    12. satırdaki for döngüsü k'ya farklı değerler atayıp, bunları ekrana bastırıyor.
"""


def fibogenerator():
    a, b = 1, 1
    while True:
        yield b
        a, b = b, a + b


for k in fibogenerator():
    if k > 10000000:
        print(k)
        break

"""
Ekrana şunu basar:
14930352
"""
