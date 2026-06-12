def user_input():
    while True:
        try:
            port = input("Enter Port Number: ")
            port = int(port) 
            return port
        except (ValueError, TypeError) as e:
            print(f"{e} Enter Valid Number")


result = user_input()

while True:
    if result > 1 or result < 65535:
        if result == 8080:
            print(f"Port {result} allocated successfully")
            break
        else:
            print(f"port {result} is not currently allocated for try another port")
            result = user_input()
    else:
        print(f"Port Must Be Between 1 and 65535")
        result = user_input()