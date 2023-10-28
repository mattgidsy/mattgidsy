
rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
num_rainy_months_lst = list()

rainfall_mi_lst = rainfall_mi.split(", ")

for n in rainfall_mi_lst:
    n = float(n)
    if n > 3:
        num_rainy_months_lst.append(n)

num_rainy_months = len(num_rainy_months_lst)

print(num_rainy_months)