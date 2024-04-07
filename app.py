from flask import Flask, jsonify, send_file



@app.route("/",methods=['GET'])
def get_default():
    return jsonify({'result': "App Running..."})

