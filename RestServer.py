from flask import Flask, jsonify, request
from CommandLineInterface import CommandLineInterface as CLI
import DataModel as dm

app = Flask(__name__)


# will execute when a GET request is made
# we can specify the different type of CRUD stuff from here
@app.route("/records", methods=["GET"])
def get_records():
    return data_model.records.to_json(orient='records', force_ascii=False)


@app.route("/records/gender", methods=["GET"])
def get_gender_records():
    gender_records = data_model.sort_by_gender()
    return gender_records.to_json(orient='records', force_ascii=False)


@app.route("/records/birthdate", methods=["GET"])
def get_bday_records():
    bday_records = data_model.sort_by_birthdate()
    return bday_records.to_json(orient='records', force_ascii=False)


@app.route("/records/name", methods=["GET"])
def get_name_records():
    name_records = data_model.sort_by_name()
    return name_records.to_json(orient='records', force_ascii=False)


@app.route("/records", methods=["POST"])
def add_record():
    # name = request.json['name']
    # balance = request.json['balance']
    # data = {'name': name, 'balance': balance}
    # accounts.append(data)
    print(request.get_data())
    return request.get_data()
    # return jsonify(data)


if __name__ == '__main__':
    # TODO: from here call fucntions to read the files and stuff
    input_path_list = CLI().prompt()
    data_model = dm.DataModel(input_path_list)
    print(data_model.records)
    app.run(port=8080)
