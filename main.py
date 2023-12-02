import time

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

plt.rcParams["font.family"] = "Malgun Gothic"

df = pd.read_csv("data.csv", encoding="cp949", thousands=",")

def show_graph(res_df, pivot):
    away_df = res_df.iloc[:,3:]
    away=away_df.tail(1).to_numpy()[0]

    x=np.arange(0,101)
    fig = plt.figure(figsize=(20,10))

    plt.plot(x,away,'ro--')
    plt.plot(x,pivot[3:],'bo--')
    plt.xticks(np.arange(0,101,5))

    plt.grid()
    plt.legend([pivot[0],res_df.iloc[-1,0]],fontsize = 16)
    st.pyplot(fig)

def main():
    try:
        pos = st.text_input('자신이 거주하고 있는 읍,면,동의 이름을 입력하시오: ')

        df100 = df[df['행정구역'].str.contains(pos)]

        all_df = df[df.columns[0:104]]
        pivot = np.array(all_df[all_df["행정구역"].str.contains(pos)])[0]
        res_df = pd.DataFrame()
        mn = pivot[1]

        for row in np.array(all_df) :
            s = 0
            for i in range(3, len(row)) :
                tmp = np.abs(pivot[i]-row[i])
                s = s + tmp 
            if s < mn and (pos not in row[0]):
                result = []
                for i in range(3, len(row)) :
                    result.append(row[i])
                mn = s          
                result_name = row[0]
                res_df = pd.concat([res_df, all_df[all_df["행정구역"]==row[0]]])
                
        st.text(f"가장 인구 구조가 비슷한 동네 이름: {res_df.iloc[-1,0]}")
        show_graph(res_df, pivot)
        
    except:
        time.sleep(5)
        st.text("해당 하는 이름을 가진 행정 구역이 존재하지 않습니다.")
        

if __name__ == "__main__":
    main()