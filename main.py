#class aderbejyan:
#    populasyon = 500
#    def salam(self):
#        print("aderbejyan dan salamlar")
#    
#    def __init__(self):
#        pass
#        #self.populasyon = 100
#        #self.populasyon = 200
#
#
#ulke = aderbejyan()
#print(ulke)

def faktoriyel(n):
    k = 1
    for i in range(1, n+1):
        k = k*i


    return k




l = int(input("sayı giriniz: "))
print(faktoriyel(l))


def faktoriyela(m):
    if m < 1:
        return 1
    return m * faktoriyela(m - 1)




y = int(input("sayı giriniz: "))
print(faktoriyel(y))