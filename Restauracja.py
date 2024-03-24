import re
import random
import tkinter as tk
from PIL import Image, ImageTk
from Jadlospis import Menu
from Exceptions import checkNumber
filename = "welcome.jpg"
img = Image.open(filename)

class Klient:
    def __init__(self, imie_, nazwisko_):
        self.__imie = imie_
        self.__nazwisko = nazwisko_

    def zamow_jedzenie(self, karta_):
        karta_.pokaz_menu()
        wybrane_danie = input("Które danie z karty dań wybierasz: ")
        while True:
            if wybrane_danie in karta_.karta_dan:
                print("Dobrze, na zamówienie trzeba poczekać {} minut".format(random.randrange(5,60)))
                return False
            else:
                wybrane_danie = input("Nie ma czegoś takiego. Które danie z karty dań wybierasz: ")



    def przetlumacz_danie(self):
        self.przetlumaczona_karta = {"Makaron": "Pasta", "Rosół": "Chicken Soup", "Pierogi ruskie": "Russian dumplings","Krem pomidorowy": "Tomato cream soup", "Kurczak w sosie": "Chicken"}
        print(self.przetlumaczona_karta.keys())
        danie_do_przetlumaczenia = input("Którą nazwę dania z powyższych chcesz przetłumaczyć? ")
        while True:
            if danie_do_przetlumaczenia in self.przetlumaczona_karta:
                print(self.przetlumaczona_karta[danie_do_przetlumaczenia])
                return False
            else:
                danie_do_przetlumaczenia = input("Podaj odpowiednią nazwę: ")


    def wezwij_kierownika(self):
        kwestionariusz = tk.Tk()
        kwestionariusz.geometry("900x600")
        kwestionariusz.title("Kwestionariusz")
        wstep = tk.Label(kwestionariusz, text="Chcesz się zobaczyć z kierownikiem. Dlaczego?", font=('Times New Roman', 18))
        wstep.pack(padx=50, pady=20)
        powod1 = tk.Checkbutton(kwestionariusz, text="Niesmaczne jedzenie", font=('Times New Roman', 18))
        powod1.pack(padx=10, pady=40)
        powod2 = tk.Checkbutton(kwestionariusz, text="Niemiła obsługa", font=('Times New Roman', 18))
        powod2.pack(padx=20,pady=80)
        powod3 = tk.Checkbutton(kwestionariusz, text="Za długi czas oczekiwania", font=('Times New Roman', 18))
        powod3.pack(padx=10,pady=20)

        kwestionariusz.mainloop()

class Pracownik(Klient):
    def __init__(self,imie_,nazwisko_,wiek_,numer_telefonu_,adres_,stanowisko_,menu_):
        super().__init__(imie_,nazwisko_)
        self.__wiek = wiek_
        self.__numer_telefonu = numer_telefonu_
        self.__adres = adres_
        self.stanowisko = stanowisko_
        self.menu = menu_

    def get_numer_telefonu(self):
        return self.__numer_telefonu

    def set_numer_telefonu(self, numer_telefonu_):
        if not re.match('^[0-9 ]{9}$', numer_telefonu_):
            print("Numer telefomnu powinien składać się z 9 cyfr bez spacji.")
        self.__numer_telefonu = numer_telefonu_

    def get_adres(self):
        return self.__adres

    def set_adres(self, adres_):
        if not re.match('\Aul.', adres_):
            print("Najpierw powinna być ulica.")
        self.__adres = adres_

    def podaj_swoje_dane(self):
        print("Mój numer telefonu: {}. Mój adres: {}".format(self.__numer_telefonu,self.__adres))

    def przywitaj(self,nazwa_restauracji_):
        self.nazwa_restauracji = nazwa_restauracji_
        img.show()
        print("Witaj w naszej restauracji {}. Oto nasze menu:".format(nazwa_restauracji_))
        self.okno = tk.Tk()
        self.okno.geometry("900x600")
        self.okno.title("Menu")
        tekst1 = tk.Label(self.okno, text="Karta dań", font=('Times New Roman', 25))
        tekst1.pack(padx=50, pady=30)
        tekst2 = tk.Label(self.okno, text="Makaron", font=('Times New Roman', 18))
        tekst2.pack(padx=50, pady=20)
        tekst3 = tk.Label(self.okno, text="Rosół", font=('Times New Roman', 18))
        tekst3.pack(padx=50, pady=20)
        tekst4 = tk.Label(self.okno, text="Krem pomidorowy", font=('Times New Roman', 18))
        tekst4.pack(padx=50, pady=20)
        tekst5 = tk.Label(self.okno, text="Pierogi ruskie", font=('Times New Roman', 18))
        tekst5.pack(padx=50, pady=20)
        tekst5 = tk.Label(self.okno, text="Kurczak", font=('Times New Roman', 18))
        tekst5.pack(padx=50, pady=20)

        self.okno.mainloop()

    def pozegnaj(self):
        print("Dziękujemy za odwiedzenie nas i zapraszamy ponownie.")

        def update_gif(label, gif_frames, frame_index):
            # Aktualizacja obrazu GIF
            frame = gif_frames[frame_index]
            label.configure(image=frame)
            frame_index += 1
            if frame_index >= len(gif_frames):
                frame_index = 0

            # Planowanie kolejnej aktualizacji po określonym czasie
            label.after(100, update_gif, label, gif_frames, frame_index)

        def show_gif(filename):
            root = tk.Tk()

            # Wczytanie pliku GIF
            gif = Image.open(filename)

            # Utworzenie listy klatek GIF
            gif_frames = []
            try:
                while True:
                    gif_frames.append(ImageTk.PhotoImage(gif))
                    gif.seek(len(gif_frames))  # Przejście do kolejnej klatki
            except EOFError:
                pass

            # Utworzenie widżetu Label i przypisanie pierwszej klatki GIF
            label = tk.Label(root)
            label.pack()
            label.after(0, update_gif, label, gif_frames, 0)

            # Uruchomienie pętli głównej
            root.mainloop()

        # Wywołanie funkcji show_gif z nazwą pliku GIF
        show_gif("hello.gif")

    def polec_danie(self):
        danie_ = random.choice(self.menu.karta_dan)
        print("Dzisiejszy specjał to {}".format(danie_))

    def zatrudnij(self):
        if self.stanowisko == "kierownik":
            while True:
                    k = input("Chcesz zatrudnić tę osobę? \n\t [1] Tak \n\t [2] Nie \n\t")
                    if k == "1":
                        print("Osoba została zatrudniona.")
                        return False
                    elif k == "2":
                        print("Osoba nie została zatrudniona.")
                        return False
                    elif not re.match('[0-9]', k):
                        k = input("Powinieneś/powinnaś podać cyfrę. 1 lub 2. Spróbuj jeszcze raz: ")
                    else:
                        k = input("Co ty klikasz? Podaj 1 lub 2: ")
        else:
            print("Nie masz wystarczających uprawnień.")

    def zwolnij(self,imie_pracownika_):
        self.imie_pracownika = imie_pracownika_
        if self.stanowisko == "kierownik":
            while True:
                try:
                    k = int(input("Dlaczego chcesz zwolnić pracownika {}?. \n\t [1] Nie wywiązuje się ze swoich obowiązków. \n\t [2] Popełnił przestępstwo. \n\t [3] Bo tak. \n\t".format(self.imie_pracownika)))
                    checkNumber(k)
                except Exception as e:
                    print(e)
                else:
                    if k == 1 or k == 2:
                        print("Pracownik został zwolniony")
                        return False
                    if k == 3:
                        print("Pracownik nie może zostać zwolniony")
                        return False
                    else:
                        print("Nie masz wystarczających uprawnień.")
                finally:
                    print()


    def dodaj_do_menu(self):
        self.menu.pokaz_menu()
        danie = input("Jakie danie chcesz dodać do powyższej karty dań: ")
        while True:
            regex = r'^[a-zA-Z\D\s]+$'
            match = re.match(regex, danie)
            if danie in self.menu.karta_dan:
                danie = input("Takie danie już istnieje, dodaj inne: ")
            elif not match:
                print('Nazwa dania została niepoprawnie zapisana.')
                danie = input("Podaj nazwę dania: ")
            else:
                self.menu.karta_dan.append(danie)
                print("Tak wygląda aktualna karta dań: ")
                self.menu.pokaz_menu()
                return False

    def usun_z_menu(self):
        self.menu.pokaz_menu()
        danie_do_usuniecia = input("Które danie z wyżej wymienionych chcesz usunąć? ")
        while True:
            if danie_do_usuniecia in  self.menu.karta_dan:
                self.menu.karta_dan.remove(danie_do_usuniecia)
                print("Aktualna karta dań: ")
                self.menu.pokaz_menu()
                return False
            else:
                self.menu.pokaz_menu()
                danie_do_usuniecia = input("Nie ma nic takiego, podaj danie z karty: ")


def main():
    Karta_dan = ["Makaron", "Rosół", "Pierogi ruskie", "Krem pomidorowy", "Kurczak"]
    karta_dan = Menu(Karta_dan)

    #Pracownicy
    pracownik1 = Pracownik("Dariusz", "Malinowski", 48, 667809723, "ul. Poznańska 54", "kierownik", karta_dan)
    pracowniczka2 = Pracownik("Anita","Kuliszewska", 45, 778994222, "ul. Szczęśliwa 2", "szefowa kuchni", karta_dan)
    pracownik3 = Pracownik("Karol", "Ciesielski", 34, 143567876, "ul. Marii Konopnickiej 13",'kucharz', karta_dan)
    pracowniczka4 = Pracownik("Joanna", "Biały", 24, 804279354, "ul. Jana Śniadeckiego 85", "kelnerka", karta_dan)

    #Klienci
    klientka1 = Klient("Małgorzata", "Wąż")
    klient3 = Klient("Leon", "Wilk")
    klient4 = Klient("Melchior", "Kot")

    pracownik1.zatrudnij()
    pracowniczka4.przywitaj("Mini Dom")
    pracowniczka4.polec_danie()
    klient4.zamow_jedzenie(karta_dan)
    klient3.wezwij_kierownika()
    pracownik1.zwolnij("Anita")
    pracowniczka2.dodaj_do_menu()
    pracownik1.pozegnaj()





if __name__=="__main__":
          main()



