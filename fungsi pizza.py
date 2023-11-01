#Fungsi pemilihan pizza dengan parameter crust, size, dan extra
def pizza(crust, size, extra):
    #Harga awal
    harga = 0

    #pilihan statement di varian crust pan pizza
    if crust == 'pan pizza' and size == 'personal':#Kondisi apakah benar pesanan pan pizza dengan ukuran personal
        harga += 43637                             #Menambahkan harga pesanan(harga akan otomatis diperbarui) 
        if extra == 'yes':                         #Jika pesanan ingin extra keju
            harga += 13636                         #Maka harga pesanan akan ditambah lagi sesuai harga tersebut
    elif crust == 'pan pizza' and size == 'regular':#Kondisi apakah benar pesanan pan pizza dengan ukuran regular
        harga += 100910                             #Menambahkan harga pesanan(harga akan otomatis diperbarui) 
        if extra == 'yes':                          #Jika pesanan ingin extra keju
            harga += 16364                          #Maka harga pesanan akan ditambah lagi sesuai harga tersebut
    elif crust == 'pan pizza' and size == 'large':#Kondisi apakah benar pesanan pan pizza dengan ukuran personal
        harga += 132727                           #Menambahkan harga pesanan(harga akan otomatis diperbarui)
        if extra == 'yes':
            harga += 19091
    #pilihan statement di varian stuffed crust cheese
    elif crust == 'stuffed crust cheese' and size == 'personal':
        harga += 55455
        if extra == 'yes':
            harga += 13636
    elif crust == 'stuffed crust cheese' and size == 'regular':
        harga += 120910
        if extra == 'yes':
            harga += 16364
    elif crust == 'stuffed crust cheese' and size == 'large':
        harga += 160000
        if extra == 'yes':
            harga += 19091
    #pilihan statement di varian stuffed crust sausage
    elif crust == 'stuffed crust sausage' and size == 'personal':
        harga += 52728
        if extra == 'yes':
            harga += 13636
    elif crust == 'stuffed crust sausage' and size == 'regular':
        harga += 117273
        if extra == 'yes':
            harga += 16364
    elif crust == 'stuffed crust sausage' and size == 'large':
        harga += 155455
        if extra == 'yes':
            harga += 19091
    #pilihan statement di varian cheesy bite
    elif crust == 'cheesy bite' and size == 'personal':
        harga += 57273
        if extra == 'yes':
            harga += 13636
    elif crust == 'cheesy bite' and size == 'regular':
        harga += 123637
        if extra == 'yes':
            harga += 16364
    elif crust == 'cheesy bite' and size == 'large':
        harga += 164546
        if extra == 'yes':
            harga += 19091
    #pilihan statement di varian crown crust
    elif crust == 'crown crust' and size == 'personal':
        harga += 55455
        if extra == 'yes':
            harga += 13636
    elif crust == 'crown crust' and size == 'regular':
        harga += 120910
        if extra == 'yes':
            harga += 16364
    elif crust == 'crown crust' and size == 'large':
        harga += 160000
        if extra == 'yes':
            harga += 19091
    # Mengembalikan harga pesanan
    return harga