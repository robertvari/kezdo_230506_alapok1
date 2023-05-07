status = -200

if status == 100:
    print("Continue")

elif status == 200:
    print("OK")

elif status == 300:
    print("Multiple Choices")

elif status == 400:
    print("Bad Request")

elif status == 500:
    print("Internal Server Error")

else:
    print(f"Status is not handled: {status} :((")