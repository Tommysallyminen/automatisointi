import pyautogui as pag
import time
import subprocess
import random

# Avaa Microsoft Edge
subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'])
time.sleep(5)  # Odottaa, että selain avautuu kunnolla

# Kirjoita URL-osoite
pag.write("https://rewards.bing.com")
pag.press('enter')
time.sleep(5)  # Odottaa, että Rewards Bing avautuu
pag.hotkey('ctrl', '0')
time.sleep(3)

# Pienennä sivu 33% maksimeista
for _ in range(6):  # Joka komento pienentää sivua noin 10% (+/- riippuen selaimesta)
    pag.hotkey('ctrl', '-')
    time.sleep(0.5)  # Viive, jotta selain ehtii päivittää zoomauksen

print("Nettisivun pienentäminen suoritettu.")

# Lista klikatuista koordinaateista
clicked_positions = []

# Funktion määrittely kaikkien kuvien klikkaustoiminnolle
def click_all_images(image_path):
    try:
        # Etsi kaikki kuvat näytöltä
        locations = list(pag.locateAllOnScreen(image_path, confidence=0.9))
        
        if locations:
            for location in locations:
                # Keskipisteen koordinattien löytäminen
                point = pag.center(location)
                
                # Tarkista, onko kuvaa jo klikattu
                if point not in clicked_positions:
                    # Klikkaa keskipistettä ja lisää sijainti listaan
                    pag.click(point)
                    clicked_positions.append(point)
                    print(f"Klikkaus suoritettu kuvaan {image_path} sijainnissa {point}!")
                    time.sleep(1.5)
                    pag.hotkey('ctrl', 'f4')
                    time.sleep(2.5)  # Viive klikkausten välillä
                else:
                    print(f"Kuvaa '{image_path}' sijainnissa {point} on jo klikattu.")
        else:
            print(f"Kuvaa '{image_path}' ei löytynyt näytöltä.")
            raise pag.ImageNotFoundException  # Nosta poikkeus, jotta voimme siirtyä hakemaan sanalista
    except pag.ImageNotFoundException:
        print(f"Kuvaa '{image_path}' ei löytynyt.")
    except Exception as e:
        if "highest confidence = 0.706" in str(e):  # Tarkista erityinen virheviesti
            print(f"Kuvaa ei löytynyt korkealla varmuudella (confidence = 0.706). Siirrytään hakemaan sanalistan sanoja.")
        else:
            print(f"Tapahtui virhe: {e}")

# Funktio, joka suorittaa haut sanalistan avulla
def search_words_from_list():
    # Sanalista
    with open("sanalista.txt", "r") as sanalista:
        words = sanalista.read().splitlines()
    

    # Valitse 10 satunnaista sanaa
    random_words = random.sample(words, 10)

    # Suorittaa haku jokaisella sanalla
    for word in random_words:
        # Avaa uusi välilehti
        pag.hotkey('ctrl', 't')
        time.sleep(2)  # Odottaa, että uusi välilehti avautuu

        # Kirjoita hakusana ja suorita haku
        pag.write(word.strip())
        pag.press('enter')
        time.sleep(4)  # Odottaa, että hakutulokset latautuvat

        # Voit lisätä toimintoja hakutulosten kanssa tässä, esim. klikata kuvia

        # Sulje välilehti
        pag.hotkey('ctrl', 'w')
        time.sleep(2)  # Odottaa, että välilehti sulkeutuu

    print("Sanahakuprosessi suoritettu.")
    exit()  # Lopeta ohjelma sanalista ajettua lävitse

# Ensimmäisen haku.png kuvan klikkaus
click_all_images(r'C:\Users\Tero\Documents\GitHub\automatisointi\msrewards\haku.png')

# Odottaa hetken, jotta sivu latautuu
time.sleep(5)
search_words_from_list()  # Kutsu sanalistahakua
# Palaa takaisin edelliselle sivulle
pag.hotkey('ctrl', 'f4')
time.sleep(5)  # Odottaa, että sivu latautuu

print("Hakuprosessi suoritettu.")
