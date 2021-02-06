import hashlib
import sys

door_id = "ffykfhsq"
#door_id = "abc"
running_num = 0
passbuild = {}
password = ['-', '-', '-', '-', '-', '-', '-', '-' ]

while len(passbuild) < 8:
    test = door_id + str(running_num)
    hashed = hashlib.md5(test.encode()).hexdigest()
    if running_num % 1000 == 0:
        sys.stdout.write("password: {} cracking hash: {} \r".format("".join(password),hashed))
        sys.stdout.flush()
    if hashed.startswith("00000"):
        place = hashed[5]
        char = hashed[6]
        if place.isdigit() and int(place) > -1 and int(place) < 8:
            if int(place) not in passbuild:
                passbuild[int(place)] = char
                password[int(place)] = char
    running_num += 1

sys.stdout.write("password: {} \r".format("".join(password)))
sys.stdout.flush()
print("password: {} \r".format("".join(password)))