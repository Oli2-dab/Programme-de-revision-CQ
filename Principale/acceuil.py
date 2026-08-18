#   Programme pour le pilotage de révision basé sur les notes de cours personnels
#
#   Olivier Moreau
#

from Banque_de_question.bqmétéo import categorie_météo
import streamlit as st
from jeu import jeu, choix_matière, choix_thème

initialization = {
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
    "réussite":False
}

for nom, valeur in initialization.items() :
    if nom not in st.session_state :
        st.session_state[nom] = valeur

st.title("Platforme de révision pour les cours de pilotage")
if st.session_state.etape == "choix_matière" :
    st.header("Choisiez la matière à réviser.")

if st.session_state.etape == "choix_matière" :
    choix_matière()

if st.session_state.etape == "choix_thèmes" :
    choix_thème()

if st.session_state.etape == "jeu" :
    jeu()

avertissement = st.container(border = True)
avertissement.header("AVERTISSEMENT")
avertissement.write("Cette platforme est utiliser pour différent projet.")
avertissement.write("Si vous renconter des erreurs, svp m'écrire pour que je puisse les corrigées pour que les autres ne les rencontres pas.")

if st.session_state.etape == "choix_matière" :
    st.write("Version 1.1.29")

    st.markdown("""
    -**1.1.29**  
    Mis à jour de la banque de question météo pour la convertir du format de l'ancien site à celui-ci.  
    -**1.0.28**  
    Lancement du site version publique avec la banque de question de météo.  
    -**0.0.0**  
    Création du site.
    """)