my_friends = ["Csaba", "Kriszta", "Tamás", "Gergő", "Csilla", "Zoli"]

for friend in my_friends:
    if friend == "Gergő":
        continue  # skip this name

    print(f"Hello {friend}")