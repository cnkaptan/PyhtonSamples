a = [1, 2, 3, 4, 5]
for k in a:
    print(k, end=" ")

print()

"""
    These iterables are handy because you can read them as much as you wish,
    but you store all the values in memory and this is not always what you want when you have a lot of values.
"""


a = [1, 2, 3, 4, 5]
b = iter(a)

while True:
    try:
        k = next(b)
    except StopIteration:
        break
    print(k, end=" ")

"""
    Yukarıdaki örnekte, ikinci satırda listenin elemanlarını sırasıyla elde etmek için bir iterator oluşturup,
    bunu b değişkenine atadık. Yukarıdaki for döngüsünde, bu işlem for döngüsü tarafından kendiğinden yapılıyordu.
    Daha sonra, 5. satırda, k'yı iterator'dan gelen bir sonraki elemana atadık. Eğer iterator yeni eleman veremiyorsa,
    StopIteration durumu oluşturuyor. Bu durumu catch ile yakalayıp, döngüden çıkıyoruz.
    Iterator'larla ilgili son bir şey;iteratorlar tek kullanımlıktır, bir kere tükendikten sonra,
    aynı  objenin elemanları içinde tekrar gezinmek için, yeni bir iterator'a ihtiyacımız var.
"""