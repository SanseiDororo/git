#Dependencies
import streamlit as st


from Intro.intro import intro
from Initialisation.initialisation import initialisation
from Branching.branching import branching
from Sharing.sharing import sharing
from Inspecting.inspecting import inspecting
from Merging.merging import merging
from Reseting.reseting import reseting
from Commiting.commiting import commiting

def main():
    
    menu = ['Intro', 'Initialisation', 'Branching', 'Merging', 'Reseting', 'Sharing', 'Inspecting']

    sub_page = st.sidebar.selectbox('Menu', menu)

    if sub_page == 'Intro':
        intro()
    if sub_page == 'Initialisation':
        initialisation()
    if sub_page == 'Branching':
        branching()
    if sub_page == 'Merging':
        merging()
    if sub_page == 'Reseting':
        reseting()
    if sub_page == 'Sharing':
        sharing()
    if sub_page == 'Inspecting':
        inspecting()
    else:
        pass
    


if __name__ == '__main__':
    main()