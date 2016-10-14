generator = (x*x*x for x in range(5))

"""
    Generators are iterators, but you can only iterate over them once.
    It's because they do not store all the values in memory, they generate the values on the fly:
"""
"""
    ilk satırda bir generator oluşturup, bunu generator isimli bir değişkene atadık.
    Şimdi bunu, istediğimiz gibi for döngüsünde kullanabiliriz.
    Burada dikkat edilmesi gereken nokta, 0,1,8 gibi değerlerin,
    ilk satırda oluşturulmamış olması. Bu değerler, for döngüsünde sıraları geldiklerinde oluşup,
    işleri bittikten sonra hafızadan siliniyorlar. Genel olarak generatorların olayı bu kadar.
"""
for k in generator:
   print(k)

"""
Ekrana şunu basar:
0
1
8
27
64
"""
for k in generator:
   print(k)
"""
Ekrana hiçbir şey basılmaz, çünkü generator'u bir kere kullandık ve bitti.
"""