#!/usr/bin/python3
#author: Arif fadillah
import os
def buat_file():
    import os
    d = os.getcwd()
    print(" ")
    print("============BUAT FILE============")
    print("posisi anda saat ini", d)
    print("kamu akan membuat file")
    buat = input("masukan nama file: ")
    if buat == '':
        print("anda tidak memasukan input")
    elif os.path.exists(buat):
        print("file/direktori", buat, "sudah ada")
    else:
        open(buat, "x")
        print("file", buat, "telah dibuat")

def hapus_file():
    import os
    d = os.getcwd()
    print(" ")
    print("============HAPUS FILE============")
    print("posisi anda saat ini", d)
    print("kamu akan menghapus file")
    hapus = input("masukan nama file: ")
    d = os.path.isfile(hapus)
    if d == True:
        t = input("lanjut menghapus..? [y/n]: ")
        if t == 'y':
            os.remove(hapus)
            print("file", hapus,"telah dihapus")
        elif t == 'n':
            menu()
        else:
            print("inputan hanya y/n")        
    elif hapus == '':
        print("anda tidak memasukan input")
    else:
        print("file/direktori", hapus, "tidak ada")


def buat_direktori():
    import os
    d = os.getcwd()
    print(" ")
    print("============BUAT DIREKTORI============")
    print("posisi anda saat ini", d)
    print("kamu akan membuat direktori")
    creat = input("masukan nama direktori: ")
    if creat == '':
        print("anda tidak memasukan input")
    elif os.path.exists(creat):
        print("direktori/file", creat, "sudah ada")
    else:
        os.mkdir(creat)
        print("direktori", creat,"telah dibuat")

def hapus_direktori():
    import os
    d = os.getcwd()
    print(" ")
    print("============HAPUS DIREKTORI============")
    print("posisi anda saat ini", d)
    print("kamu akan menghapus direktori")
    remove = input("masukan nama direktori: ") 
    d = os.path.isdir(remove)
    if d == True:
        t = input("lanjut menghapus..? [y/n]: ")
        if t == 'y':
            import shutil
            shutil.rmtree(remove)
            print("direktori", remove,"telah dihapus")
            
        elif t == 'n':
            menu()
        else:
            print("inputan hanya y/n")
    elif remove == '':
        print("anda tidak memasukan input")
    else:
        print("direktori", remove, "tidak ada")
def melihat_isi_file():
    import os
    d = os.getcwd()
    print(" ")
    print("============LIHAT ISI FILE============")
    print("posisi anda saat ini", d)
    print("kamu akan melihat isi file")
    read = input("masukan nama file: ")
    print(" ")
    d = os.path.isfile(read)
    if d == True:
        f = open(read, "r")
        print(f.read())
    elif read == '':
        print("anda tidak memasukan input")
    else:
        print("file", read, "tidak ada")

def lihat_direktori():
    import os
    d = os.getcwd()
    print(" ")
    print("============LIHAT ISI DIREKTORI============")
    print("posisi anda saat ini", d)
    print("kamu akan melihat isi direktori")
    imput = input("masukan nama direktori (beserta path): ")
    if imput=='':
        print("anda tidak memasukan input")
    else:
        d = os.path.isdir(imput)
        if d == True:
            x = os.listdir(imput)
            print(x)
        else:
            print("direktori", imput," tidak ada")

def menu():
    while True:
        print(" ")
        print("===========SELAMAT DATANG========")
        print("=============== MENU ============")
        print("||                             ||")
        print("|| 1. MEMBUAT FILE             ||")
        print("|| 2. MENGHAPUS FILE           ||")
        print("|| 3. MEMBUAT DIREKTORI        ||")
        print("|| 4. MENGHAPUS DIREKTORI      ||")
        print("|| 5. MELIHAT ISI FILE         ||")
        print("|| 6. MELIHAT ISI DIREKTORI    ||")
        print("|| 7. KELUAR                   ||")
        print("||                             ||")
        print("=================================")
        
        menu = input('Masukan menu perintah (Nomer Menu): ')
        
        if menu == '':
            while True:
                print("anda tidak memasukan input")
                print(" ")
                tanya()
        elif menu == '1':
            while True:
                buat_file()
                print(" ")
                tanya()
        elif menu == '2':
            while True:
                hapus_file()
                print(" ")
                tanya()
        elif menu == '3':
            while True:
                buat_direktori()
                print(" ")
                tanya()
        elif menu == '4':
            while True:
                hapus_direktori()
                print(" ")
                tanya()
        elif menu == '5':
            while True:    
                melihat_isi_file()
                print(" ")
                tanya()
        elif menu == '6':
            while True:    
                lihat_direktori()
                print(" ")
                tanya()
        elif menu == '7':
            os.system('clear')
            exit()
        else:
            while True:
                print("Menu hanya 1-7")
                print(" ")
                tanya()

def tanya():
    while True:   
        tanya = input('kembali ke menu..? (y/n): ')
        if tanya == 'y':
            menu()
        elif tanya == 'n':
            break
        elif tanya == '':
            print("anda tidak memasukan input")
        else:
            print("inputan salah")

menu()
