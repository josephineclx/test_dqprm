#### Equation simplifiée
Dans le cas la cas d'une **radioembolisation**,
- toute l'activité injectée est piègée dans le foie (si pas de *shunt pulmonaire*)
- seule la décroissance physique du radionucléide intervient (pas d'élimination biologique du traceur).

Cela simplifie le calcul

$$\bar{D}_{foie} = A(0)_{foie} \times \frac{T_{phys.}}{ln\,2} \times S_{foie \leftarrow foie}$$

Dans le cas où on utilise un radionucléide qui émet **uniquement des émissions $\beta^-$**, la dernière équation est équivalente à :

$$ \bar{D}_{foie} = A(0)_{foie} \times \frac{T_{phys.} \times \Delta}{ln\,2\times m_{foie}}$$

où $\Delta$ représente **l'énergie totale émise par transition** et $m_{foie}$ la masse du foie.

En réorganisant les équations, on obtient l'activité à injecter pour une dose absorbée déterminée

$$ A(0)_{foie} = \frac{\bar{D}_{foie} \times m_{foie} \times ln\,2}{T_{phys.}\times \Delta}$$

Dans le cadre d'un traitement par radioembolisation avec des µ-sphères de verre, on souhaite délivrer une dose absorbée de 120 Gy dans **l'ensemble du foie perfusé**.

**Question 1.** Lire avec Pandas le fichier `Table.csv` contenu dans le dossier `data` qui contient les valeurs des différents volumes d'intérêt ainsi que les activités dans ces volumes (attention au format du séparateur de colonnes). La première colonne sera utilisée comme index des lignes.

**Question 2.** Ajouter une colonne au tableau avec les masses des différents volumes d'intérêt (on prendra comme valeur de masse volumique $\rho=1.03\ g/cm^3$)

**Question 3.** Déterminer l'activité à injecter dans le lobe droit pour atteindre cette dose absorbée limite en utilisant l'équation simplifiée du MIRD

**Question 4.** Déterminer la dose absorbée à la tumeur pour cette activité injectée

NB. Il n'y a pas eu de shunt pulmonaire identifié durant cette procédure

Données :
* Période de l'yttrium 90 : 64,05 $heures$
* Energie totale émise par transition : 0.9336 $\frac{MeV}{Bq.s}$
* On considère que les tissus hépatiques et la tumeur ont une masse volumique égale à 1.03 $\frac{g}{cm^3}$
