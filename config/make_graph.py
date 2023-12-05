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