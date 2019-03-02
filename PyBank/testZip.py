prices = [30.4, 32.5, 31.7, 31.2, 32.7, 34.1, 35.8, 37.8, 36.3, 36.3, 35.6]

changes = []
for a, b in zip(prices[::1], prices[1::1]):
    change = b-a
    changes.append(change)

print(changes)