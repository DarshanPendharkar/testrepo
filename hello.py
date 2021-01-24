user_response = "YES"
while user_response == "YES" :
    print("Enter first no.")
    no1 = int(input())
    print("Enter second no.")
    no2 = int(input())

    print("Addition of two nos. is "+ str(no1 + no2))

    print("Do you wanna continue, reply with YES or NO")

    user_response = input()