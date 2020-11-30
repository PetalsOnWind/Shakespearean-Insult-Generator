from flask import Flask, render_template
import pandas as pd
import random

app = Flask(__name__)

@app.route('/hello_insult',  methods=["POST","GET"])
def hello_insult():
    df = pd.read_csv("insult_list.csv")
    max_num = df.shape[0]

    random_num1 = int(max_num*random.random())
    random_num2 = int(max_num*random.random())
    random_num3 = int(max_num*random.random())

    my_insult = "Thou "+ df.iloc[random_num1, 0] + " " + df.iloc[random_num2, 1] + " " + df.iloc[random_num3, 2] + "!"
    return render_template("index.html", insult=my_insult)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

