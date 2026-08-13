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
| 10 | 11.69% |
| 13 | 19.44% |
| 20 | 41.14% |
| 22 | 47.57% |
| **23** | **50.73%** |

Próg 50% pojawia się przy **23 osobach**.

> **Poprawka:** wartości dla N=13, 20 i 22 w poprzedniej wersji tej
> tabeli (18.74%, 37.62%, 43.57%) były błędne — nie zgadzały się
> z dokładnym wzorem `P = 1 - 365!/((365-N)!*365^N)`. Powyższe wartości
> zostały przeliczone programowo (bez zaokrągleń pośrednich) i
> zweryfikowane: dla N=23 dają znane, podręcznikowe 50.73%, co jest
> dobrym testem poprawności metody liczenia.

---

## 3. Wniosek

- relacje (pary) rosną **kwadratowo**,  
- intuicja człowieka rośnie **liniowo**,  
- dlatego 23 osoby dają ponad 50% szans na kolizję,  
- i dlatego próg 0.5 jest naturalnym **warunkiem brzegowym**.

To jest matematyczny fundament do dalszych plików TIMDR.
