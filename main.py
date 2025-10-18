import random
symvols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
len_pass = int(input("длинна "))
password = ""
for _ in range(len_pass):
    password += random.choice(symvols)

print(password)