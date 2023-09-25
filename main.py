from flask import Flask, render_template
import pandas as pd

web = Flask(__name__)

df = pd.read_csv("dictionary.csv")


@web.route("/")
def home():
    return render_template("home.html")


@web.route("/api/v1/<word>/")
def about(word: str):
    definition = df.loc[df["word"] == word]["definition"].squeeze()
    return {"word": word, "definition": definition}


if __name__ == "__main__":
    web.run(debug=True)
