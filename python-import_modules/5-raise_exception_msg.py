def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except NameError:
        print(message)
raise_exception_msg("This is a name exception.")