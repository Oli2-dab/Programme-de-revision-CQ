#   Programme pour le pilotage de révision basé sur les notes de cours personnels
#
#   Olivier Moreau
#

from Banque_de_question.bqmétéo import categorie_météo
import streamlit as st
import random

matière_dispo = {
        "météo" : "La météo",
#        "théorie_du_vol" : "La théorie du vol",
#        "règlementation" : "RAC",
#        "navigation" : "Nav",
    }

banque_de_thèmes = {
    "météo": categorie_météo,
#    "théorie_du_vol": categorie_TDV,
#    "règlementation": categorie_RAC,
#    "navigation": categorie_NAV
}

def choix_matière():
    # Toujours repartir d'une liste vide
    st.session_state.matière_choisie = []

    # Affichage des matières
    for matière, nom_matière in matière_dispo.items():
        st.checkbox(nom_matière, key=matière)

    # Bouton : on lit les checkboxes AVANT de changer l'étape
    if st.button("Passer au choix des thèmes"):
        for matière in matière_dispo.keys():
            if st.session_state.get(matière, False):
                st.session_state.matière_choisie.append(matière)

        if not st.session_state.matière_choisie:
            st.warning("Veuillez sélectionner des matières.")
            return

        st.session_state.etape = "choix_thèmes"
        st.rerun()

def choix_thème():
    # Toujours repartir d'une liste vide de questions
    st.session_state.bqjeu = []

    # Affichage des thèmes
    for matière in st.session_state.matière_choisie:
        for theme in banque_de_thèmes[matière].keys():
            st.checkbox(theme, key=f"{matière}_{theme}")

    # Bouton : on lit les checkboxes AVANT de changer l'étape
    if st.button("Débuter"):
        for matière in st.session_state.matière_choisie:
            for theme, questions in banque_de_thèmes[matière].items():
                if st.session_state.get(f"{matière}_{theme}", False):
                    st.session_state.bqjeu += questions

        if not st.session_state.bqjeu:
            st.warning("Veuillez sélectionner des thèmes.")
            return

        st.session_state.nbquestion = len(st.session_state.bqjeu)
        st.session_state.etape = "jeu"
        st.rerun()



def reset_jeu():
    st.session_state.bqjeu = []
    st.session_state.scoretotal = 0
    st.session_state.no_q = 0
    st.session_state.nbquestion = 0
    st.session_state.qactuel = None
    st.session_state.répval = False
    st.session_state.etape = "choix_matière"

def scoremaj(theme, question, scoreq) :
    st.session_state.scoretotal += scoreq
    
    if theme not in st.session_state.scorecat :
        st.session_state.scorecat[theme] = 0

    if theme not in st.session_state.totalcat :
        st.session_state.totalcat[theme] = 0

    if question in st.session_state.qdscore :
        qancienne = st.session_state.qdscore[question]
        st.session_state.scorecat[theme] -= qancienne

    else :
        st.session_state.totalcat[theme] += 3

    st.session_state.scorecat[theme] += scoreq
    st.session_state.qdscore[question] = scoreq

    st.session_state.répval = True

def choix_question() :

        choixq = random.choice(st.session_state.bqjeu)

        question = choixq["question"]

        réponse = choixq["réponse"]

        theme = choixq["theme"]

        st.session_state.bqjeu.remove(choixq)

        return(question, réponse, theme)

def jeu() :
    if st.session_state.no_q == st.session_state.nbquestion :
        st.subheader("Votre score par thème est de :")
        for theme, score in st.session_state.scorecat.items():
            st.write(f"{theme}: {score}/{st.session_state.totalcat[theme]}")
        st.success(f"Bravo! Votre score est de {st.session_state.scoretotal} sur {st.session_state.no_q * 3}.")
        if st.button("Retourner au choix des matières"):
            reset_jeu()
            
    st.subheader(f"Question {st.session_state.no_q + 1} sur {st.session_state.nbquestion}")

    if st.session_state.qactuel is None :
        st.session_state.qactuel = choix_question()
    question, réponse, theme = st.session_state.qactuel

    st.write(question)

    if st.session_state.répval == False :

        if st.button("Voir la réponse") :
            st.write(réponse)

        colonne1, colonne2, colonne3, colonne4 = st.columns(4)

        with colonne1 :
            if st.button("Je n'en sais rien"):
                scoreq = 0
                scoremaj(theme, question, scoreq)
                st.rerun()

        with colonne2 :
            if st.button("Je sais environ la réponse, mais je suis vraiment pas sûr"):
                scoreq = 1
                scoremaj(theme, question, scoreq)
                st.rerun()

        with colonne3 :
            if st.button("Je suis pas mal sûr de la réponse, mais je ne la connaît pas à 100%"):
                scoreq = 2
                scoremaj(theme, question, scoreq)
                st.rerun()

        with colonne4 :
            if st.button("Je connait la réponse!!!"):
                scoreq = 3
                scoremaj(theme, question, scoreq)
                st.rerun()

    if st.session_state.répval == True :
        st.warning(f"Voici la réponse : {réponse}")

        if st.button("Question suivante"):
            st.session_state.répval = False
            st.session_state.qactuel = None
            st.session_state.no_q += 1
            st.rerun()