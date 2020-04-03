

def prob_same_bday(num):
    prod = 1
    for i in range(num):
        prod *= ((365-(i))/365)
    return 1 - prod

print(prob_same_bday(35))