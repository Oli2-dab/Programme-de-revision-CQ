#   Programme pour le pilotage de révision basé sur les notes de cours personnels
#
#   Olivier Moreau
#

import streamlit as st
import random

#Choix

def reset_jeu() :
    st.session_state.choix_opérateur = []
    st.session_state.nbmath = 0
    st.session_state.noqmath = 0
    st.session_state.score_math = 0
    st.session_state.opération = ""
    st.session_state.rép_envoyé = False

def choix() :

    st.session_state.choix_opérateur = []

    st.checkbox("Addition", key="+")
    st.checkbox("Soustraction", key="-")
    st.checkbox("Multiplication", key="x")
    st.checkbox("Division", key="÷")

    st.session_state.nbmath = st.number_input("Combien de question coulez vous")

    if st.button("Débuter") :
        for opérateur in choix() :
            if st.session_state.get(opérateur, False):
                st.session_state.choix_opérateur.append(opérateur)

#Jeu

def choix_nombre() :
    nb1 = random.randint(1, 3000)
    nb2 = random.randint(1, 3000)
    return(nb1, nb2)

def validation_réponse(réponse_joueur, réponse_jeu) :
    if réponse_joueur == réponse_jeu :
        st.success("Bravo, vous avez eu la bonne réponse")
        st.session_state.score_math += 1

    elif réponse_joueur != réponse_jeu :
        st.warning("Vous n'avez pas eu la bonne réponse. La bonne réponse était", réponse_jeu)

def jeu_math() :

    if st.session_state.rép_envoyé == False :

        while st.session_state.noqmath <= st.session_state.nbmath :
            st.session_state.opération = random.choice(st.session_state.choix_opérateur)

            nb1, nb2 = choix_nombre()
            st.session_state.noqmath += 1

            if st.session_state.opération == "Addition" :
                st.session_state.opération = "+"
                réponse_jeu = nb1 + nb2

            elif st.session_state.opération == "Soustraction" :
                st.session_state.opération = "-"
                réponse_jeu = nb1 - nb2

            elif st.session_state.opération == "Multiplication" :
                st.session_state.opération = "x"
                réponse_jeu = nb1 * nb2

            elif st.session_state.opération == "Division" :
                réponse_jeu = nb1 / nb2
                st.session_state.opération = "÷"
                
                while réponse_jeu.is_integer() != True :
                    nb1, nb2 = choix_nombre()
                    réponse_jeu = nb1 / nb2

            st.subheader("Question", st.session_state.noqmath, "sur", st.session_state.nbmath)
            st.write(nb1, st.session_state.opération, nb2)

            réponse_joueur = st.number_input("Votre réponse")

            if st.button("Soumettre la réponse") :
                st.session_state.rép_envoyé = True
                st.rerun()

        st.success("Bravo! Votre score est de", st.session_state.score_math, "sur", st.session_state.nbmath)

        if st.button("Recommencer") :
            reset_jeu()
            st.session_state.choix_math = False

        if st.button("Retourner à l'accueil") :
            reset_jeu()
            st.session_state.choix_math = False
            st.switch_page("Pages/accueil.py")

    elif st.session_state.rép_envoyé == True :
        validation_réponse(réponse_joueur, réponse_jeu)

        if st.button("Question suivante") :
            st.session_state.rép_envoyé = False
            st.rerun()

if st.session_state.choix_math == False :
    choix()

elif st.session_state.choix_math == True :
    jeu_math()