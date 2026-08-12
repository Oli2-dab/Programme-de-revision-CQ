#   Programme pour le pilotage de révision basé sur les notes de cours personnels
#
#   Olivier Moreau
#

from Banque_de_question import bqmétéo, bqnav, bqrac, bqtdv
import streamlit as st
import random

def score(theme, question) :
    st.session_state.scoretotal += st.session_state.scoreq
    
    if theme not in st.session_state.scorecat :
        st.session_state.scorecat[theme] = 0

    if theme not in st.session_state.totalcat :
        st.session_state.totalcat[theme] = 0

    if question in st.session_state.qdscore :
        qancienne = st.session_state.qdscore[question]
        st.session_state.scorecat[theme] -= qancienne

    else :
        st.session_state.totalcat[theme] += 3

    st.session_state.scorecat[theme] += st.session_state.scoreq
    st.session_state.qdscore[question] = st.session_state.scoreq

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
            st.session_state.jeulancé == False
            st.rerun()

    st.subheader(f"Question {st.session_state.no_q + 1} sur {st.session_state.nbquestion}")

    if st.session_state.qactuel is None :
        st.session_state.qactuel = choix_question()
    question, réponse, theme = st.session_state.qactuel

    st.write(question)

    if st.button("Voir la réponse") :
        st.write(réponse)

    colonne1, colonne2, colonne3, colonne4 = st.columns(4)

    with colonne1 :
        if st.button("Je n'en sais rien"):
            st.write("Voici la réponse", réponse)
            st.session_state.scoreq = 0
            score(theme, question)

    with colonne2 :
        if st.button("Je sais environ la réponse, mais je suis vraiment pas sûr"):
            st.write("Voici la réponse", réponse)
            st.session_state.scoreq = 1
            score(theme, question)

    with colonne3 :
        if st.button("Je suis pas mal sûr de la réponse, mais je ne la connaît pas à 100%"):
            st.write("Voici la réponse", réponse)
            st.session_state.scoreq = 2
            score(theme, question)

    with colonne4 :
        if st.button("Je connait la réponse!!!"):
            st.write("Voici la réponse", réponse)
            st.session_state.scoreq = 3
            score(theme, question)

    if st.session_state.répval == True :
        if st.button("Question suivante"):
            st.session_state.répval = False
            st.session_state.qactuel = None
            st.rerun()

