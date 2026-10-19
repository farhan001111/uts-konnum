
from fungsi import buat_fungsi
from input_data import input_data
from metode_biseksi import bisection_method
from output_hasil import tampilkan_hasil


def main():
    print("====================================")
    print("       PROGRAM METODE BISEKSI")
    print("====================================")

    f, a, b, toleransi = input_data()

    try:
        akar, iterasi = bisection_method(f, a, b, toleransi)
        tampilkan_hasil(akar, iterasi)

    except ValueError as e:
        print("Terjadi kesalahan:", e)


if __name__ == "__main__":
    main()

