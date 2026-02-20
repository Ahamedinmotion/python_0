def ft_plot_area():
    try:
        len = int(input("Enter length: "))
        wid = int(input("Enter width: "))
    except ValueError:
        print("Invalid Type")
        return None
    print("Plot area: ", len * wid)
