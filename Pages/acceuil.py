#   Programme pour le pilotage de révision basé sur les notes de cours personnels
#
#   Olivier Moreau
#

from Banque_de_question import bqmétéo, bqtdv, bqrac, bqnav
import streamlit as st
from jeu import jeu

st.title("Platforme de révision pour les cours de pilotage")
if st.session_state.jeulancé == False :
    st.header("Choisiez la matière à réviser.")

def choix_des_questions() :

    matière_dispo = {
        "météo" : ("La météo", bqmétéo),
        "théorie_du_vol" : ("La théorie du vol", bqtdv),
        "règlementation" : ("RAC", bqrac),
        "navigation" : ("Nav", bqnav)
    }

    for matière, (nom_matière, _) in matière_dispo.items() :
        st.checkbox(nom_matière, key = matière)

    if st.button("Choisir ces matières") :
        for matière in matière_dispo.keys():
            if st.session_state[matière] :
                st.session_state.bqjeu += matière_dispo[matière][1]

        if not st.session_state.bqjeu:
            st.warning("Veuillez sélectionner des thèmes")
            return

        st.session_state.no_q
        st.session_state.nbquestion = len(st.session_state.bqjeu)
        st.session_state.jeulancé = True
        st.rerun()

if st.session_state.jeulancé == False :
    choix_des_questions()

if st.session_state.jeulancé == True :
    jeu()

avertissement = st.container(border = True)
avertissement.header("AVERTISSEMENT")
avertissement.write("Cette platforme est utiliser pour différent projet.")
avertissement.write("Si vous renconter des erreurs, svp m'écrire pour que je puisse les corrigées pour que les autres ne les rencontres pas.")

if st.session_state.jeulancé == False :
    st.write("Version 0.0.0")

    st.markdown("""
                -**0.0.0**  
                Création du site
                """)