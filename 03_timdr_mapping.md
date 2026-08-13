# 03_timdr_mapping.md
# Mapowanie T–I–M–D–R na proces probabilistyczny

## 1. TIMDR jako struktura probabilistyczna

TIMDR można traktować jako system, w którym obiekt pojawia się dopiero wtedy,
gdy suma informacji i relacji przekracza próg kolapsu.

Elementy:

- **T — Topologia**  
  Struktura relacji. W kontekście probabilistyki: graf par, zależności, powiązań.

- **I — Informacja**  
  Rozkład prawdopodobieństwa. To, co wiemy o systemie przed kolapsem.

- **M — Model**  
  Reguła decyzyjna: jak liczymy kolaps, jakie metryki bierzemy pod uwagę.

- **D — Dynamika**  
  Jak rośnie liczba relacji wraz z N.  
  W paradoksie urodzin: relacje rosną kwadratowo.

- **R — Rezonans**  
  Wynik porównania dynamiki z progiem.  
  Odpowiednik: czy prawdopodobieństwo przekroczyło 0.5.

---

## 2. Warunek kolapsu w TIMDR

TIMDR działa jak system progowy:



\[
R_{\text{total}} \ge R_\* \Rightarrow \text{OBIEKT}
\]





\[
R_{\text{total}} < R_\* \Rightarrow \text{SZUM}
\]



Gdzie:

- \( R_{\text{total}} \) — łączny efekt T, I, M, D,  
- \( R_\* \) — stała brzegowa (odpowiednik 0.5).

---

## 3. Analogiczność do paradoksu urodzin

Paradoks urodzin:

- T — wszystkie możliwe pary  
- I — równy rozkład 365 dni  
- M — model kolizji  
- D — wzrost liczby par  
- R — prawdopodobieństwo kolizji

Kolaps następuje przy:



\[
P = 0.5 \quad \text{dla} \quad N = 23
\]



To jest dokładnie ten sam mechanizm, co w TIMDR.

---

## 4. TIMDR jako uniwersalny opis emergencji

TIMDR nie opisuje pojedynczych obiektów.  
Opisuje **moment, w którym system przechodzi z szumu do struktury**.

Dlatego:

- paradoks urodzin,  
- kolaps grawitacyjny,  
- powstawanie galaktyk,  
- strategie rynkowe,  
- modele decyzyjne  

— wszystkie podlegają tej samej logice progowej.

---

## 5. Wniosek

TIMDR jest naturalnym rozszerzeniem probabilistyki:

- T i D opisują **jak rośnie złożoność**,  
- I i M opisują **jak ją interpretujemy**,  
- R decyduje **czy system kolapsuje w obiekt**.

## 6. Uwaga: ten akronim T-I-M-D-R jest specyficzny dla tego repozytorium

**Poprawka:** nazwa "TIMDR" jest używana w kilku innych repozytoriach tego
samego autora (EasySound, Senscore, KHIPU), ale w każdym oznacza coś innego
— nie jest to ten sam mechanizm wywoływany pod różnymi postaciami, tylko ta
sama nazwa nadana czterem różnym, niepowiązanym konstrukcjom:

| Repozytorium | Co robi "TIMDR" | Typ obiektu |
|---|---|---|
| EasySound (`TIMDRAnalyzer`) | liczy Λ = τ/ρ + J na podstawie fazy sygnału analitycznego (transformata Hilberta) — wskaźnik "szorstkości fazowej" sygnału audio | ciągła wielkość liczbowa z przetwarzania sygnałów |
| Senscore (`TIMDRFilter`) | odrzuca hity detektora, których energia odstaje >3 odchylenia standardowe, i przycina ogony rozkładu czasowego | filtr statystyczny (z-score + percentyle) |
| KHIPU (`TIMDR` validator) | sprawdza, czy para (skręt S, kierunek K) węzła jest zgodna z regułą wyprowadzenia; pilnuje "zasady 1/2 i φ" | dyskretny walidator par + reguła bilansu |
| probabilistic-timdr (ten plik) | akronim T-I-M-D-R = Topologia/Informacja/Model/Dynamika/Rezonans, próg R_total ≥ R* → OBIEKT | schemat pojęciowy, nie wzór |

Żadna z tych czterech definicji nie oblicza tego samego co pozostałe, i żadna
z pozostałych trzech nie używa rozwinięcia "Topologia-Informacja-Model-
-Dynamika-Rezonans" — ten akronim pojawia się tylko tutaj. Innymi słowy:
to nie jest jeden mechanizm TIMDR zastosowany w czterech dziedzinach, tylko
cztery różne mechanizmy noszące tę samą nazwę. Jeśli intencją jest pokazanie,
że różne systemy mają jakiś próg/warunek odrzucenia (co jest prawdą i samo
w sobie jest użyteczną obserwacją), warto to tak właśnie nazwać — bez
sugerowania, że to dosłownie ten sam, przenośny algorytm. Pełne zestawienie:
`TIMDR_POROWNANIE.md`.
