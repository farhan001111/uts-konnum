import math


def buat_fungsi(ekspresi):
    """Ubah teks fungsi menjadi fungsi Python f(x)."""
    lingkup = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    lingkup["abs"] = abs

    def f(x):
        lingkup["x"] = x
        return eval(ekspresi, {"__builtins__": {}}, lingkup)

    return f


def biseksi(f, a, b, toleransi, maks_iterasi=100):
    """Hitung akar f(x) dengan metode biseksi dan tampilkan tabel iterasi."""
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        print("Error: f(a) dan f(b) harus berbeda tanda. Ubah interval.")
        return None

    print(f"\n{'Iter':<5}{'a':>12}{'b':>12}{'c':>12}{'f(c)':>14}{'|b-a|':>12}")
    print("-" * 67)

    c = a
    for i in range(1, maks_iterasi + 1):
        c = (a + b) / 2
        fc = f(c)
        print(f"{i:<5}{a:>12.6f}{b:>12.6f}{c:>12.6f}{fc:>14.6f}{abs(b - a):>12.6f}")

        if fc == 0 or abs(b - a) / 2 < toleransi:
            return c

        if fa * fc < 0:
            b = c
        else:
            a, fa = c, fc

    return c


def main():
    print("=== Metode Biseksi ===")
    try:
        ekspresi = input("Masukkan fungsi f(x) (contoh: x**2 - 4): ")
        f = buat_fungsi(ekspresi)
        a = float(input("Batas bawah: "))
        b = float(input("Batas atas: "))
        tol = float(input("Toleransi (contoh: 0.001): "))

    if a >= b:
            print("Error: batas bawah harus lebih kecil dari batas atas.")
            return
        if tol <= 0:
            print("Error: toleransi harus lebih dari 0.")
            return
 
        akar = biseksi(f, a, b, tol)
        if akar is not None:
            print(f"\nHasil: akar pendekatan x = {akar:.6f}")
            print(f"f(x) = {f(akar):.6f}")
    except ValueError:
        print("Error: input angka tidak valid.")
    except Exception as e:
        print(f"Error: fungsi tidak valid ({e}).")
 
 
if __name__ == "__main__":
    main()
