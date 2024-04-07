from flask import Flask, jsonify, send_file

app=Flask(__name__)

@app.route("/",methods=['GET'])
def get_default():
    return jsonify({'result': "App Running..."})

if   __name__ == "__main__":
    app.run(debug=False)