from flask import Flask, jsonify, send_file
import pandas as pd
import numpy as np
i

@app.route("/",methods=['GET'])
def get_default():
    return jsonify({'result': "App Running..."})

