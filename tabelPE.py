m = []
s = 1
P = []
print "Proses Permutasi Dengan Tabel P"
print "Masukkan Biner : "
for i in range(1, 33):
    masukan = raw_input()
    m.append(masukan)
    if i % 4 == 0:
        print "\n"
    # print (m)

# Test Logic
# while s < 33 :
#     m.append(s)
#     s += 1

P = [m[16 - 1], m[7 - 1], m[20 - 1], m[21 - 1],
     m[29-1], m[12-1], m[28-1], m[17-1],
     m[1-1], m[15-1], m[23-1], m[26-1],
     m[5-1], m[18-1], m[31-1], m[10-1],
     m[2-1], m[8-1], m[24-1], m[14-1],
     m[32-1], m[27-1], m[3-1], m[9-1],
     m[19-1], m[13-1], m[30-1], m[6-1],
     m[22-1], m[11-1], m[4-1], m[25-1]]

print ("%"*80)
print(m)
print ("%"*80)
print P
print ("%"*80)
print "Hasil Setelah melalui Tabel P\n"
print P[0:4], P[4:8], P[8:12], P[12:16]
print "\n"
print P[16:20], P[20:24], P[24:28], P[28:32]
print "\n"
print ("%"*80)
print "F = ", P[0:32]
print ("%"*80)
print "Jumlah Bit",len(P)
