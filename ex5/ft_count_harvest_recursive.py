def print_days_recursive(current, days):
    if current > days:
        return
    print(f"Day {current}")
    print_days_recursive(current + 1, days)


def ft_count_harvest_recursive():
    while True:
        try:
            days = int(input("Days until harvest: "))
        except ValueError:
            print("Invalid value")
            continue
        if days < 0:
            print("Invalid argument: negative")
            continue
        break
    print_days_recursive(0, days)
