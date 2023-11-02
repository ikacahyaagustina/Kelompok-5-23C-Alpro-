#pemesanan pizza menggunakan penambahan crust, size, dan extrakeju
def toppingpizza(crust, size, extrakeju):
    #Harga awal
    harga = 0

    #pilihan pizza di varian crust pan pizza dan size pizza
    if crust == 'pan pizza' and size == 'personal':
        #Kondisi pesanan varian pan pizza dan personal, maka memperbarui harga pesanan
        harga += 43637  
        #jika pesanan ingin menambahkan keju,maka harga pesanan otomatis akan ditambahkan
        if extra == 'yes':                        
            harga += 13636               
    elif crust == 'pan pizza' and size == 'regular':
        #Kondisi pesanan varian pan pizza dan reguler, maka memperbarui harga pesanan
        harga += 100910 
        #jika pesanan ingin menambahkan keju,maka harga pesanan otomatis akan ditambahkan
        if extra == 'yes':                          
            harga += 16364                         
    elif crust == 'pan pizza' and size == 'large':
        #Kondisi pesanan varian pan pizza dan large, maka memperbarui harga pesanan
        harga += 132727   
        #jika pesanan ingin menambahkan keju,maka harga pesanan otomatis akan ditambahkan
        if extra == 'yes':
            harga += 19091
    #pilihan statement di varian stuffed crust cheese
    elif crust == 'stuffed crust cheese' and size == 'personal':
         #Kondisi pesanan varian stuffed crust cheese dan personal, maka memperbarui harga pesanan
        harga += 55455
        #jika pesanan ingin menambahkan keju,maka harga pesanan otomatis akan ditambahkan
        if extra == 'yes':
            harga += 13636
    elif crust == 'stuffed crust cheese' and size == 'regular':
         #Kondisi pesanan varian stuffed crust cheese reguler, maka memperbarui harga pesanan
        harga += 120910
        #jika pesanan ingin menambahkan keju,maka harga pesanan otomatis akan ditambahkan
        if extra == 'yes':
            harga += 16364
    elif crust == 'stuffed crust cheese' and size == 'large':
         #Kondisi pesanan varian stuffed crust cheese large, maka memperbarui harga pesanan
        harga += 160000
        #jika pesanan ingin menambahkan keju,maka harga pesanan otomatis akan ditambahkan
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
