card = 9232416
door = 14144084
number = 20201227

def get_loop(public_key):
    val = 1
    i = 0
    while val != public_key:
        val = (val * 7) % number
        i += 1
    return i
    
def get_encryption(loop, public_key):
    val = 1
    for _ in range(loop):
        val = (val * public_key) % number
    return val

card_loop = get_loop(card)
door_loop = get_loop(door)

ans = get_encryption(card_loop, door)
assert ans == get_encryption(door_loop, card)
print(ans)
