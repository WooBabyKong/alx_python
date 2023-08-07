def raise_exception():
    try:
        raise TypeError("Exception has been raised")
    except TypeError:
        pass

    print("Exception has been raised")
