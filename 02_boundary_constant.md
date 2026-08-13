# 02_boundary_constant.md
# Stała brzegowa 0.5 jako próg kolapsu

## 1. Definicja stałej brzegowej

W probabilistyce istnieje naturalna granica:



\[
p_\* = 0.5
\]



To punkt, w którym prawdopodobieństwo istnienia obiektu jest równe prawdopodobieństwu jego nieistnienia.

---

## 2. Paradoks urodzin jako przykład

Dla 23 osób:



\[
P(\text{≥1 wspólnych urodzin}) = 50.73\%
\]



To pierwszy moment, w którym system przechodzi z fazy „szum” do fazy „obiekt”.

---

## 3. Interpretacja kolapsu

Stała 0.5 działa jako warunek brzegowy:

- poniżej 0.5 → system pozostaje w superpozycji (szum),
- powyżej 0.5 → następuje kolaps (pojawia się obiekt).

To uniwersalny mechanizm w probabilistyce i systemach emergentnych.

---

## 4. TIMDR i próg kolapsu

W TIMDR definiujemy:

- \( R_{\text{total}} \) — łączny rezonans metryk,
- \( R_\* \) — próg krytyczny odpowiadający 0.5.

Warunek:



\[
R_{\text{total}} \ge R_\* \Rightarrow \text{OBIEKT}
\]




\[
R_{\text{total}} < R_\* \Rightarrow \text{SZUM}
\]



---

## 5. Dlaczego 0.5 jest naturalne — i gdzie ta naturalność się kończy

0.5 to w probabilistyce:

- punkt równowagi dla zdarzenia binarnego (jest/nie ma kolizji),
- punkt maksymalnej entropii rozkładu Bernoulliego H(p), rzeczywiście
  maksymalizowanej dokładnie przy p=0.5 — to jest twierdzenie, nie metafora,
- w paradoksie urodzin: wartość, przy której P(kolizja) po raz pierwszy
  przekracza 1/2 (N=23).

**Poprawka:** 0.5 NIE jest uniwersalną stałą progową dla dowolnego systemu
przejścia fazowego — to częsty błąd nadinterpretacji. Kontrprzykład z teorii
perkolacji: próg krytyczny p_c zależy od geometrii sieci i rzadko wynosi
dokładnie 0.5:

| Sieć / typ perkolacji | p_c |
|---|---|
| kwadratowa, wiązaniowa | **0.5** (dokładnie — z samodualności sieci, dowód Kestena 1980) |
| trójkątna, węzłowa | **0.5** (dokładnie — z dualności dopasowanej sieci) |
| trójkątna, wiązaniowa | ≈0.347 |
| sześciokątna, wiązaniowa | ≈0.653 |
| kwadratowa, węzłowa | ≈0.593 (brak wzoru zamkniętego) |
| sześcienna 3D, wiązaniowa | ≈0.249 (brak wzoru zamkniętego) |

0.5 pojawia się tylko tam, gdzie da się je wyprowadzić z konkretnej symetrii
(samodualność sieci, definicja zdarzenia w paradoksie urodzin) — nie jako
domyślna stała każdego progu. W kosmologii (`04_cosmic_application.md`)
analogiczny próg krytyczny wynosi δ_crit ≈ 1.686, nie 0.5 — to inna liczba,
z innego wyprowadzenia (teoria sferycznego kolapsu), pełniąca **analogiczną
rolę** (próg między "szumem" a "obiektem"), a nie tę samą wartość liczbową.

Dlatego poprawniej jest powiedzieć: **stała brzegowa 0.5 jest fundamentem
konkretnie w paradoksie urodzin** (bo stamtąd się wyprowadza), a nie
uniwersalnym fundamentem probabilistyki czy TIMDR w ogóle. Rola "progu
krytycznego" jest uniwersalna jako *wzorzec* (wiele systemów ma jakiś próg),
ale konkretna wartość 0.5 nie jest.
