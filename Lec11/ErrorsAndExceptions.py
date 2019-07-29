def computeDivision(first, second):
    try:
        division = first/second
    except TypeError:
        print('you didnt enter two floating point numbers')
    except ZeroDivisionError:
        print('Second number should not be a zero')
    except:
        print('There was an exception')
    else:
        print('No exceptions occured')
    finally:
        ('completing this function')
    return division


print(computeDivision(3, 7))
