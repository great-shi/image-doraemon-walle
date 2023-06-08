import streamlit as st
import pandas as pd
import numpy as np
##1

# df = pd.DataFrame({
#    'first column': [1,2,3,4],
#    'second column' : [10,20,30,40]  
# })

# df

## 2

 #import numpy as np

# chart_data = pd.DataFrame(
  #  np.random.randn(20,3),#矩阵
#    columns=['a','b','c',]
# )

# st.line_chart(chart_data)

##3 有错

# map_data = pd.DataFrame(
#    np.random.randn(1000,2)/[[50,50]+37.76,-122.4],
# columns=['lat','lon']
# )
# st.map(map_data)

## 4

#滑动块 x的平方（显示结果）
# x = st.slider('x')
# st.write(x,'squared is',x * x)

## 5
#输入名字 展示出来 效果同##
# st.text_input('Enter your name',key='name')
# st.session_state['name']

## 6
#折线图 交互（勾选show展示折线图，不勾选不显示）

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns=['a','b','c']
    )
    st.line_chart(chart_data)

## 7
#敲进去什么 告诉你选择了什么
#交互式的 可以用来对客户端信息的读取 然后进行存储

# df = pd.DataFrame({
#    'first column': [1,2,3,4],
#    'second column' : [10,20,30,40]  
# })
# option = st.selectbox(
#     'Which number do you like best?',
#     df['first column'])
# 'You selected: ',option

