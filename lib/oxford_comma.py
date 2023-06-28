def oxford_comma(items):
    length = len(items)
    if length == 2:
        return " and ".join(items)
    elif length == 1:
        return "".join(items)
    else:
       return  ", ".join(items[0:length - 1]) + f", and {items[length - 1]}"
