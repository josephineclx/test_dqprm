## Exercice 3 - Dosimétrie
-----------

### Contexte
**Radioembolisation** dans le traitement d'un cancer hépatique à l'aide de **microsphères de verre** marquées à l'$^{90}Y$.

Planification de l'activité à administrer à l'aide d'une acquisition tomographique réalisée au $^{99m}Tc$-MAA

- Déterminer l'activité d'$^{90}Y$ pour délivrer une dose absorbée limite de 120 Gy au lobe hépatique contenant la tumeur
- Déterminer la dose absorbée à la tumeur

Pour illustrer le propos de l'impact de la dosimétrie prévisionnelle dans le traitement des hépatocarcinome, voir [ici](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4731431/#!po=84.5455).

### Modéle de partionnement

[Ho et al.](https://www.ncbi.nlm.nih.gov/pubmed/8753684) ont défini un modèle de calcul basée sur la connaissance de **la répartition de l'activité** dans le foie après la perfusion des microsphères radioactives. Le calcul de la dose absorbée aux  volumes d'intérêt est estimée par la méthologie du *MIRD*.

L'activité perfusée dans le foie se répartie dans lui-même et les poumons s'il existe un *shunt* entre ce premier et ces derniers.

- L'activité dans les poumons est estimée par $A_L = A_{inj.} \times \frac{L}{100}$
    - L pourcentage de shunt pulmonaire
- L'activité dans le foie comprenant la partie saine ($A_N$) et tumorale ($A_T$) est estimée par $A_N+A_T = A_{inj.} (1-\frac{L}{100})$
- Le rapport tumeur/foie sain $r=\frac{\frac{A_T}{m_T}}{\frac{A_N}{m_N}}$ peut être estimé à partir des pseudo-concentrations d'activité mesurées par la segmentation dans la tumeur et le foie sain. A l'aide de l'équation précédente, on peut ensuite exprimer les activités dans le foie sain ($A_N$) et dans la tumeur ($A_T$) en fonction de ce rapport et de $A_{inj.}$.

### Rappels

#### Equation du MIRD

$$ \bar{D}_{k \leftarrow h} = \sum_{h} \tilde{A}_{h} \times S_{k \leftarrow h} $$

où $\tilde{A}_{h}$ est l'activité cumulée dans la source i.e: le **nombre total de désintégration dans la source h** et $S_{k \leftarrow h}$ **le facteur S** liant la source h à la cible k.