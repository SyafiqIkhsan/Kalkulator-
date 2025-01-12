#tambah
def tambah(x, y):
    return x + y

#kurang
def kurang(x, y):
    return x - y

#kali
def kali(x, y):
    return x * y

#bagi
def bagi(x, y):
    if y == 0:
        return "Tidak bisa membagi dengan nol!"
    else:
        return x / y

# menu kalkulator
def menu():
    print("Pilih menu:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")

def kalkulator():
    while True:
        menu()
        pilihan = input("Masukkan pilihan (1/2/3/4) atau 'q' untuk keluar: ")

        if pilihan == 'q':
            print("Keluar dari kalkulator...")
            break
        
        try:
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")
            continue

        if pilihan == '1':
            print(f"Hasil: {num1} + {num2} = {tambah(num1, num2)}")
        elif pilihan == '2':
            print(f"Hasil: {num1} - {num2} = {kurang(num1, num2)}")
        elif pilihan == '3':
            print(f"Hasil: {num1} * {num2} = {kali(num1, num2)}")
        elif pilihan == '4':
            print(f"Hasil: {num1} / {num2} = {bagi(num1, num2)}")
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-4 atau 'q' untuk keluar.")
        
        lanjut = input("Apakah Anda ingin melakukan perhitungan lain? (ya/tidak): ")
        if lanjut.lower() != 'ya':
            break

if __name__ == "__main__":
    kalkulator()
