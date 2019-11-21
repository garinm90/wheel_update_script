import requests
import json
import pprint

data = {"channelOutputs": [
    {"type": "universes", "enabled": 1, "startChannel": 1, "channelCount": -1, "universes": []}]}


address = "192.168.1."
controller_number = 1
start_channel = 1
universe_number = 1
universe_info = {"active": 1, "description": "", "id": 1, "startChannel": 1,
                 "universeCount": 1, "channelCount": 510, "type": 1, "address": "192.168.1.201", "priority": 0}
for i in range(1, 109):
    universe_info["startChannel"] = start_channel
    universe_info["id"] = i

    if(i == 1):
        universe_info["address"] = address + str(200 + controller_number)
    elif (i % 3 == 1):
        controller_number += 1
        universe_info["address"] = address + str(200 + controller_number)
    data["channelOutputs"][0]["universes"].append(universe_info.copy())
    start_channel += 510


for i in range(109, 119):
    universe_info["active"] = 0
    universe_info["startChannel"] = start_channel
    universe_info["id"] = i
    universe_info["type"] = 0
    universe_info["address"] = ""
    data["channelOutputs"][0]["universes"].append(universe_info.copy())
    start_channel += 510
    # print(universe_info)

universe_id = 201
controller_number = 1
counter = 119
for i in range(119, 227):
    universe_info["startChannel"] = start_channel
    universe_info["active"] = 1
    universe_info["id"] = universe_id
    universe_info["type"] = 1
    if((i - 118) == 1):
        universe_info["address"] = address + str(200 + controller_number)
    elif ((i - 118) % 3 == 1):
        controller_number += 1
        universe_info["address"] = address + str(200 + controller_number)
    data["channelOutputs"][0]["universes"].append(universe_info.copy())
    start_channel += 510
    universe_id += 1

# pprint.pprint(data)
r = requests.post("http://fpp.local/fppjson.php", json=data)
