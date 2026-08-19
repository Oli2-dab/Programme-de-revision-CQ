#   Programme pour le pilotage de révision basé sur les notes de cours personnels
#
#   Olivier Moreau
#

import streamlit as st

navigation = st.navigation([
    st.Page("accueil.py", title = "Page d'accueil"),
    st.Page("activité/jeu.py", title = "Pour réviser la matière des différents cours"),
    st.Page("activité/math.py", title = "Pour pratiquer les maths sans calculatrice"),
])

navigation.run()