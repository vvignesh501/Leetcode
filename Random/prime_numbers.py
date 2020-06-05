class PrimeNumber:
    def getPrimeNos(self, num:int):
        prime_nos = []
        for x in range(2, num):
            for y in range(2, x):
                if x % y == 0:
                    break
            else:
                prime_nos.append(x)
        return prime_nos


g = PrimeNumber()
num = int(input("Please enter a number:"))
out = g.getPrimeNos(num)
print(str(out).replace('[','').replace(']',''))