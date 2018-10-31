temperature = [14,12,17,5,6]


print(temperature)
temp_fahren = list(map(lambda temp: round((temp * 1.8) + 32, 0), temperature))

print(temp_fahren)

temp_cels = list(map(lambda temp: round((temp - 32) / 1.8, 0), temp_fahren))
print (temp_cels)