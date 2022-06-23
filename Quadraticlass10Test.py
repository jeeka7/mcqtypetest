import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

menu=['Donate Money','Quadratic Equations Test','Result']

if 'result' not in st.session_state:
    st.session_state.result = 0


score=0

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
  def addscore():
    global score
    score = score + 3
  def DoNothing():
    pass
  def subtractscore():
    global score
    score = score - 1
  st.title(f"You have chosen {selected}")
  student=st.text_input("what is your name ?")
  st.write("Attempt all questions , You get + 3 marks for correct answer , -1 marks for wrong answer and 0 for not attempting")
  
  st.write("Q1 : The Polynomial Equation x (x + 1) + 8 = (x + 2) (x - 2) is")
  a1=st.radio("Ans.1",('cubic','quadratic','linear','biquadratic','SKIP'),horizontal=True)
  if a1 == 'linear':
    addscore()
  elif (a1 == 'cubic')or (a1 =='quadratic')or (a1=='biquadratic'):
    subtractscore()
  elif (a1 == 'SKIP'):
    DoNothing()
  st.write("Q2 : The Quadratic equation whore one rational root is 3+\u221A2 is")
  a2=st.radio("Ans.2",('x\u00b2-7x+5=0','x\u00b2+7x+6=0','x\u00b2-7x+6=0','x\u00b2-6x+7=0','SKIP'),horizontal=True)
  if a2 == 'x\u00b2+7x+6=0':
    addscore()
  elif (a2 == 'x\u00b2-7x+5=0')or(a2 =='x\u00b2-7x+6=0')or(a2=='x\u00b2-6x+7=0'):
    subtractscore()
  elif (a2 == 'SKIP'):
    DoNothing()
st.session_state.result = score
if selected == 'Result':
  st.title(f"You have chosen {selected}")
  st.write("your final score is",result) 
  #st.write("Congratulations {}, you have scored {} in your test and your Overall Rank is {}",format(   ))
