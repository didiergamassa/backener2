from flask import Flask, jsonify, send_file
import pandas as pd
import numpy as np
import calendar
from calendar import monthrange

app = Flask(__name__)

# Monthly consumption data
electricity_data = pd.DataFrame({'Month': ['january','february','march','april','may','june','july','august','september','october','november','december'],
                                 'Consumption': [127000, 124000, 123000, 122000, 169000, 229000, 224000, 225000, 226000, 187000, 125000, 129000]})
gas_data = pd.DataFrame({'Month': ['january','february','march','april','may','june','july','august','september','october','november','december'],
                         'Consumption': [483470, 482500, 483400, 445000, 425000, 317000, 315000, 314000, 370000, 475000, 485000, 480000]})
water_data = pd.DataFrame({'Month': ['january','february','march','april','may','june','july','august','september','october','november','december'],
                           'Consumption': [75, 75, 77, 78, 77, 80, 82, 85, 82, 81, 86, 75]})

# Function to generate random daily consumption data for each month
def generate_daily_consumption(months, mean_consumption, std_dev):
    data = {}
    for month in months:
        year = 2023
        num_days = monthrange(year, list(calendar.month_name).index(month.capitalize()))[1]  # Get the number of days in the month
        data[month] = np.random.normal(mean_consumption, std_dev, num_days).astype(int)
    return data

# Calculate daily consumption
electricity_daily = {key: value.tolist() for key, value in generate_daily_consumption(electricity_data['Month'], mean_consumption=4000, std_dev=1000).items()}
gas_daily = {key: value.tolist() for key, value in generate_daily_consumption(gas_data['Month'], mean_consumption=2000, std_dev=500).items()}
water_daily = {key: value.tolist() for key, value in generate_daily_consumption(water_data['Month'], mean_consumption=50, std_dev=10).items()}





@app.route("/",methods=['GET'])
def get_default():
    return jsonify({'result': "App Running..."})

@app.route("/electricity")
def get_electricity_data():
    return jsonify(electricity_data.to_dict(orient='records'))

@app.route("/gas")
def get_gas_data():
    return jsonify(gas_data.to_dict(orient='records'))

@app.route("/water")
def get_water_data():
    return jsonify(water_data.to_dict(orient='records'))

@app.route("/daily_consumption_data")
def get_daily_consumption_data():
    daily_consumption_data = {'Electricity': electricity_daily,'Gas':gas_daily,'Water': water_daily}
    return jsonify(daily_consumption_data)


if   __name__ == "__main__":
    app.run(debug=False)
