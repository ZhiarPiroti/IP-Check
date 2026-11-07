from flask import Flask, render_template, jsonify, request
from calculation import *
from flask_cors import CORS

from ping import ping_


app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/info", methods=["POST"])
def info():
    data = request.get_json()
    ip = data.get('ip')
    nc = network_class(ip)
    net_id, host_id = identity(ip)
    net_address = network_(net_id, "0")
    broadcast = network_(net_id, "255")
    submask = subnetmask(net_id)

    result = {
        'ip': ip,
        'class': nc,
        'networkId': net_id,
        'hostId': host_id,
        'networkAddr': net_address,
        'broadcast': broadcast,
        'subnetMask': submask,
    }
    return jsonify(result), 200

@app.route("/ping", methods=["POST"])
def ping():
    data = request.get_json()
    ip = data.get('ip')
    res = ping_(ip, "-n")
    if res:
        return jsonify({"ping": True})
    else:
        return jsonify({"ping": False})
app.run()