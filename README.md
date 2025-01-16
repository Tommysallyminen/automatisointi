# automatisointi
TAK-Kurssi

Tomi Salminen
Opiskelija
S22ÄTIV
Työtehtävien automatisointi komentokielellä (TAK)

katso kuvanpolut oikein..

install python
py -m pip install autogui
pip install pillow
pip install opencv-python


Tein myös lisäosa haun mikä etsii https://rewards.bing.com/ sivulta kaikki tietyt kuvat mistä saa pisteitä, painaa niitä palaa takaisin ja näin saan lisäpisteitä.
Tein myös ohjelman joka hakee Microsoft Edge selaimesta Bing hakukonetta apuna käyttäen sanalistan sanoja (455 sanaa) Etsii listasta 10 satunnaista sanaa ja hakee näitä bingistä. Näistäkin saa microsoft reward pisteitä.


Skriptin Tarkoitus

Tämä skripti on suunniteltu automatisoimaan Microsoft Edgen avaaminen, Bing Rewards -sivustolle siirtyminen, zoomaustason säätäminen ja hakujen suorittaminen sanalistasta. Lisäksi skripti etsii ja klikkaa kuvia näytöllä.
Järjestelmävaatimukset

    Käyttöjärjestelmä: Windows

    Tarvittavat ohjelmistot:

        Python 3.x

        PyAutoGUI (asennetaan komennolla pip install pyautogui)

        Microsoft Edge -selain

    Muut vaatimukset:

        sanalista.txt-tiedosto, joka sisältää hakusanat

        Kuvatiedostot, kuten haku.png, klikkauksia varten

Siirrettävyys

Skripti on pääasiassa suunniteltu Windows-käyttöjärjestelmälle ja sisältää kovakoodattuja polkuja, jotka saattavat vaatia muokkausta eri ympäristöissä. Varmista, että kaikki polut suoritettaviin tiedostoihin ja kuvatiedostoihin ovat oikein määritettyjä.
Rajoitukset

    Skripti olettaa tietyn tiedostorakenteen ja polut, mikä voi rajoittaa sen käytettävyyttä.

    Kuvantunnistuksen varmuustaso voi vaatia säätämistä eri näyttötarkkuuksille.

    Skripti ei käsittele kaikkia mahdollisia virheitä ja reunatapauksia.

Kehitysajatukset

    Paranna virheenkäsittelyä, jotta skriptistä tulee kestävämpi ja luotettavampi.

    Tee lisää randomisointia esimerkiksi hakujen välissä ettei Microsoft tunnista sinua robotiksi.

    Lisää toiminnallisuus, joka mukautuu dynaamisesti eri näyttötarkkuuksille.

    Toteuta käyttäjäystävällinen määritystiedosto, jonka avulla käyttäjä voi asettaa polut ja muut parametrit helposti.
