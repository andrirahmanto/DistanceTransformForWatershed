import numpy as np

def city_block(arr):

    matrix = np.array(arr)

    # simpan index pixel fore-ground atau pixel yang valunya non-zero kedalam saveindex
    saveindex = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i,j] != 0:
                saveindex.append((i,j))

    # buat matrik hasil yang berisi 0 di setiap elementnya
    hasil = np.zeros((len(arr),len(arr[0])))
    # loop untuk setiap pixel(termasuk pixel fore-ground)
    for i1 in range(len(hasil)):
        for j1 in range(len(hasil[0])):
            lis = []
            for i2,j2 in saveindex:
                # cari jarak pixel ke semua pixel fore-ground
                jarak = abs(i1-i2) + abs(j1-j2)
                lis.append(jarak)
            # ambil jarak yang paling minimum ke fore-ground yang terdekat
            hasil[i1,j1] = min(lis)
    return hasil


arr = [[0,0,0,0,2],
       [0,1,0,0,0],
       [0,0,0,0,0],
       [0,0,0,1,0],
       [0,0,0,0,0],]

print(city_block(arr))