# # cara membuat variabel di python
# nama = "alex sandro dabukke"
# umur = 20
# # cara menampilkan variabel di python
# print("Nama saya adalah", nama, "umur saya adalah", umur)

# #tipe data di python ada numbers, string, list, tuple, dictionary, set, boolea
# #numbers ada integer, float, complex
# #string adalah kumpulan karakter
# #list adalah kumpulan data yang bisa diubah
# #tuple adalah kumpulan data yang tidak bisa diubah
# #dictionary adalah kumpulan data yang berpasangan
# #set adalah kumpulan data yang tidak berurutan
# #boolea adalah tipe data yang hanya berisi true atau false


# #contoh tipe data numbers
# x = 10
# y = 10.5
# z = 10j
# print(x, "adalah tipe data integer")
# print(y, "adalah tipe data float")
# print(z, "adalah tipe data complex")

# #contoh tipe data string
# a = "ini adalah string"
# print(a)

# #contoh tipe data list
# b = ["apel", "mangga", "jeruk"]
# print(b)

# #contoh tipe data tuple
# c = ("apel", "mangga", "jeruk")
# print(c)

# #contoh tipe data dictionary
# d = {
#     "nama": "alex sandro dabukke",
#     "umur": 20
# }
# print(d)

# #contoh tipe data set
# e = {"apel", "mangga", "jeruk"}
# print(e)

# #contoh tipe data boolean
# f = True
# g = False
# print(f)
# print(g)

# #concatenation
# h = "ini adalah"
# i = "contoh concatenation"
# j = h + " " + i
# print(j)

# #backslash
# k = "ini adalah backslash \\"
# print(k)
# print("Hellos\"World")
# \n = new line 
# \t = tab
# \b = backspace
# \r = carriage return

# x.capitalize() #membuat huruf pertama menjadi kapital
# x.upper() #membuat semua huruf menjadi kapital
# x.lower() #membuat semua huruf menjadi kecil
# x.replace("a", "b") #mengganti huruf a menjadi b
# x.split() #memisahkan kata
# x.strip() #menghapus spasi
# x.find("a") #mencari huruf a
# x.count("a") #menghitung huruf a
# x.startswith("a") #mencari huruf a di awal kata
# x.endswith("a") #mencari huruf a di akhir kata
# x.isalnum() #mencari angka
# x.isalpha() #mencari huruf
# x.isdigit() #mencari angka
# x.islower() #mencari huruf kecil
# x.isupper() #mencari huruf besar


#input berfungsi untuk memasukkan data dari keyboard
# nama = input("siapa nama anda? ")
# umur = input("berapa umur anda? ")
# print("halo salam kenal "+ nama + "  wah anda berumur "+ umur +" tahun anda masih muda ayo semangat masih ada waktu") 


#if else
# x = 10
# y = 20
# if x > y:
#     print("x lebih besar dari y")
# elif x == y:
#     print("x sama dengan y")
# else:
#     print("x lebih kecil dari y")

# logika sederhana penggunaan if else
# tamu  = "wanita"
# baik = True
# rajin = True
# cantik = True

# if baik & rajin & cantik & (tamu == "wanita"):
#     print("boleh jadi pacar saya")
# else:
#     print("maaf saya tidak tertarik")

#looping while
# hitung = 0
# while hitung < 10:
#     print("saya suka makan kucing", hitung)
#     hitung += 2
# else:
#     print("saya sudah kenyang makan kucing")

#looping for
# orang = ["alex", "sandro", "dabukke"]
# for x in orang:
#     print("saya suka makan kucing", x)
# else:
#     print("saya sudah kenyang makan kucing")

# a = 1

#loop bercabang
#adalah loop yang berada di dalam loop 
# cara kerjanya adalah dengan mengeksekusi loop atas dan akan di oper ke loop bawah
# setelah loop bawah selesai akan di cek lagi  di loop atas sampai semua kondisi loop terpenenuhi

# while a < 10:
#     b = 0
#     while b < a:
#         print("*", end="")
#         b += 1
#     print()
#     a += 1
# else:
#     print("selesai")


# for a in range(1, 10):
#     for b in range(1, 10):
#         c = a * b
#         print(c, end="\t")
#     print()

# #list
# buah = ["apel", "mangga", "jeruk"]
# jumlah = [1, 2, 3]
# mixed = [1, "apel", 2, "mangga", 3, "jeruk"]
# #cara menambahkan data ke list
# buah.append("anggur")
# #cara edit data di list
# buah[0] = "nanas"
# #cara menghapus data di list
# del buah[0]
# #cara menampilkan data di list
# print(buah[0])

# for x in buah:
#     print(x)

# tuples
# tuples adalah list yang tidak bisa diubah

# mobil = ("toyota", "honda", "suzuki")
# #cara mengkonversi tuple ke list
# mobil = list(mobil) 

# print(mobil)

# dictionary
# adalah list yang berpasangan
# data = {
#     "nama": "alex",
#     "umur": 22,
#     "pekerjaan": "cyber security",
#     "pasangan" : "anggi christina sitorus"
# }
# # #cara menambahkan data di dictionary
# # data["alamat"] = "jakarta"
# # #cara mengedit data di dictionary
# # data["nama"] = "alex sandro dabukke"
# # #cara menghapus data di dictionary
# # del data["umur"]
# # #cara menampilkan data di dictionary
# # print(data)

# for key, value in data.items():
#     print(key, value)

#nested dictionary
# data =  { 1: {'nama': 'alex', 'umur': 22, 'pekerjaan': 'cyber security'},
#           2: {'nama': 'sandro', 'umur': 23, 'pekerjaan': 'programmer'},
# }

# for key, value in data.items():
#     print(key, value)
#     for key2 in value:
#         print(key2, value[key2])

#set
# adalah list yang tidak berurutan
# tidak boleh duplikat

# angka1 = {1, 2, 3, 4, 5,}
# angka2 = {4, 5, 6, 7, 8, 9}

# print(angka1 | angka2) #union
# print(angka1 & angka2) #intersection
# print(angka1 - angka2) #difference
# print(angka1 ^ angka2) #symmetric difference


#function
# def hitung(a,b):
#     return a + b

# print(hitung(10, 20))

# def printData(name,hobby):
#     print("name " + name + " hobby " + hobby) 


# printData(hobby="ngoding", name="alex")

# #args
# def printData(*args):
#     print(args)

# printData("alex", "sandro", "dabukke")

# #kwargs
# def printData(**kwargs):
#     print(kwargs)

# printData(name="alex", hobby="ngoding", age=22)

orang ={
    "nama": "anggi christina sitorus",
    "umur": 20,
    "pekerjaan": "mahasiswa",
}