#   Programme pour le pilotage de révision basé sur les notes de cours personnels
#
#   Olivier Moreau
#

import streamlit as st
import random

# Reset du jeu

def reset_jeu():
    st.session_state.choix_opérateur = []
    st.session_state.nbmath = 0
    st.session_state.noqmath = 0
    st.session_state.score_math = 0
    st.session_state.victoire = False
    st.session_state.rép_envoyé = False

    # Reset question
    st.session_state.nb1 = None
    st.session_state.nb2 = None
    st.session_state.op_symbole = None
    st.session_state.réponse_jeu = None

# Page de choix

def choix():

    st.title("Choix des opérations")

    opérateur_dispo = {
        "Addition": "add",
        "Soustraction": "sou",
        "Multiplication": "mul",
        "Division": "div"
    }

    st.session_state.choix_opérateur = []

    for nom, key in opérateur_dispo.items():
        if st.checkbox(nom, key=key):
            st.session_state.choix_opérateur.append(key)

    st.session_state.nbmath = st.number_input(
        "Combien de questions voulez-vous ?", step=1, min_value=1
    )

    if st.button("Débuter"):
        if len(st.session_state.choix_opérateur) == 0:
            st.warning("Veuillez choisir au moins une opération.")
            return

        st.session_state.choix_math = True
        st.rerun()


# Génération d'une nouvelle question

def générer_question():

    op = random.choice(st.session_state.choix_opérateur)

    nb1 = random.randint(1, 3000)
    nb2 = random.randint(1, 3000)

    if op == "add":
        symbole = "+"
        réponse = nb1 + nb2

    elif op == "sou":
        symbole = "-"
        réponse = nb1 - nb2

    elif op == "mul":
        symbole = "x"
        réponse = nb1 * nb2

    elif op == "div":
        symbole = "÷"
        réponse = nb1 / nb2

        while not réponse.is_integer():
            nb1 = random.randint(1, 3000)
            nb2 = random.randint(1, 3000)
            réponse = nb1 / nb2

        réponse = int(réponse)

    st.session_state.nb1 = nb1
    st.session_state.nb2 = nb2
    st.session_state.op_symbole = symbole
    st.session_state.réponse_jeu = réponse

    st.session_state.noqmath += 1

# Jeu

def jeu_math():

    # Générer une question seulement si aucune n'est en cours
    if st.session_state.rép_envoyé is False and st.session_state.nb1 is None:
        générer_question()

    st.subheader(f"Question {st.session_state.noqmath} sur {st.session_state.nbmath}")
    st.write(f"{st.session_state.nb1} {st.session_state.op_symbole} {st.session_state.nb2}")

    réponse_joueur = st.number_input("Votre réponse", key="réponse_joueur")

    if st.button("Soumettre la réponse"):

        st.session_state.rép_envoyé = True

        if réponse_joueur == st.session_state.réponse_jeu:
            st.success("Bravo, bonne réponse !")
            st.session_state.score_math += 1
        else:
            st.warning(f"Mauvaise réponse. La bonne réponse était : {st.session_state.réponse_jeu}")

        if st.session_state.noqmath == st.session_state.nbmath:
            st.session_state.victoire = True

        st.rerun()

    if st.session_state.rép_envoyé:

        if st.session_state.victoire:
            st.success(f"Partie terminée ! Score : {st.session_state.score_math} / {st.session_state.nbmath}")

            if st.button("Recommencer"):
                reset_jeu()
                st.session_state.choix_math = False
                st.rerun()

            if st.button("Retourner à l'accueil"):
                reset_jeu()
                st.session_state.choix_math = False
                st.switch_page("Pages/accueil.py")

        else:
            if st.button("Question suivante"):
                st.session_state.nb1 = None
                st.session_state.nb2 = None
                st.session_state.op_symbole = None
                st.session_state.réponse_jeu = None
                st.session_state.rép_envoyé = False
                st.rerun()

# ROUTAGE

if st.session_state.choix_math is False:
    choix()
else:
    jeu_math()