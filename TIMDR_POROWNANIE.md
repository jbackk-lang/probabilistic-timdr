# Porównanie: czym jest "TIMDR" w różnych repozytoriach

Ten dokument zestawia pięć różnych użyć nazwy **TIMDR** w repozytoriach
tego samego autora (Synoptyk-v2.0, EasySound, Senscore, KHIPU,
probabilistic-timdr), żeby było jasne, że to nie jest jeden, przenośny
mechanizm stosowany w pięciu dziedzinach — to pięć różnych konstrukcji
noszących tę samą nazwę.

**Aktualizacja:** dodano `Synoptyk-v2.0` jako piąty wpis (wcześniej ten
dokument opisywał tylko cztery). Synoptyk to w istocie punkt wyjścia całej
rodziny — `analyzer/timdr_analyzer.py::TIMDRAnalyzer` liczy właśnie te
cztery sygnały (anomalia/defekt/rezonans/skręt na progach z rozstępu
p10–p90 i adaptacyjnej kalibracji klimatologicznej), które są najbardziej
"pierwotną", źródłową definicją TIMDR w tym ekosystemie — starszą i prostszą
niż jakakolwiek z pozostałych czterech, mimo że pojawia się tu jako ostatnia
pozycja w tabeli.

## Zestawienie

| Repo | Klasa/obiekt | Wejście | Co liczy | Wyjście | Wzór/reguła |
|---|---|---|---|---|---|
| **Synoptyk-v2.0** | `TIMDRAnalyzer` | szereg czasowy stacji pogodowej (temp/pressure/humidity/wind_speed/precip) | 4 niezależne sygnały: anomalię (odstęp od normy), defekt (skok), rezonans (≥3 anomalie naraz), skręt (odwrócenie trendu) | 4 listy zdarzeń (`anomalia`, `defekt`, `rezonans`, `skręt`), każda ze znacznikiem czasu i parametrem | progi z rozstępu p10-p90 (adaptacyjne, kalibrowane z danych na żywo, gdy brak klimatologii) — bez pojedynczej stałej progowej |
| **EasySound** | `TIMDRAnalyzer` | sygnał audio (próbki) | fazę chwilową sygnału analitycznego (transformata Hilberta) | ciągła wielkość Λ, statystyki (mean/median/std/max/min) | `Λ = τ/ρ + J`, gdzie `τ`=gradient fazy, `ρ`=\|gradient znormalizowanego sygnału\|, `J`=gradient τ |
| **Senscore** | `TIMDRFilter` | lista hitów detektora (energia, czas) | z-score energii + rozstęp czasowy | przefiltrowana lista hitów | odrzuć jeśli `\|z_energy\| > max_energy_deviation` (domyślnie 3.0); przytnij ogony czasowe do percentyla 10–90, jeśli rozpiętość > progu |
| **KHIPU** | `TIMDRValidator` | para (skręt S, kierunek K) węzła / cały sznur węzłów | zgodność K z regułą wyprowadzenia ze S; bilans "rosnących"/"malejących" skrętów w sznurze | bool (poprawna/niepoprawna para); bool (sznur zbalansowany) | `k == derive_direction(s)`; udział węzłów rosnących w `[0.5-(φ-1), 0.5+(φ-1)]` |
| **probabilistic-timdr** | akronim T-I-M-D-R | dowolny system progowy (paradoks urodzin, kolaps grawitacyjny) | pięć etykiet pojęciowych: Topologia/Informacja/Model/Dynamika/Rezonans | decyzja binarna: OBIEKT / SZUM | `R_total ≥ R* ⇒ OBIEKT` (R* dobierane kontekstowo — 0.5 albo 1.686) |

Ciekawostka warta odnotowania: nawet ta sama nazwa klasy (`TIMDRAnalyzer`)
powtarza się w dwóch zupełnie niepowiązanych repozytoriach (Synoptyk-v2.0 i
EasySound) i liczy dwie zupełnie różne rzeczy (progi statystyczne na
szeregu pogodowym vs transformata Hilberta na sygnale audio) — sama nazwa
klasy też nie jest wskazówką, co dany `TIMDRAnalyzer` faktycznie robi, trzeba
sprawdzić kod.

## Co z tego wynika

1. **Żadne dwie z tych pięciu definicji nie liczą tej samej rzeczy.**
   Synoptyk liczy cztery niezależne progi statystyczne (anomalia/defekt/
   rezonans/skręt) na szeregu czasowym pogody. EasySound liczy ciągłą
   wielkość z przekształcenia Hilberta na próbkach audio. Senscore odrzuca
   elementy listy na podstawie statystyki z-score. KHIPU sprawdza dyskretną
   zgodność pary symboli. probabilistic-timdr nie ma żadnego wzoru
   obliczeniowego — R_total i R* są tu etykietami pojęciowymi, nie
   wielkościami z konkretnym przepisem na policzenie.

2. **Akronim T-I-M-D-R pojawia się tylko w jednym z pięciu repozytoriów.**
   Synoptyk, EasySound i Senscore w ogóle nie rozwijają nazwy TIMDR — to po
   prostu nazwa klasy/modułu. KHIPU też nie rozwija akronimu — TIMDR tam to
   nazwa walidatora skrętu/kierunku. Rozwinięcie "Topologia-Informacja-Model-
   -Dynamika-Rezonans" jest wprowadzone dopiero w `probabilistic-timdr`
   i nie odpowiada operacyjnie żadnej z pozostałych czterech implementacji
   (np. "Topologia" nigdzie indziej nie występuje jako pojęcie, mimo że
   TIMDR tam działa).

3. **To nie jest błąd sam w sobie — ale nazwa sugeruje więcej, niż jest.**
   Nazywanie pięciu niepowiązanych konstrukcji tą samą nazwą sprawia
   wrażenie jednego, przenośnego narzędzia/prawa, które "działa" w
   meteorologii, audio, fizyce detektorów, architekturze procesora i
   kosmologii. W rzeczywistości każde repo definiuje TIMDR od nowa, pod
   swoje potrzeby. Jeśli to jest świadomy wybór stylistyczny (wspólna
   "marka" dla rodziny projektów), warto to tak właśnie nazwać wprost — np.
   jedno zdanie w każdym repo: "TIMDR tutaj oznacza X i nie jest tym samym
   mechanizmem co TIMDR w [inne repo]". To rozwiązuje problem bez usuwania
   nazwy.

4. **Synoptyk jest najbliżej "źródła"**, jeśli komuś zależy na jednym
   punkcie odniesienia: to jedyny z pięciu, który faktycznie implementuje
   (nie tylko nazywa) dokładnie te cztery sygnały (anomalia/defekt/rezonans/
   skręt), które opisuje ogólny szkielet tego ekosystemu. Pozostałe cztery
   albo liczą coś innego pod tą samą nazwą (EasySound, Senscore, KHIPU),
   albo nie liczą niczego konkretnego wcale (probabilistic-timdr, przed
   dodaniem `probabilistic_timdr/` — patrz sekcja "Kod obliczeniowy" w
   README tego repo).

## Rekomendacja

W `03_timdr_mapping.md` dodano odnośnik do tego pliku i zastąpiono
twierdzenie o TIMDR jako "naturalnym rozszerzeniu probabilistyki" (sugerujące
ciągłość z innymi repo) jawnym zestawieniem różnic. To samo warto rozważyć
w Synoptyku, KHIPU i Senscore — jedno zdanie w README każdego repo,
linkujące do tego pliku, zamiast zakładać, że czytelnik sam się domyśli, że
"TIMDR" znaczy co innego w każdym miejscu.
