from fungsi_pizza import pizza

#fungsi order pizza
def order():

    #List harga pesanan
    pesanan = []

    #Loop agar bisa digunakan order pizza variasi lain 
    while True:
        #Variabel untuk inisiasi total harga awal
        totalHarga = 0

        #Menampilkan varian pizza
        topping = input("""
        Varian topping
        1. Frankfurter BBQ
        2. Meat Monsta
        3. Super Supreme
        4. Super Supreme Chicken
        Pilihan anda:""").lower()

        #Pilihan crust atau kulit yang bisa dipesan pelanggan
        crust1 = input("""
        Varian Crust
        1. Pan Pizza
        2. Stuffed Crust Cheese
        3. Stuffed Crust Sausage
        4. Cheesy Bite
        5. Crown Crust
        Pilihan anda:""").lower()

        #Pilihan ukuran dari pizza
        size1 = input("""
        Size
        1. Personal
        2. Regular
        3. Large
        Pilihan anda:""").lower()

        #Menambahkan variasi ekstra keju
        extra1 = input("""
        Extra Cheese
        1. Yes
        2. No
        Pilihan anda:""").lower()

        #harga pesanan pizza berdasarkan jenis crust, size, dan ekstra keju ke total harga.
        harga_pizza = pizza(crust1, size1, extra1)

        #Menambahkan harga pesanan pizza ke variabel totalharga
        totalHarga += harga_pizza

        #Membuat input untuk jumlah varian yang telah dipesan
        jumlah_order = int(input("Berapa jumlah pizza yang ingin anda order? "))
        totalHarga *= jumlah_order  # Menghitung total harga per pesanan 

        #Menambah totalHarga ke list pesanan
        pesanan.append(totalHarga)

        #Membuat input untuk bisa memilih apakah ingin memesan variasi pizza lain atau tidak
        nextOrder = input("Apakah anda ingin memesan varian lain (Yes/No)? ").lower()

        #Percabangan apakah ada variasi pesanan pizza baru
        if nextOrder != 'yes': #Jika input masuk selain 'yes'
            break              #Maka program looping akan berhenti

    #menambah kan semua pesanan
    total_pesanan = sum(pesanan)

    #Mengembalikan total harga pesanan
    return total_pesanan
