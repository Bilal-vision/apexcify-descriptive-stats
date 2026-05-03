import os
from flask import Flask, render_template
import pandas as pd
from sklearn.datasets import load_iris

# Explicitly set template folder to same directory as app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))

def get_stats():
    iris = load_iris(as_frame=True)
    df = iris.frame
    df["species"] = df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})
    df = df.drop(columns="target")
    df.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

    numeric_cols = df.select_dtypes(include="number").columns

    describe = df.describe().round(3)

    manual = pd.DataFrame({
        "Mean":    df[numeric_cols].mean(),
        "Median":  df[numeric_cols].median(),
        "Std Dev": df[numeric_cols].std(),
        "Min":     df[numeric_cols].min(),
        "Max":     df[numeric_cols].max(),
    }).round(3)

    groupby = df.groupby("species")[numeric_cols].mean().round(3)
    head = df.head()

    return {
        "shape": df.shape,
        "columns": list(df.columns),
        "head": head,
        "describe": describe,
        "manual": manual,
        "groupby": groupby,
    }

@app.route("/")
def index():
    stats = get_stats()
    return render_template("index.html", stats=stats)

if __name__ == "__main__":
    import webbrowser, threading
    threading.Timer(1.2, lambda: webbrowser.open("http://127.0.0.1:5000")).start()
    app.run(debug=False)
