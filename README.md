## 🔗 Wszystkie modele i repozytoria
Pełna lista projektów znajduje się na stronie:
https://jbackk-lang.github.io
---

# probabilistic‑timdr
Model łączący rachunek prawdopodobieństwa, warunki brzegowe i topologię TIMDR.

Repozytorium pokazuje:

- skąd biorą się progi probabilistyczne (np. 50% w paradoksie urodzin),
- dlaczego liczymy relacje (pary), a nie indywidua (osoby),
- jak próg prawdopodobieństwa staje się warunkiem kolapsu,
- jak to mapuje się na TIMDR (szum → stan krytyczny → obiekt),
- oraz jak tę samą logikę stosuje się w kosmologii (powstawanie galaktyk).

Struktura repo:

1. 01_probability_basics.md  
   Kombinacje, liczba par, paradoks urodzin, tabela prawdopodobieństw.
   *(poprawiono błędne wartości P dla N=13, 20, 22)*

2. 02_boundary_constant.md  
   Stała brzegowa 0.5 jako warunek kolapsu (urodziny → TIMDR → kosmologia).
   *(dodano zastrzeżenie: 0.5 nie jest uniwersalne — kontrprzykład z teorii perkolacji)*

3. 03_timdr_mapping.md  
   Mapowanie T–I–M–D–R na proces probabilistyczny.
   *(dodano rozdział 6: ten akronim różni się od TIMDR w innych repo — patrz TIMDR_POROWNANIE.md)*

4. 04_cosmic_application.md  
   Jak fluktuacje gęstości przekraczają próg i tworzą galaktyki.
   *(doprecyzowano: δ_crit≈1.686 to inna liczba niż 0.5, analogia strukturalna, nie tożsamość)*

5. TIMDR_POROWNANIE.md  
   Zestawienie czterech różnych definicji "TIMDR" w repozytoriach autora
   (EasySound, Senscore, KHIPU, ten projekt) — żadna z nich nie liczy tej
   samej rzeczy.

## Status poprawek

Ten model łączy trzy rodzaje twierdzeń o różnej mocy dowodowej:
- **policzalne i sprawdzone** — kombinatoryka, paradoks urodzin (po poprawce tabeli),
- **realne i poprawnie zacytowane, ale osobne** — δ_crit≈1.686 z teorii sferycznego kolapsu,
- **analogia pojęciowa, nie dowód** — twierdzenie, że różne systemy progowe
  są "tym samym mechanizmem" (TIMDR). Wzorzec "próg krytyczny" jest realny
  i częsty, ale konkretna wartość progu i wzór, którym się go liczy, są
  różne w każdej dziedzinie — tak jak różne są cztery definicje TIMDR
  w repozytoriach autora (patrz `TIMDR_POROWNANIE.md`).
