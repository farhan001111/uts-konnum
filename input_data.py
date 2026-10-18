import math

fungsi = input("Masukkan fungsi f(x): ")

a = float(input("Masukkan batas bawah (a): "))
b = float(input("Masukkan batas atas (b): "))

toleransi = float(input("Masukkan toleransi: "))

def f(x):
    return eval(fungsi, {"x": x, "math": math})

print("\n Data Metode Bisection ")
print("Fungsi       :", fungsi)
print("Batas bawah  :", a)
print("Batas atas   :", b)
print("Toleransi    :", toleransi)

if f(a) * f(b) < 0:
    print("Syarat Bisection terpenuhi.")
else:
    print("Peringatan: f(a) dan f(b) harus berlainan tanda.")
