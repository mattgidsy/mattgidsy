placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

d = {}

for char in placement:
    if char not in d:
        d[char] = 0
    d[char] += 1

keys = list(d.keys())

#arbitrary place to start iterating through the list
min_value = keys[0]

for key in keys:
    if d[key] < d[min_value]:
        min_value = key

print(f"\n The letter '{min_value}' occurs {d[min_value]} times in the sentence: \n \n {placement}\n")