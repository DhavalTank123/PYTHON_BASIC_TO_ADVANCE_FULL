def uppercase(func):

    print("DEBUG 1: uppercase() decorator function called")
    print("DEBUG 2: Received function:", func)

    def wrapper(name):

        print("DEBUG 3: uppercase wrapper started")
        print("DEBUG 4: Name received:", name)

        result = func(name)

        print("DEBUG 5: Original function returned:", result)

        result = result.upper()

        print("DEBUG 6: After upper():", result)

        return result

    print("DEBUG 7: Returning uppercase wrapper")
    return wrapper


def add_stars(func):

    print("DEBUG 8: add_stars() decorator function called")
    print("DEBUG 9: Received function:", func)

    def wrapper(name):

        print("DEBUG 10: add_stars wrapper started")
        print("DEBUG 11: Name received:", name)

        result = func(name)

        print("DEBUG 12: Function returned:", result)

        result = "*** " + result + " ***"

        print("DEBUG 13: After adding stars:", result)

        return result

    print("DEBUG 14: Returning add_stars wrapper")
    return wrapper


print("DEBUG 15: Before decorators")

@add_stars
@uppercase
def welcome(name):

    print("DEBUG 16: Original welcome() function started")

    result = "Hello " + name

    print("DEBUG 17: Returning from welcome():", result)

    return result


print("DEBUG 18: Taking input")

name = input("Enter your name: ")

print("DEBUG 19: Calling welcome()")

answer = welcome(name)

print("DEBUG 20: Final answer:", answer)

print(answer)