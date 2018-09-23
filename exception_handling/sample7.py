def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    #except ValueError:
    #    print("Wrong type of value given")
    #except Exception:
    #    print("Unown exception")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)
divide(2, 0)
divide("2", "1")