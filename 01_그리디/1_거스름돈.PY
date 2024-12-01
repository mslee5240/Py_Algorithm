n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin  # count = count + (n // coin)
    n %= coin   # n = n % coin

print(count)