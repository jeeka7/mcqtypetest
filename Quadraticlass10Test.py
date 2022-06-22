import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

menu=['Donate Money','Probability','Result']

with st.sidebar:
  selected = option_menu(
  menu_title = None,
  icons=["piggy-bank","123","bar-chart"],
  default_index=1,
  orientation='horizontal',
  options = menu,)

if selected == 'Donate Money':
  st.title(f"You have chosen {selected}")
if selected == 'Probability':
  st.title(f"You have chosen {selected}")
if selected == 'Result':
  st.title(f"You have chosen {selected}")
