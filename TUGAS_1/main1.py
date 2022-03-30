# Alpina Damayanti Program main1_120450054.py
# Author : Alpina Damayanti 
# NIM : 120450054
# Kelas : RB
# Affiliation : Sains Data ITERA
# Date : xx march 2022
# Perbaikan kuis 1 PBF RA
# Program Description : Program to solve simple encryption password problem 

from spetools_120450054 import encrypt

while True:
    jawab=input("Apakah kamu ingin melakukan enkripsi (y/n)? ")
    if jawab  == "y":
        text = input("Masukkan text pasword anda : ")
        print ("Text : " + text)
        print ("Cipher : " + encrypt(text))
    else:
        print("Terimakasih")
        break
