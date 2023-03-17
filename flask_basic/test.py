def latin(name):
    if name[-1] == "y":
        name = name[:-1] + "iful"
        return name
    else:
        name += "y"
        return name
