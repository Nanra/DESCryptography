m = []
s = 1
Pmin = []
print "Proses Permutasi Dengan Tabel P-1"
print "Masukkan Biner : "
# for i in range(1, 65):
#     masukan = raw_input()
#     m.append(masukan)
#     if i % 4 == 0:
#         print "\n"
#     # print (m)

# # Test Logic
while s < 65 :
    m.append(s)
    s += 1

Pmin = [m[40 - 1], m[8 - 1], m[48 - 1], m[16 - 1], m[56 - 1], m[24 - 1], m[64 - 1], m[32 - 1],
        m[39-1], m[7-1], m[47-1], m[15-1], m[55-1], m[23-1], m[63-1], m[31-1],
        m[38-1], m[6-1], m[46-1], m[14-1], m[54-1], m[22-1], m[62-1], m[30-1],
        m[37-1], m[5-1], m[45-1], m[13-1], m[53-1], m[21-1], m[61-1], m[29-1],
        m[36-1], m[4-1], m[44-1], m[12-1], m[52-1], m[20-1], m[60-1], m[28-1],
        m[35-1], m[3-1], m[43-1], m[11-1], m[51-1], m[19-1], m[59-1], m[27-1],
        m[34-1], m[2-1], m[42-1], m[10-1], m[50-1], m[18-1], m[58-1], m[26-1],
        m[33-1], m[1-1], m[41-1], m[9-1], m[49-1], m[17-1], m[57-1], m[25-1]]

print ("&"*60)
print(m)
print ("@"*60)
print Pmin
print ("$"*80)
print "Hasil Setelah melalui Tabel P-1\n"
print Pmin[0:4], Pmin[4:8], Pmin[8:12], Pmin[12:16]
print "\n"
print Pmin[16:20], Pmin[20:24], Pmin[24:28], Pmin[28:32]
print "\n"
print Pmin[32:36], Pmin[36:40], Pmin[40:44], Pmin[44:48]
print "\n"
print Pmin[48:52], Pmin[52:56], Pmin[56:60], Pmin[60:64]
print "\n"
print ("#"*80)
print "Hasil L16 R16 P-1 = ", Pmin[0:64]
print ("%"*80)
print "Jumlah Bit",len(Pmin)
