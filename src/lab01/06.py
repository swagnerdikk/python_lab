kolich = int(input("in_1: "))
ochno_ = 0
zaochno_ = 0
for i in range(kolich):
    ychastnik = input(f"in_{i+2}: ")
    if "True" in ychastnik:
        ochno_ = ochno_ + 1
    else:
        zaochno_ = zaochno_ + 1
print(f"out: {ochno_} {zaochno_}")
