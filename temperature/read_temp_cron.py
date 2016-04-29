#!/usr/bin/env python3
'''

When this application is called, it will read the temperature of 
the probe and print output in Farenheit.

The result is then sent to Plotly via their API.

'''

import os
import glob
import time
import plotly.plotly as py
import plotly.graph_objs as go
import json
import datetime


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
log_file = '/home/pi/raspi/temperature/output_file.log'

with open('./config.json') as config_file:
    plotly_user_config = json.load(config_file)

    py.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f

with open(log_file, "a") as myfile:
        myfile.write(time.strftime("%c") + "\t" + str(read_temp()) + '\n')


deg_f = read_temp()
time_stamp = time.strftime("%c")

data = [go.Scatter( x = time_stamp, y = deg_f)]

url = py.plot([
    {
        'x': [], 'y': [], 'type': 'scatter',
        'stream': {
            'token': plotly_user_config['plotly_streaming_tokens'][0],
            'maxpoints': 200
        }
    }], filename='Raspberry Pi Streaming Example Values')

print("View your streaming graph here: ", url)


stream = py.Stream(plotly_user_config['plotly_streaming_tokens'][0])
stream.open()

stream.write({'x': datetime.datetime.now(), 'y': deg_f})


