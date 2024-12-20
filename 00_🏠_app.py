import streamlit as st
from PIL import Image
import urllib
import pandas as pd
import dhlab as dh
import streamlit as st


@st.cache_data()
def corpus(file):
    c = pd.read_pickle(file)
    c['url'] = c.urn.apply(lambda x: f"https://nb.no/items/{x}")
    return c



st.set_page_config(page_title="Terjes app", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)



st.session_state.update(st.session_state)

corpus_select = st.selectbox("Velg et korpus fra listen", 
                              options = [
                                  "terje_aviser_demokrati.pkl", 
                                  "terje_storting_demokrati.pkl",
                                  "terje_tidsskrift_demokrati.pkl",
                                  "terje_bok_demokrati.pkl"
                              ])


litt_korpus = corpus(corpus_select)

st.session_state['korpus'] = litt_korpus
st.session_state['dhlabid'] = [int(x) for x in litt_korpus.dhlabid]
st.session_state["korpus_id"] = corpus_select
st.sidebar.write(st.session_state.korpus_id)

st.title("Oversikt over korpuset")
st.write("Klikk på lenkene for å gå til Nettbiblioteket. Velg en oppgave fra sidemenyen, finn konkordanser, se på trendlinjer eller bygg en kollokasjon. Sjekk ut https://dh.nb.no mer om DH-lab og tekstanalyse")

st.write(f"Det er {len(litt_korpus)} dokument totalt i {corpus_select}")

st.dataframe(
    litt_korpus[['url','title', 'authors','year']],
    column_config={
            "url": st.column_config.LinkColumn("URL")
    },
    hide_index=True
)

    
        