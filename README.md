Projekta apraksts:
Šis python projekts ļauj lietotājam iegūt aktuālo laika prognozi par jebkuru
izvēlētu pilsētu. Lietotājs ievada pilsētas nosaukumu un programma sākumā noskaidro
pilsētas koordinātas, kuras vēlāk izmanto mājaslapā weather.com, lai iegūtu
laika temperatūru, vēja ātrumu un laika aprakstu. Ņemot vērā, ka izmantoju 
mājaslapu angļu valodā, projektā ir izmantotas arī funkcijas, kuras pārveido 
mērvienibas.

Projekta uzdevums:
1. Atrast koordinātās lietotāja ievadītajai pilsētai, izmantojot OpenStreetMap
2. Izmantot atrastās koordinātas mājaslapā weather.com, lai noskaidrotu 
laika temperatūru, vēja ātrumu un laika aprakstu
3. Temperatūru pārvērst no Fārenheita grādiem uz Celsija grādiem un vēja ātrumu
no jūdzēm stundā uz kilometriem stundā
4. Izvadīt datus sakārtoti un apkopoti
5. Ja nepieciešams, izvadīt informāciju par to, ka nav datu

Izmantotās bibliotēkas:
requests - tiek izmantota, lai veiktu pieprasījumu HTTP lapām. Ta ļauj nosūtīt 
pieprasījumu un saņemt atbiles
BeautifulSoup - tiek izmantota, lai iegūtu datus no HTML lapām. Šī bibliotēka 
palīdz meklēt konkretas HTML sadaļas pēc dotajiem atribūtiem
re - izmanto, lai no teksta izvilktu mērvienibas

1. Programmas startēšana
Lietotājs startē programmu un tiek aicināts ievadīt pilsētas nosaukumu angļu valodā.
2. Koordinātu meklēšana
Programma automātiski nosūta pieprasījumu uz OpenStreetMap, lai 
iegūtu precīzas koordinātas.
3. Laika datu iegūšana
Ar koordinātām tiek izveidots pieprasījums uz weather.com, no kura, izmantojot 
BeautifulSoup, tiek izvilkti temperatūras, laika apraksta un vēja ātruma dati.
4. Datu apstrāde
Temperatūra tiek parveidota uz Celsija grādiem, vēja ātrums tiek pārvērsts uz km/h.
5. Izvade
Visi dati tiek izvadīti uz ekrāna saprotamā formātā ar pilsētas nosaukumu, 
temperatūru, laika aprakstu un vēja ātrumu.
6. Kļūdu apstrāde
Programma informē lietotāju, ja pilsētas koordinātas nav atrastas vai ja nav
pieejami laika dati.

