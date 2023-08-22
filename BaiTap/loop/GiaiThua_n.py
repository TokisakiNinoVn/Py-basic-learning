# import math
# number = int(input("Nhập số cần tính giai thừa: "))
# print(f"Giai thừa của {number} là {math.factorial(number)}")


# def tinh_giai_thua(n):
#     if n == 0:
#         return 1
#     else:
#         return n * tinh_giai_thua(n - 1)

# so_can_tinh = int(input("Nhập vào một số nguyên dương: "))
# ket_qua = tinh_giai_thua(so_can_tinh)
# print(f"Giai thừa của {so_can_tinh} là {ket_qua}")



def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("Nhập số cần tính giai thừa: "))
print(f"Giai thừa của {number} là {factorial_iterative(number)}")
