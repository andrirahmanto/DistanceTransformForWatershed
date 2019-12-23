import numpy as np
import matplotlib.pyplot as plt

def city_block(lis):

    matrix = np.array(lis)

    # simpan index pixel fore-ground atau pixel yang valunya non-zero kedalam saveindex
    saveindex = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i,j] != 0:
                saveindex.append((i,j))

    # buat matrik hasil yang berisi 0 di setiap elementnya
    hasil = np.zeros((len(lis),len(lis[0])))
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


lis = [[0,0,0,0,0],
       [0,0,1,0,0],
       [0,1,0,1,0],
       [0,0,1,0,0],
       [0,0,0,0,0],]

hasil = city_block(lis)
print(hasil)

f,(x,y) = plt.subplots(1,2)
x.imshow(lis, 'gray')
y.imshow(hasil, 'gray')
plt.show()
