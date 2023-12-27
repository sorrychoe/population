from flask import Flask, render_template, request
import pandas as pd
import numpy as np

from config.make_graph import show_graph, check_population
from models.data import load_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    try:
        pos = request.form['position']
        
        df = load_data()

        all_df = df[df.columns[0:104]]
        pivot = np.array(all_df[all_df["행정구역"].str.contains(pos)])[0] 
        res_df = check_population(all_df, pivot, pos)
                
        names = res_df.iloc[-1, 0][:-12]
        plot = show_graph(res_df, pivot)

        return render_template("result.html", result_name=names, chart_data=plot) 

    except Exception as e:
        print(e)
        return render_template("error.html")

if __name__ == "__main__":
    app.run()