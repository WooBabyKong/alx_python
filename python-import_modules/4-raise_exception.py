def raise_exception():
    class CustomException(Exception):
        pass

    raise CustomException("Exception has been raised")

try:
    raise_exception()
except CustomException as e:
    print(e)