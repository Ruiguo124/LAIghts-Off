# Problématique et Thème
La pollution lumineuse change le rythme circadien et selon les docteurs chez WHO et AMA, ce changement est classifié comme étant un fort cancérogène, augmente le risque de dépression et d'obésité. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4593354/

La plus grosse source de pollution lumineuse sont les lampadaires et les feux de circulations qui sont ouvert toute la nuit et produise 50% de cette pollution. Non seulement ils sont une énorme source de consommation d'électricité, il sont également endommageant pour la santé et cache les étoiles.

# Solution
Notre projet varie la luminosité des lampadaires et des feux de circulation la nuit selon le besoin. (Rue vide -> moins de lumière, plus d'usagers -> plus de lumière). Cela permet de réduire la pollution lumineuse durant la nuit et de réduire la consommation d'électricité.

# Technologie
On a premièrement utilisé une recherche internet pour créer notre propre dataset (28 photos de bus, 40 autres). On a réduit la résolution a 40 x 70 px et mis en noir et blanc. On a feed le dataset dans notre Multi-Layered Convolution Network écrit avec Python, TensorFlow, tfLearn et opencv pour 15 epoch ce qui nous donne un accuracy de 52% avec notre dataset.

On a ensuite utilisé le modèle de detection d'objet YOLOv2 pour détecter et compter le nombre de voitures et de piétons. Avec un algorithme, on décide de la luminosité du lampadaire qu'on a simulé avec un Arduino et un LED.

# Difficulté
On a pas eu assez de temps pour obtenir un plus gros sample size pour notre CNN. Le GPU de nos ordis est également trops faible pour pouvoir utiliser ip-webcam avec un frame-rate raisonnable.

# Commercialisation/Marketing
Non seulement notre projet réduit la pollution lumineuse (population plus en santé), cela réduit la consommation électrique de la ville.

Ce qu'on a apprit YOLOv2, obtenir notre propre data avec Google, CNN avec TensorFlow et le travail d'équipe. L'analyse d'objet est une tâche qui requière une grande puissance numérique.

# À suivre
On veux accroître notre algorithme pour gérer les feux de circulations selon le traffic.

