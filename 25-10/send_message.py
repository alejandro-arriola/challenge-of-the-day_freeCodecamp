from functools import reduce

def send_message(route):
    return round(reduce(lambda total, jump: total + (jump / 300000) + 0.5, route, -0.5), 4)
    
print(send_message([10000, 21339, 50000, 31243, 10000])) #return 2.4086