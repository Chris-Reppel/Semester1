colours = {"Chartreuse1": "#7fff00", "AliceBlue": "#f0f8ff", "Aquamarine1": "#7fffd4",
           "BlueViolet": "#8a2be2", "CadetBlue1": "#98f5ff", "CornflowerBlue": "#6495ed",
           "Cyan1": "#00ffff", "DarkOrchid": "#9932cc", "DarkViolet": "#9400d3", "DodgerBlue1": "#1e90ff"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    if colour_name in colours:
        print("The Hex value for \"{}\" is {}".format(colour_name, colours.get(colour_name)))
    else:
        print("Invalid colour")
    colour_name = input("Enter a colour name: ")
