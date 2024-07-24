def popper(stack):
    try:
        return stack.pop()
    except IndexError:
        raise IndexError("Missing argument for Fetch!")
