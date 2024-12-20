import os
import streamlit as st

import sqlite3
import pandas as pd
from dhlab.api.dhlab_api import totals
from collections import Counter
import socket

from dhlab.constants import BASE_URL
import requests
import json

import tools_corpus as tc

st.set_page_config(page_title="Trend lines", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

st.session_state.update(st.session_state)

st.sidebar.write(st.session_state.korpus_id)


corpus = st.session_state['korpus']


words =  st.text_input("trendlinjer for enkeltord", st.session_state.get('trend_words', ''), key='trend_words', help="Skriv en liste med ord adskilt med mellomrom som for eksempel 'utvandring Utvandring Demokrati demokratisk' - uten anførselstegn")

try:
    st.session_state["trendlines"] = tc.corpus_ngram(corpus, words, mode="abs")
    st.line_chart(st.session_state["trendlines"])
except:
    st.write('ingen trender')