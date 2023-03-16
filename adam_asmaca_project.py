import random

tahmin_edilenler = []
words = ["mal","totoş","faruk","televizyon","bilgisayar"]
alfabe = '[ a b c ç d e f g ğ h i ı j k l m n o ö p r s ş t u ü v y z ]'

sekil0 = (""
          
          
          "__\n")

sekil1 = ("|    \n"
          "|\n"
          "|\n"
          "__\n")

sekil2 = ("---------\n"
          "|    \n"
          "|\n"
          "|\n"
          "__\n")

sekil3 = ("---------\n"
          "|       |\n"
          "|\n"
          "|\n"
          "__\n")

sekil4 = ("---------\n"
          "|       |\n"
          "|       O\n"
          "|     \n"
          "__\n")     

sekil5 = ("---------\n"
          "|       |\n"
          "|       O\n"
          "|       | \n"
          "__\n")

sekil6 = ("---------\n"
          "|       |\n"
          "|       O\n"
          "|     / | \ \n"
          "__\n")

sekil7 = ("---------\n"
          "|       |\n"
          "|       O\n"
          "|     / | \ \n"
          "__     | |\n")

def welcome():
    print("-----------------ADAM ASMACA OYUNUNA HOŞGELDİNİZ-----------------")
    isim = input("Lütfen isminizi girin:")
    b = isim.upper()
    a = "Kullanıcı Adı:" + b
    print(a)

def play_again():
    play_game = int(input("If you want to try again press 1 or don't press 2:"))
    
    if play_game == 1 :
        print("Game is started again!")
        adam_asmaca()
    elif play_game == 2:
        print("Game Finished.")
        


def adam_asmaca():
    welcome()
    global tahmin_edilenler
    global words
    global alfabe
    
    word = random.choice(words)
    print("Oyunun başlıyor hazır mısın ? Bilmen gereken kelime {} harfli. BOL ŞANS!!".format(len(word)))    
    haklar = 8
    
    while haklar > 0:
        gorunen_harfler = ''
        for harf in word:
            if harf in tahmin_edilenler:
                gorunen_harfler += harf
            else:
                gorunen_harfler += '_'
        print(gorunen_harfler)
        
        tahmin = str(input('Lütfen harfi giriniz:')).lower()

        if tahmin not in alfabe:
            print("Lütfen harfleri belirtilen alfabe içinden seçiniz >>> {}".format(alfabe))
            continue
        
        if tahmin in word:
            print("Tebrikler! Harfi bildiniz.")
            tahmin_edilenler.append(tahmin)
        else:
            print("Ne yazık ki yanlış")
            haklar -= 1   
    
        if haklar == 7:
            print(sekil0)
        elif haklar == 6:
            print(sekil1)
        elif haklar == 5:
            print(sekil2)
        elif haklar == 4:
            print(sekil3)
        elif haklar == 3:
            print(sekil4)
        elif haklar == 2:
            print(sekil5)
        elif haklar == 1:
            print(sekil6)
            
            
        if all(harf in tahmin_edilenler for harf in word):
            print("Oyunu kazandırıp adamı asımaktan kurtardığınız için adam size minnettar.")
            play_again()
            break
    else:
        print("Ne yazık ki haklarınızı tükettiniz. Kelime buydu {}.\n {} ".format(word,sekil7))
     
adam_asmaca()
    
        