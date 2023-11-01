from fungsi_order import order

#Menampilkan hiasan(opsional)
print("""
--------------Selamat Datang Di Pizza Hut--------------
""")

#Memanggil fungsi order
hasil_order = order()

#Menampilkan harga total
print(f"""
Total harga dari pesanan anda adalah Rp {hasil_order},00
""")

#Menampilkan variasi(opsional)
print("""
--------------Terima Kasih Telah Memakai Layanan Kami--------------
""")