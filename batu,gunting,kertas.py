import random

pilihan = ["Batu","Gunting","Kertas"]
komputer = random.choice(pilihan)
pemain = False
score_comp = 0
score_pemain = 0
counter = 0
while counter < 3:
    user = input("Masukan Pilihan (Batu, Gunting, Kertas) = ").capitalize()
    if user == komputer :
        print("Imbang")
    elif user == "Batu" :
        if komputer == "Gunting":
            print("Selamat anda Menang")
            score_pemain += 1
        else :
            print("Anda Kalah")
            score_comp += 1
    elif user == "Gunting":
        if komputer == "Batu":
            print("Selamat Anda Menang!!!")
            score_pemain += 1
        else :
            print("Anda Kalah !!!")
            score_comp += 1
    elif user == "Kertas":
        if komputer == "Batu":
            print("Selamat anda Menang!!!")
            score_pemain += 1
        else :
            print("Anda Kalah")
            score_comp += 1
    counter += 1

print(" SCORE PEMAIN "+ str(score_pemain))
print(" SCORE KOMPUTER "+ str(score_comp))

        

