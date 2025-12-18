from flask import Flask, Response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    return Response("id_list_message=t-החיבור עובד", mimetype="text/plain")
