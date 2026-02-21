def ft_count_harvest_iterative():
    while True:
        try:
            days = int(input("Days until harvest: "))
        except ValueError:
            print("Invalid Value")
            continue
        if days < 0:
            print("Invalid Argument: Negative")
            continue
        for i in range(1, days + 1):
            print(f"Day {i}")
        break
