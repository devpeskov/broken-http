from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def getpost():
    qdata_msg = f'Query-data: "{request.args.get("q", "No data provided")}"\n'
    bdata_msg = f'Body-data: "{request.form.get("title", "No data provided")}"'
    return qdata_msg + bdata_msg


@app.route("/abra", methods=["ABRAKADABRA"])
def abrakadabra():
    """Custom HTTP method"""
    return "Response for Abrakadabra-method!"


@app.route("/getb", methods=["GET"])
def getbody():
    """GET-Request with body"""
    return f'Body-data: "{request.form.get("title", "No data provided")}"'


@app.route("/postq", methods=["POST"])
def postq():
    """POST-Request with query-parameters"""
    data_msg = (
        f'Query-data: query is "{request.args.get("q", "No data provided")}", '
        f'page is "{request.args.get("p", "No data provided")}"'
    )
    return data_msg


if __name__ == "__main__":
    app.run(debug=True)
