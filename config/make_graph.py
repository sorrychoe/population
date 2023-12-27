import pandas as pd
import numpy as np
import json

def show_graph(res_df, pivot):
    away_df = res_df.iloc[:, 3:]
    away = away_df.tail(1).to_numpy()[0]

    x = np.arange(0, 101)

    chart_data = {
        "labels": x.tolist(),
        "datasets": [
            {
                "label": pivot[0],
                "data": away.tolist(),
                "backgroundColor": "rgba(255, 99, 132, 0.2)",
                "borderColor": "rgba(255, 99, 132, 1)",
                "borderWidth": 1,
                "pointBackgroundColor": "rgba(255, 99, 132, 1)",
                "pointRadius": 5
            },
            {
                "label": res_df.iloc[-1, 0],
                "data": pivot[3:].tolist(),
                "backgroundColor": "rgba(54, 162, 235, 0.2)",
                "borderColor": "rgba(54, 162, 235, 1)",
                "borderWidth": 1,
                "pointBackgroundColor": "rgba(54, 162, 235, 1)",
                "pointRadius": 5
            }
        ]
    }

    return json.dumps(chart_data)


def check_population(df, pivot, pos):
    res_df = pd.DataFrame()
    mn = pivot[1]
        
    for row in np.array(df) :
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
            res_df = pd.concat([res_df, df[df["행정구역"]==row[0]]])
    return res_df