import os
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

cwd = os.getcwd()
sequence_path = os.path.join(cwd, "Sequences")


controller_addresses = {"controller_" +
                        str(i): "http://192.168.1."+str(i) for i in range(201, 204)}

form_e131_data = {
    # Total Number of Uninverse
    "z": "6",
    # Addressing Mode: {0: Absolute, 1: Universe/Start Channel}
    "a": "1",
    # Blanking Timeoute
    "B": "5",
    "btnSave": "Save",
    # {Universe Key, Universe Number}, {Channel Key, Starting Channel Number}, {Univere Size Key: Size}, {Type Key (0=E131): 0}
    "u0": "1", "c0": "1", "s0": "510", "t0": "0",
    "u1": "2", "c1": "511", "s1": "510", "t1": "0",
    "u2": "3", "c2": "1021", "s2": "510", "t2": "0",
    "u3": "201", "c3": "1531", "s3": "510", "t3": "0",
    "u4": "202", "c4": "2041", "s4": "510", "t4": "0",
    "u5": "203", "c5": "2551", "s5": "510", "t5": "0"
}

form_string_ports = {"m": "0",
                     "S": "6", "a": "1", "q": "0", "r": "1",
                     "k0": "1024", "k1": "0", "k2": "0",
                     "p0": "0", "g0": "1", "s0": "1", "c0": "114", "d0": "0", "o0": "0", "t0": "1", "n0": "0", "z0": "0", "b0": "0", "B0": "0", "u0": "7", "y0": "",
                     "p1": "1", "g1": "1", "s1": "1", "c1": "81", "d1": "0", "o1": "0", "t1": "1", "n1": "0", "z1": "0", "b1": "0", "B1": "0", "u1": "8", "y1": "",
                     "p2": "1", "g2": "1", "s2": "1", "c2": "32", "d2": "0", "o2": "0", "t2": "1", "n2": "0", "z2": "0", "b2": "0", "B2": "0", "u2": "9", "y2": "",
                     "p3": "2", "g3": "1", "s3": "1", "c3": "114", "d3": "0", "o3": "0", "t3": "1", "n3": "0", "z3": "0", "b3": "0", "B3": "0", "u3": "207", "y3": "",
                     "p4": "3", "g4": "1", "s4": "1", "c4": "81", "d4": "0", "o4": "0", "t4": "1", "n4": "0", "z4": "0", "b4": "0", "B4": "0", "u4": "208", "y4": "",
                     "p5": "3", "g5": "1", "s5": "1", "c5": "32", "d5": "0", "o5": "0", "t5": "1", "n5": "0", "z5": "0", "b5": "0", "B5": "0", "u5": "209", "y5": ""}


def get_controller_string_ports(controller_number, form_string_ports):
    form_string_ports["u0"] = str(controller_number * 3 - 2)
    form_string_ports["u1"] = str(controller_number * 3 - 1)
    form_string_ports["u2"] = str(controller_number * 3)
    form_string_ports["u3"] = str((controller_number * 3 - 2) + 200)
    form_string_ports["u4"] = str((controller_number * 3 - 1) + 200)
    form_string_ports["u5"] = str((controller_number * 3) + 200)
    return form_string_ports


def get_controller_e131(controller_number, form_e131_data):
    form_e131_data["u0"] = str(controller_number * 3 - 2)
    form_e131_data["u1"] = str(controller_number * 3 - 1)
    form_e131_data["u2"] = str(controller_number * 3)
    form_e131_data["u3"] = str((controller_number * 3 - 2) + 200)
    form_e131_data["u4"] = str((controller_number * 3 - 1) + 200)
    form_e131_data["u5"] = str((controller_number * 3) + 200)
    return form_e131_data


for file in os.listdir(sequence_path):
    upload_file = open(os.path.join(sequence_path, file), "rb")
    print(f"Uploading {file} to controller please wait.....")
    r = requests.post(
        "http://fpp.local/api/sequence/" + file, data=upload_file)
    print(f"Upload of {file} completed.")


# for i, v in enumerate(controller_addresses.values()):
#     controller_number = i + 1
#     form_data = get_controller_e131(controller_number, form_e131_data)
#     r = requests.post(v + "/E131.htm", data=form_data)
#     form_data = get_controller_string_ports(
#         controller_number, form_string_ports)
#     r = requests.post(v + "/StringPorts.htm", data=form_data)
