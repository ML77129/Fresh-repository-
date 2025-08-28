def check_prime(a):
    number_type = "Prime"
    for i in range(2, a):
        if a%i == 0:
            number_type = "Not Prime"
    return number_type            

print(check_prime(11))