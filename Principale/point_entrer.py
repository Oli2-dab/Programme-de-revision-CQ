#   Programme pour le pilotage de révision basé sur les notes de cours personnels
#
#   Olivier Moreau
#

import streamlit as st

st.set_page_config(page_title="Révision des cours du CQ")

navigation = st.navigation([
    st.Page("Pages/accueil.py", title = "Page d'accueil"),
    st.Page("Pages/jeu.py", title = "Pour réviser la matière des différents cours"),
    st.Page("Pages/math.py", title = "Pour pratiquer les maths sans calculatrice"),
])

navigation.run()