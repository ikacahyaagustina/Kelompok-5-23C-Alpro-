#pemesanan pizza menggunakan penambahan crust, size, dan extrakeju
def pizza(crust, size, extrakeju):
    #Harga awal
    harga = 0

    #pilihan pizza di varian crust pan pizza dan size pizza
    if crust == 'pan pizza' and size == 'personal':
        #Kondisi pesanan varian pan pizza dan personal, maka memperbarui harga pesanan
        harga += 43637  
        #jika pesanan ingin menambahkan keju,maka harga pesanan otomatis akan ditambahkan
        if extrakeju == 'yes':                        
            harga += 13636               
    elif crust == 'pan pizza' and size == 'regular':
        #Kondisi pesanan varian pan pizza dan reguler, maka memperbarui harga pesanan
        harga += 100910 
        #jika pesanan ingin menambahkan keju,maka harga pesanan otomatis akan ditambahkan
        if extrakeju == 'yes':                          
            harga += 16364                         
    elif crust == 'pan pizza' and size == 'large':
        #Kondisi pesanan varian pan pizza dan large, maka memperbarui harga pesanan
        harga += 132727   
        #jika pesanan ingin menambahkan keju,maka harga pesanan otomatis akan ditambahkan
        if extrakeju == 'yes':
            harga += 19091
    #pilihan statement di varian stuffed crust cheese
    elif crust == 'stuffed crust cheese' and size == 'personal':
        #Kondisi pesanan varian stuffed crust cheese dan personal, maka memperbarui harga pesanan
        harga += 55455
        #jika pesanan ingin menambahkan keju,maka harga pesanan otomatis akan ditambahkan
        if extrakeju == 'yes':
            harga += 13636
    elif crust == 'stuffed crust cheese' and size == 'regular':
        #Kondisi pesanan varian stuffed crust cheese reguler, maka memperbarui harga pesanan
        harga += 120910
        #jika pesanan ingin menambahkan keju,maka harga pesanan otomatis akan ditambahkan
        if extrakeju == 'yes':
            harga += 16364
    elif crust == 'stuffed crust cheese' and size == 'large':
        #Kondisi pesanan varian stuffed crust cheese large, maka memperbarui harga pesanan
        harga += 160000
        #jika pesanan ingin menambahkan keju,maka harga pesanan otomatis akan ditambahkan
        if extrakeju == 'yes':
            harga += 19091
    #pilihan statement di varian stuffed crust sausage
    elif crust == 'stuffed crust sausage' and size == 'personal':
        #Kondisi pesanan varian stuffed crust sausage dan personal, maka memperbarui harga pesanan
        harga += 52728
        #jika pesanan ingin menambahkan keju,maka harga pesanan otomatis akan ditambahkan
        if extrakeju == 'yes':
            harga += 13636
    elif crust == 'stuffed crust sausage' and size == 'regular':
        #Kondisi pesanan varian stuffed crust sausage dan regular, maka memperbarui harga pesanan
        harga += 117273
        #jika pesanan ingin menambahkan keju,maka harga pesanan otomatis akan ditambahkan
        if extrakeju == 'yes':
            harga += 16364
    elif crust == 'stuffed crust sausage' and size == 'large':
        #Kondisi pesanan varian stuffed crust sausage dan large, maka memperbarui harga pesanan
        harga += 155455
        #jika pesanan ingin menambahkan keju,maka harga pesanan otomatis akan ditambahkan
        if extrakeju == 'yes':
            harga += 19091
    #pilihan statement di varian cheesy bite
    elif crust == 'cheesy bite' and size == 'personal':
        #Kondisi pesanan varian cheesy bite dan personal, maka memperbarui harga pesanan
        harga += 57273
        #jika pesanan ingin menambahkan keju,maka harga pesanan otomatis akan ditambahkan
        if extrakeju == 'yes':
            harga += 13636
    elif crust == 'cheesy bite' and size == 'regular':
        #Kondisi pesanan varian cheesy bite dan reguler, maka memperbarui harga pesanan
        harga += 123637
        #jika pesanan ingin menambahkan keju,maka harga pesanan otomatis akan ditambahkan
        if extrakeju == 'yes':
            harga += 16364
    elif crust == 'cheesy bite' and size == 'large':
        #Kondisi pesanan varian cheesy bite dan large, maka memperbarui harga pesanan
        harga += 164546
        #jika pesanan ingin menambahkan keju,maka harga pesanan otomatis akan ditambahkan
        if extrakeju == 'yes':
            harga += 19091
    #pilihan statement di varian crown crust
    elif crust == 'crown crust' and size == 'personal':
        #Kondisi pesanan varian crown crust dan personal, maka memperbarui harga pesanan
        harga += 55455
        #jika pesanan ingin menambahkan keju, maka harga pesanan otomatis akan ditambahkan
        if extrakeju == 'yes':
            harga += 13636
    elif crust == 'crown crust' and size == 'regular':
        #Kondisi pesanan varian crown crust dan regular, maka memperbarui harga pesanan
        harga += 120910
        #jika pesanan ingin menambahkan keju, maka harga pesanan otomatis akan ditambahkan
        if extrakeju == 'yes':
            harga += 16364
    elif crust == 'crown crust' and size == 'large':
        #Kondisi pesanan varian crown crust dan large, maka memperbarui harga pesanan
        harga += 160000
        #jika pesanan ingin menambahkan keju, maka harga pesanan otomatis akan ditambahkan
        if extrakeju == 'yes':
            harga += 19091
    # Mengembalikan harga pesanan
    return harga
