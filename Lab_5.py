# Part 1

# Task 1

def is_valid_part(part):
    try:
        number = int(part)
    except ValueError:
        return False

    if number < 0 or number > 255:
        return False

    if len(part) > 1 and part[0] == '0':
        return False

    return True

print(is_valid_part('255'))
print(is_valid_part('256'))
print(is_valid_part('01'))
print(is_valid_part('0'))

# Task 2

def is_valid_ip(ip):
    parts = ip.split('.')

    if len(parts) != 4:
        return False

    for p in parts:
        if  not is_valid_part(p):
            return False

    return True

print(is_valid_ip("192.168.1.1"))  # True
print(is_valid_ip("192.168.256.1"))  # False
print(is_valid_ip("192.168.1"))  # False
print(is_valid_ip("192.168.01.1"))  # False

# Part 2

# Task 1

def decimal_to_binary(n):
    if n == 0:
        return "0"

    if n == 1:
        return "1"

    return decimal_to_binary(n//2) + str(n % 2)

# Test cases
print(decimal_to_binary(10))   # "1010"
print(decimal_to_binary(255))  # "11111111"
print(decimal_to_binary(1))    # "1"

# Task 2

def binary_to_decimal(b):
    if b == "":
        return 0

    first = b[0]
    rest = b[1:]

    value = int(first)
    place = len(rest)

    return value * (2 ** place) + binary_to_decimal(rest)

print(binary_to_decimal("1010"))      # 10
print(binary_to_decimal("11111111"))  # 255
print(binary_to_decimal("1"))         # 1