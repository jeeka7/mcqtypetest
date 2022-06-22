import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

menu=['Donate Money','Quadratic Equations Test','Result']

with st.sidebar:
  selected = option_menu(
  menu_title = None,
  icons=["piggy-bank","123","bar-chart"],
  default_index=1,
  orientation='horizontal',
  options = menu,)
  

if selected == 'Donate Money':
  st.title(f"You have chosen {selected}")
  st.write(" Kindly Donate whatever amount you feel is right to keep making such applications and tests in future")
  st.image('qrcode.png')
  url = "https://paytm.me/K1T-ra3"
  st.write("Donate Via [link](%s)" % url)

if selected == 'Quadratic Equations Test':
  score = 0
  def addscore():
    score += 3
  def subtractscore():
    score -= 1
  st.title(f"You have chosen {selected}")
  student=st.text_input("what is your name ?")
  st.write("Attempt all qustions , You get + 3 marks for correct answer , -1 marks for wrong answer and 0 for not attempting")
  st.write("Q1 : The Polynomial Equation x (x + 1) + 8 = (x + 2) (x - 2) is")
  a1=st.radio("q1",('cubic','quadratic','linear','biquadratic'),horizontal=True)
  if a1 == 'linear':
    addscore()
  elif a1 == 'cubic'or a1 =='quadratic'or a1=='biquadratic':
    subtractscore()
  st.write("your score is {}",format(score)) 
if selected == 'Result':
  st.title(f"You have chosen {selected}")
  
  #st.write("Congratulations {}, you have scored {} in your test and your Overall Rank is {}",format(   ))
