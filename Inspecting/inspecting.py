import streamlit as st

def inspecting():
    st.header('Inspecting')
    st.write("")
    st.write('''
            Version control system is all about changes and tracking. Git offers few tools 
            to check what has been changed localy or remotely. Moreover, it allows to move
            back and forth if neccessary. 

            ''')
            
    st.write('''''')
    st.write('''''')

    with st.expander('Inspecting & Copmparing'):
        st.write('''

            | Command                               | Description                                  |
            |---------------------------------------|----------------------------------------------|
            | git log                               | View changes                                 |
            | git log --summary                     | View changes detailes                        |
            | git log --oneline                     | View changes briefly                         |
            | git diff [source branch] [target branch]           | Preview changes before comming                              |
            | git log branch1..branch2              |Show the difference between branch2 and branch1                       |
            | git diff branch1..branch2             |Show the difference between branch2 and branch1                       |
            | git checkout -b [branch name]         | Create new branch and switch to it           |

        ''')
