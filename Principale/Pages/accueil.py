#   Programme pour le pilotage de révision basé sur les notes de cours personnels
#
#   Olivier Moreau
#

import streamlit as st

#Page

st.title("Platforme de révision pour les cours de pilotage")

#Initialisation

initialisation = {
    "matière_choisie":[],
    "bqjeu":[],
    "etape":"choix_matière",
    "scorecat":{},
    "scoretotal":0,
    "totalcat":{},
    "qdscore":{},
    "qactuel":None,
    "no_q" : 0,
    "nbquestion":0,
    "répval":False,
    "réussite":False,
    "choix_opérateur":[],
    "nbmath":0,
    "noqmath":0,
    "score_math":0,
    "opération":"",
    "rép_envoyé":False,
    "choix_math":False,
    "victoire" :False
}

for nom, valeur in initialisation.items() :
    if nom not in st.session_state :
        st.session_state[nom] = valeur

avertissement = st.container(border = True)
avertissement.header("AVERTISSEMENT")
avertissement.write("Cette platforme est utiliser pour différent projet.")
avertissement.write("Si vous renconter des erreurs, svp m'écrire pour que je puisse les corriger et que les autres ne les rencontres pas.")

if st.button("Pour réviser la matière des différents cours") :
    st.switch_page("Pages/jeu.py")

if st.button("Pour pratiquer le calcul mental") :
    st.switch_page("Pages/math.py")

#Version

st.write("Version 1.1.44")

st.markdown("""
-**1.1.29**  
Mis à jour de la banque de question météo pour la convertir du format de l'ancien site à celui-ci.  
-**1.0.28**  
Lancement du site version publique avec la banque de question de météo.  
-**0.0.0**  
Création du site.
""")