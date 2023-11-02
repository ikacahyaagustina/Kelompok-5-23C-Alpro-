from fungsi_pizza1 import pizza

#cara order pizza
def order():

    #List pesanan
    pesanan = []

    #Loop digunakan untuk order pizza variasi lain
    while True:
        #Variabel untuk inisiasi total harga awal
        totalHarga = 0

        #Pilihan topping pizza
        toppingpizza = input("""
        Varian topping
        1. Frankfurter BBQ
        2. Meat Monsta
        3. Super Supreme
        4. Super Supreme Chicken
        Pilih topping apa?""").lower()

        #Pilihan crust pizza yang dipesan pelanggan
        crust = input("""
        Varian Crust
        1. Pan Pizza
        2. Stuffed Crust Cheese
        3. Stuffed Crust Sausage
        4. Cheesy Bite
        5. Crown Crust
        Pilih crust apa?""").lower()

        #Pilihan ukuran pizza
        size = input("""
        Size
        1. Personal
        2. Regular
        3. Large
        Pilih size apa?""").lower()

        #Menambahkan ekstra keju
        extrakeju = input("""
        Extra Keju
        1. Yes
        2. No
        Pilih Iya/Tidak?""").lower()

        #harga pesanan pizza berdasarkan jenis crust, size, dan ekstra keju ke total harga.
        harga_pizza = pizza(crust, size, extrakeju)

        #Menambahkan harga pesanan pizza ke variabel totalharga
        totalHarga += harga_pizza

        #Membuat input untuk jumlah varian yang telah dipesan
        jumlah_order = int(input("Berapa jumlah pizza yang ingin anda order? "))
        totalHarga *= jumlah_order  
        
        #Menambah totalHarga ke list pesanan
        pesanan.append(totalHarga)
        
        break              #Maka program looping akan berhenti

    #menambah kan semua pesanan
    total_pesanan = sum(pesanan)

    #Mengembalikan total harga pesanan
    return total_pesanan
