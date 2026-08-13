# Porównanie: czym jest "TIMDR" w różnych repozytoriach

Ten dokument zestawia cztery różne użycia nazwy **TIMDR** w repozytoriach
tego samego autora (EasySound, Senscore, KHIPU, probabilistic-timdr), żeby
było jasne, że to nie jest jeden, przenośny mechanizm stosowany w czterech
dziedzinach — to cztery różne konstrukcje noszące tę samą nazwę.

## Zestawienie

| Repo | Klasa/obiekt | Wejście | Co liczy | Wyjście | Wzór/reguła |
|---|---|---|---|---|---|
| **EasySound** | `TIMDRAnalyzer` | sygnał audio (próbki) | fazę chwilową sygnału analitycznego (transformata Hilberta) | ciągła wielkość Λ, statystyki (mean/median/std/max/min) | `Λ = τ/ρ + J`, gdzie `τ`=gradient fazy, `ρ`=\|gradient znormalizowanego sygnału\|, `J`=gradient τ |
| **Senscore** | `TIMDRFilter` | lista hitów detektora (energia, czas) | z-score energii + rozstęp czasowy | przefiltrowana lista hitów | odrzuć jeśli `\|z_energy\| > max_energy_deviation` (domyślnie 3.0); przytnij ogony czasowe do percentyla 10–90, jeśli rozpiętość > progu |
| **KHIPU** | `TIMDRValidator` | para (skręt S, kierunek K) węzła / cały sznur węzłów | zgodność K z regułą wyprowadzenia ze S; bilans "rosnących"/"malejących" skrętów w sznurze | bool (poprawna/niepoprawna para); bool (sznur zbalansowany) | `k == derive_direction(s)`; udział węzłów rosnących w `[0.5-(φ-1), 0.5+(φ-1)]` |
| **probabilistic-timdr** | akronim T-I-M-D-R | dowolny system progowy (paradoks urodzin, kolaps grawitacyjny) | pięć etykiet pojęciowych: Topologia/Informacja/Model/Dynamika/Rezonans | decyzja binarna: OBIEKT / SZUM | `R_total ≥ R* ⇒ OBIEKT` (R* dobierane kontekstowo — 0.5 albo 1.686) |

## Co z tego wynika

1. **Żadne dwie z tych czterech definicji nie liczą tej samej rzeczy.**
   EasySound liczy ciągłą wielkość z przekształcenia Hilberta na próbkach
   audio. Senscore odrzuca elementy listy na podstawie statystyki z-score.
   KHIPU sprawdza dyskretną zgodność pary symboli. probabilistic-timdr nie
   ma żadnego wzoru obliczeniowego — R_total i R* są tu etykietami
   pojęciowymi, nie wielkościami z konkretnym przepisem na policzenie.

2. **Akronim T-I-M-D-R pojawia się tylko w jednym z czterech repozytoriów.**
   EasySound i Senscore w ogóle nie rozwijają nazwy TIMDR — to po prostu
   nazwa klasy. KHIPU też nie rozwija akronimu — TIMDR tam to nazwa
   walidatora skrętu/kierunku. Rozwinięcie "Topologia-Informacja-Model-
   -Dynamika-Rezonans" jest wprowadzone dopiero w `probabilistic-timdr`
   i nie odpowiada operacyjnie żadnej z pozostałych trzech implementacji
   (np. "Topologia" w EasySound/Senscore w ogóle nie występuje jako
   pojęcie, mimo że TIMDR tam działa).

3. **To nie jest błąd sam w sobie — ale nazwa sugeruje więcej, niż jest.**
   Nazywanie czterech niepowiązanych konstrukcji tą samą nazwą sprawia
   wrażenie jednego, przenośnego narzędzia/prawa, które "działa" w audio,
   fizyce detektorów, architekturze procesora i kosmologii. W
   rzeczywistości każde repo definiuje TIMDR od nowa, pod swoje potrzeby.
   Jeśli to jest świadomy wybór stylistyczny (wspólna "marka" dla rodziny
   projektów), warto to tak właśnie nazwać wprost — np. jedno zdanie w
   każdym repo: "TIMDR tutaj oznacza X i nie jest tym samym mechanizmem co
   TIMDR w [inne repo]". To rozwiązuje problem bez usuwania nazwy.

## Rekomendacja

W `03_timdr_mapping.md` dodano odnośnik do tego pliku i zastąpiono
twierdzenie o TIMDR jako "naturalnym rozszerzeniu probabilistyki" (sugerujące
ciągłość z innymi repo) jawnym zestawieniem różnic. To samo warto rozważyć
w KHIPU i Senscore — jedno zdanie w README każdego repo, linkujące do tego
pliku, zamiast zakładać, że czytelnik sam się domyśli, że "TIMDR" znaczy co
innego w każdym miejscu.
