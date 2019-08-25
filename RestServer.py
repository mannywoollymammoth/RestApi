from flask import Flask, jsonify, request
from CommandLineInterface import CommandLineInterface as CLI
import DataModel as dm

app = Flask(__name__)


# will execute when a GET request is made
# we can specify the different type of CRUD stuff from here
@app.route("/records", methods=["GET"])
def getRecords():
    return data_model.records.to_json(orient='records', force_ascii=False)


# @app.route("/account/<id>", methods=["GET"])
# def getRecords(id):
#     id = int(id) - 1
#     return jsonify(accounts[id])


# @app.route("/account", methods=["POST"])
# def addAccount():
#     name = request.json['name']
#     balance = request.json['balance']
#     data = {'name': name, 'balance': balance}
#     accounts.append(data)
#
#     return jsonify(data)


if __name__ == '__main__':
    # TODO: from here call fucntions to read the files and stuff
    input_path_list = CLI().prompt()
    data_model = dm.DataModel(input_path_list)
    print(data_model.records)
    app.run(port=8080)
