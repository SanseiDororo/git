import streamlit as st

def intro():
    st.header('Git Wiki')
    st.write("")
    st.write('''
            
            This git wiki stores basic information, commands and recipes
            for creating, maintaining and troubleshoting git repositories. 
            It is not meant to be a deep dive resource about git but rather 
            a quick refresher or reference.


            ''')

    st.write(''' ''')

    with st.expander('Support'):
        st.write('''

            If you like this project and you would like to support it's further development, you
            can make a donation by sending ERG, ADA or BTC to the following addresses:
            
            ###### ERG
        
                9fkAUtZsEegVyKukFAzGN89zWsoHSK7JCBcNxwgiE7oHC95AFTY

            ###### ADA
        
                addr1q8ncfqc7xa9f7qmaskyrgfln059m7srcj36jttautsnkep9nqlhalm5s3n6wyt3yq60a3uyhuws34t39qakwl6gcvvzq8nvvpfpf

            ###### BTC
        
                16T8KzvJ6LZVJSsDv6ntad3gXAESCKvb7t

          ''')

   

        
        
