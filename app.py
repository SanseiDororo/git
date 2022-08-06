#Dependencies
import streamlit as st


from Intro.intro import intro
from Initialisation.initialisation import initialisation


def main():
    
    menu = ['Intro', 'Initialisation']

    sub_page = st.sidebar.selectbox('Menu', menu)

    if sub_page == 'Intro':
        intro()
    if sub_page == 'Initialisation':
        initialisation()
    else:
        pass
    


if __name__ == '__main__':
    main()