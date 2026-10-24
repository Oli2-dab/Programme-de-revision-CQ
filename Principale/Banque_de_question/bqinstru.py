#   Programme pour le pilotage de révision basé sur les notes de cours personnels
#
#   Olivier Moreau
#

TRE = [
    {"theme" : "theore", "question" : "Qu'est-ce qu'une onde?", "réponse" : "Une fréquence électromagnétique qui se déplace, avec une osillation."},
    {"theme" : "theore", "question" : "Comment ce nomme le bas de l'osillation?", "réponse" : "Creux"},
    {"theme" : "theore", "question" : "Comment ce nomme le haut de l'osillation?", "réponse" : "Crête"},
    {"theme" : "theore", "question" : "Quel est l'autre nom d'un cycle lorsqu'on parle d'une onde?", "réponse" : "Une période"},
    {"theme" : "theore", "question" : "Comment ce nomme la distance d'un cycle de l'onde?", "réponse" : "Une longueur d'onde"},
    {"theme" : "theore", "question" : "Quel est l'unité de mesure, normalement utilisé, de la longueur d'onde?", "réponse" : "Le mètre"},
    {"theme" : "theore", "question" : "Une onde qui a une grande longueur d'onde a _____ d'énergie?", "réponse" : "peu"},
    {"theme" : "theore", "question" : "Une onde qui a une petite longueur d'onde a _____ d'énergie?", "réponse" : "beaucoup"},
    {"theme" : "theore", "question" : "Qu'est-ce que l'amplitude d'une onde?", "réponse" : "La distance entre le centre de l'onde et un creux/crête"},
    {"theme" : "theore", "question" : "Qu'est-ce que la phase d'une onde?", "réponse" : "La veleur atteinte dans une période à un instant (temps)"},
    {"theme" : "theore", "question" : "Quelle est l'unité de mesure de la phase d'une onde?", "réponse" : "Le degré"},
    {"theme" : "theore", "question" : "Qu'est-ce que la fréquence d'une onde?", "réponse" : "Le nombre de période par seconde"},
    {"theme" : "theore", "question" : "Qu'est-ce que le déphasage?", "réponse" : "La différence entre les phases de deux ondes"},
    {"theme" : "theore", "question" : "Quel est l'unité de mesure de la fréquence?", "réponse" : "Le Hertz (Hz)"},
    {"theme" : "theore", "question" : "À quoi équivaut 1 Hz?", "réponse" : "Un cycle par seconde"},
    {"theme" : "theore", "question" : "Dans la formule de la vitesse de l'onde, à quoi équivaut c?", "réponse" : "300 000 000 m/s"},
    {"theme" : "theore", "question" : "Si la fréquence d'un VOR est de 114,2 MHz, quelle est sa longueur d'onde?", "réponse" : "2,63m"},
    {"theme" : "theore", "question" : "Quel est la fréquence, la longueur d'onde et des utilitées d'une fréquence LF?", "réponse" : "30 kHz à 300 kHz, 10km à 1km, NDB"},
    {"theme" : "theore", "question" : "Quel est la fréquence, la longueur d'onde et des utilitées d'une fréquence MF?", "réponse" : "300 kHz à 3 MHz, 1km à 100m, NDB, Radio AM"},
    {"theme" : "theore", "question" : "Quel est la fréquence, la longueur d'onde et des utilitées d'une fréquence HF?", "réponse" : "3 MHz à 30 MHz, 100m à 10m, Communication pour les vols long courrier, Radio-identification"},
    {"theme" : "theore", "question" : "Quel est la fréquence, la longueur d'onde et des utilitées d'une fréquence VHF?", "réponse" : "30 MHz à 300 MHz, 10m à 1m, Radio FM, Télévision, Communication radio avion, VOR, ILS"},
    {"theme" : "theore", "question" : "Quel est la fréquence, la longueur d'onde et des utilitées d'une fréquence UHF?", "réponse" : "300 MHz à 3 GHz, 1m à 10cm, GSM, GPS, Wi-Fi, ILS, Certains radar"},
    {"theme" : "theore", "question" : "Qu'est-ce que l'atténuation?", "réponse" : "La perte d'intensité d'un signal à mesure que la distance augmente. Plus l'onde va loin, plus elle va perdre de l'énergie, ce qui va altérer sa fréquences"},
    {"theme" : "theore", "question" : "Quels sont les causes de l'atténuation en parlant d'une onde?", "réponse" : "L'espace est de plus en plus grand et la dissipation dans le sol, dans l'atmosphère et dans les couches ionisées en altitude."},
    {"theme" : "theore", "question" : "L'environement affecte une onde. Entre l'eau et la terre, sur quelle surface l'onde ira-t-elle le plus loin?", "réponse" : "L'eau"},
    {"theme" : "theore", "question" : "Quel est la formule de la relation entre la portée et la puissamce d'une onde?", "réponse" : "Portée = √Puissance"},
    {"theme" : "theore", "question" : "Si on quadruple la puissance de l'émetteur, que va-t-il se passer au niveau de la portée de l'onde?", "réponse" : "Elle va doubler"},
    {"theme" : "theore", "question" : "Qu'est-ce que la réfraction et donne moi des exemple d'endroit où il peut y avoir de la réfraction?", "réponse" : "Un changement de direction qui passe d'un milieu à un autre, ou de densité différente. Exemple : Réfraction atmosphérique (température, pression et humidité), Réfraction côtière et Réfraction ionosphérique."},
    {"theme" : "theore", "question" : "Qu'est-ce que l'Ionosphère?", "réponse" : "Une couche qui varie entre la thermosphère et la mésophère. C'est une couche ionisé où il y a les aurores boréales. C'est une couche qui réfléchit certaines ondes radios."},
    {"theme" : "theore", "question" : "Quelle couche de l'Ionosphère apparait et disparait selon le moment de la journée et quelle est son influence sur les ondes?", "réponse" : "La région D et, puisqu'elle bouge selon le moment de la journée, les ondes ne sont jamais réfléchies de la même façon."},
    {"theme" : "theore", "question" : "Qu'est-ce que l'onde de sol ou onde de surface?", "réponse" : "Un signal qui suit la surafce de la terre, selon la fréquence de l'onde. Elle n'est pas affecter par les perturabations de la Ionosphère. Le signal est plus rapidement absorbée par la terre que l'eau, selon sa fréquence elle est plus ou moins absorbée. Les basses fréquences sont moins atténuées, donc meilleur protée, fréquence ≤ 1000 kHz (ELF, SLF, ULF, VLF et LF)"},
    {"theme" : "theore", "question" : "Qu'est-ce que l'onde ionosphérique ou de ciel?", "réponse" : "Une onde réfléchies par la Ionospère. Elle est donc influencé par la position de cette dernière. Fréquence de 1 MHz à 30 MHz = HF et dernière partie de MF. Difficile à utiliser pour la navigation précise, car trajectoire de l'onde est variable. Très affectées par les perturbations solaires. Affectée aussi par les nuages, les inversions et les lignes électriques."},
    {"theme" : "theore", "question" : "Qu'est-ce que l'onde direct ou d'espace?", "réponse" : "Signal qui se propage en ligne droite. Il n'est pas réfléchit par la Ionoshère. Peux subir une réflexion totale interne s'il y a une très forte inversion. Fréquence au-delà de 100 MHz (VHF, VOR, DME, GPS, etc.) Dans les basses fréquences, le signal tant à courber. Exemple, le VOR = 108 à 118 MHz et DME = 962 à 1213 MHZ. Donc, perte du DME en premier"},
    {"theme" : "theore", "question" : "Quel est la formule pour calculer la potée d'une onde, dans les examens de Steve?", "réponse" : "Portée (nm) = 1.25 x √altitude (pi)"},
    {"theme" : "theore", "question" : "VLF est une onde de ___?", "réponse" : "Sol et Ciel"},
    {"theme" : "theore", "question" : "LF est une onde de ___?", "réponse" : "Sol de joue et Sol et Ciel la nuit"},
    {"theme" : "theore", "question" : "MF est une onde de ___?", "réponse" : "Sol de joue et Sol et Ciel la nuit"},
    {"theme" : "theore", "question" : "HF est une onde de ___?", "réponse" : "Principalement de Ciel, de jour et de nuit"},
    {"theme" : "theore", "question" : "VHF, UHF et SHF est une onde de ___?", "réponse" : "d'Espace"},
    {"theme" : "theore", "question" : "Qu'est-ce que l'effet de canal?", "réponse" : "Lorsqu'il y a une inversion de température et une chute rapide du taux d'humidité avec l'altitude (changement de densité) les fréqunecs supérieurs à 30 MHz sont réfléchies"},
    {"theme" : "theore", "question" : "Qu'est-ce qu'une onde entertenue ou onde porteuse?", "réponse" : "Une onde émis en continue"},
    {"theme" : "theore", "question" : "Qu'est-ce qu'une onde manipulées?", "réponse" : "Une onde où on coupe une partie de l'onde, un peu comme le code morse"},
    {"theme" : "theore", "question" : "Qu'est-ce que la modulation d'amplitude?", "réponse" : "L'amplitude d'une onde est modifiée pour coder et décoder de l'information (Exemple, les radios AM encode le son en modifiant l'amplitude)"},
    {"theme" : "theore", "question" : "Qu'est-ce que la modulation de fréquence?", "réponse" : "L'information est encoder en utilisant la modulation de fréquence, soit en modifiant la fréquence de l'onde. Par exemple, l'ELT à beaucoup d'énergie. Donc, son signal va dépassé sur les fréquences autour de 121.5 MHz. De plus, nous ne somme pas capable de décode le DME. Donc, le DME utilise la modulation de fréquence pour moduler une fréquence UFH en VHF."},
    {"theme" : "theore", "question" : "Qu'est-ce qu'une zone de silence?", "réponse" : "Une zone où les ondes ne se rendent plus"},
    {"theme" : "theore", "question" : "Qu'est-ce que l'angle limite en propagation?", "réponse" : "L'angle à partir duquel une fréquence précise va rebondir sur ou passer au travers de quelque chose."},
    {"theme" : "theore", "question" : "Qu'est-ce que la fréquence critique?", "réponse" : "La fréquence à partir de laquelle l'onde va rebondir sur ou passer au travers de quelque chose."},
    {"theme" : "theore", "question" : "Qu'est ce que le <<Fade-Out>>?", "réponse" : "L'atténuation du signal dû à différent élément."},
    {"theme" : "theore", "question" : "Qu'est-ce que le squelsh sur une radio?", "réponse" : "Le filtre de <<Fade-Out>> électonique."},
]

# {"theme" : "", "question" : "?", "réponse" : ""},

categorie_instru = {
    "theore" : (TRE, "Théorie sur la radio électricité"),

}