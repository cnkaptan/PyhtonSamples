# karsilastirma operatorlerinin hepsi tuple ve diger collectionlarda calisir
# ilk elemana bakar ayniysa ikinciye gecer taki farkli elemani bulana kadar

print (0, 1, 2) < (5, 1, 2)

print (0, 1, 20000) < (0, 2, 0)

print ('Jones', "Sally") < ("Jones", "Sam")

print ("Jones", 'Sally') > ("Adams", "Sam")
