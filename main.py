from flask import Flask
import datetime

app = Flask(__name__)
weekdays = ["Monday :(", "Tuesday :|", "WEDNESDAY MY DUDES!!", "Thursday ;(", "Friday", "Saturday", "Sunday"]


@app.route("/")
def home():
    return "It is "  + weekdays[datetime.datetime.today().weekday()]

if __name__ == "__main__":
    app.run()