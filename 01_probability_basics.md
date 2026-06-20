# 01_probability_basics.md
# Podstawy prawdopodobieństwa w kontekście TIMDR

## 1. Dlaczego liczymy pary, a nie osoby

Para to nie „połowa osoby”.  
Para to **dowolne dwie osoby wybrane z grupy**.

Dlatego liczba par w grupie N osób to:



\[
\binom{N}{2} = \frac{N(N-1)}{2}
\]



To jest fundament całego paradoksu urodzin.

Przykłady:

| N osób | liczba par |
|-------|------------|
| 2 | 1 |
| 3 | 3 |
| 4 | 6 |
| 5 | 10 |
| 13 | 78 |
| 23 | 253 |

---

## 2. Paradoks urodzin — prawdopodobieństwo kolizji

Prawdopodobieństwo, że **co najmniej dwie osoby** mają urodziny tego samego dnia:

| N osób | P(≥1 wspólnych urodzin) |
|--------|--------------------------|
| 2 | 0.27% |
| 5 | 2.71% |
| 10 | 11.70% |
| 13 | 18.74% |
| 20 | 37.62% |
| 22 | 43.57% |
| **23** | **50.73%** |

Próg 50% pojawia się przy **23 osobach**.

---

## 3. Wniosek

- relacje (pary) rosną **kwadratowo**,  
- intuicja człowieka rośnie **liniowo**,  
- dlatego 23 osoby dają ponad 50% szans na kolizję,  
- i dlatego próg 0.5 jest naturalnym **warunkiem brzegowym**.

To jest matematyczny fundament do dalszych plików TIMDR.
