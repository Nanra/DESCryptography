m = []
s = 1
E = []
print "Proses Permutasi Dengan Tabel E"
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

E = [m[32-1], m[1-1], m[2-1], m[3-1], m[4-1], m[5-1],
      m[4-1], m[5-1], m[6-1], m[7-1], m[8-1], m[9-1],
      m[8-1], m[9-1], m[10-1], m[11-1], m[12-1], m[13-1],
      m[12-1], m[13-1], m[14-1], m[15-1], m[16-1], m[17-1],
      m[16-1], m[17-1], m[18-1], m[19-1], m[20-1], m[21-1],
      m[20-1], m[21-1], m[22-1], m[23-1], m[24-1], m[25-1],
      m[24-1], m[25-1], m[26-1], m[27-1], m[28-1], m[29-1],
      m[28-1], m[29-1], m[30-1], m[31-1], m[32-1], m[1-1]]

print ("%"*80)
print(m)
print ("%"*80)
print E
print ("%"*80)
print "Hasil Setelah melalui Tabel E\n"
print E[0:6], E[6:12], E[12:18], E[18:24]
print "\n"
print E[24:30], E[30:36], E[36:42], E[42:48]
print "\n"
print ("%"*80)
print "E(Rn-1) = ", E[0:48]
print ("%"*80)
print "Jumlah Bit",len(E)
