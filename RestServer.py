# This file is in charge of defining the APIs and returning appropriate responses
# It is also the main running point of the program and the commandline is called from here
from flask import Flask, jsonify, request
from CommandLineInterface import CommandLineInterface as CLI
import DataModel as dm


app = Flask(__name__)


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
    line = request.get_data()
    if data_model.add_line_to_record(line):
        return data_model.records.to_json(orient='records', force_ascii=False)
    else:
        return "Invalid Format"


if __name__ == '__main__':
    input_path_list = CLI().prompt()
    data_model = dm.DataModel(input_path_list)
    print(data_model.records)
    app.run(port=8080)
