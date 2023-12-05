from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

from config.make_graph import show_graph
from models.data import load_data

app = Flask(__name__)

plt.rcParams["font.family"] = "Malgun Gothic"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    try:
        pos = request.form['position']
        
        df = load_data()

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
                
        names = res_df.iloc[-1, 0][:-12]
        plot = show_graph(res_df, pivot)

        return render_template("result.html", result_name=names, chart_data=plot) 

    except Exception as e:
        print(e)
        return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=True)