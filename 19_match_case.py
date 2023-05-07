status = 2000

match status:
    case 100:
        print("Continue")
    case 200:
        print("OK")
    case 300:
        print("Multiple Choices")
    case 400:
        print("Bad Request")
    case 500:
        print("Internal Server Error")
    case _:
        print(f"Status is not handled: {status} :((")