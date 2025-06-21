#Find the LCM and HCF of two numbers using loops

# Find HCF and LCM using loops

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# HCF (using loop)
hcf = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        hcf = i

# LCM (using loop)
lcm = max(a, b)
while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += 1

print("HCF of", a, "and", b, "is:", hcf)
print("LCM of", a, "and", b, "is:", lcm)
