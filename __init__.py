from flask import Flask
import datetime

counter = 0

app = Flask(__name__)
weekdays = ["Monday :(", "Tuesday :|", "WEDNESDAY MY DUDES!!", "Thursday ;(", "Friday", "Saturday", "Sunday"]


@app.route("/")
def home():
    global counter
    counter += 1
    return "<h2>It is "  + weekdays[datetime.datetime.today().weekday()] + "</h2>counter since last update:" + str(counter)

if __name__ == "__main__":
    app.run()