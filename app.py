#cara import file lain
import datetime
import learn
import sys
# #cara import fungsi dari file lain
# from learn import fungsi

#jika ingin memakai fungsi yang ada di file lain jangan lupa menambahkan nama file nya didepan fungsi
# print(learn.orang)

# print(datetime.datetime.now())


# # kita tidak bisa mengakses variabel yang ada di dalam fungsi
# name = "alex"
# def printName():
#     #jika ingin mengakses variabel yang ada di dalam fungsi kita harus menambahkan global
#     global name
#     print("ini nama saya dalam akses dalam" + name)



# printName()

# print("ini nama saya dalam akses luar " + name)

# # metode untuk menangani error
# # raise adalah fungsi untuk mematikan kode yang ada dibawahnya
# # raise Exception("ini adalah error")

# # try adalah metode untuk menangani error dengan cara mencoba kode yang ada didalamnya
# # except adalah metode untuk menangani error dengan cara menangkap error yang ada
# # finally adalah metode untuk menangani error dengan cara menjalankan kode yang ada didalamnya
# #     #value error adalah error yang akan menampilkan pesan error jika variabel yang di panggil tidak ada
# #     #name error adalah error yang akan menampilkan pesan error yang kita buat sendiri
# # try:
# #     print(x)
# # except ValueError:
# #     print("variabel x tidak ada")
# # finally:
# #     print("ini kode yang akan dijalankan")

# def apakah_ini_linux():
#     assert ('linux' in sys.platform), "fungsi ini hanya bisa dijalankan di linux"
#         #jika ingin menampilkan pesan error yang kita buat sendiri kita bisa menambahkan pesan error di belakang assert

# apakah_ini_linux()

# game sederhana

# player1 = {

#     "name": "alex",
#     "power": 100,
    
# }

# player2 = {
    
#         "name": "anggi",
#         "power": 100,
      
#     }

# def train(player):
#     player["power"] += 10


# def attack(attacker, defender):
#     if(attacker["power"] > defender["power"]):
#         print('serangan anda berhasil mengalahkan', defender["name"], "selamat atas kemenangan anda", attacker["name"])
#     elif(attacker["power"] == defender["power"]):
#             print("kekuatan anda seimbang dengan", defender["name"], attacker["name"],"!")
#     else:
#         print('serangan anda gagal mengalahkan', defender["name"], "anda kalah", attacker["name"])




# attack(player1, player2)


# game sederhana 2


name = input("masukkan nama peliharaan anda ^_^: ")
peliharaan = { "name": name, "power": 100, }
print("selamat datang", peliharaan["name"])

def startGame():
    choice = input("apa yang ingin anda lakukan?  1. train  2. cek status  3. exit ")

    if choice == "1":
        goEat()

    elif choice == "2":
        goStatus()

    elif choice == "3":
        print("terima kasih sudah bermain , dadah!")
        exit()

    else:
        print("pilihan tidak tersedia")
        startGame()




def goEat():
    print("nyam nyam nyam")
    peliharaan["power"] += 10
    print("peliharaan anda bertambah kuat")
    startGame()


def goStatus():

    print("status peliharaan anda" , peliharaan)
    startGame()

startGame()