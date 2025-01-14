#!/usr/bin/python

import json
import math
from collections import OrderedDict


# Introduce a schema and validate the JSON for more improvements.
# schema = {
#     "description": "Schema to validate the Json file is in expected format",
#     "type": "object",
#     "properties": {
#         "Volts": {"type": "float"},
#         "Current": {"type": "float"},
#         "PF": {"type": "float"},
#     },
# }

class CalcPower:
    def __init__(self):
        # Initiate a private member
        self.__power_factor = 0.9
        # Allowable names for voltage, current, and power factor
        self.v_names = {'v', 'V', 'Volts', 'Voltage'}
        self.i_names = {'i', 'I', 'Amps', 'Amperes', 'Current'}
        self.pf_names = {'pf', 'PF', 'Power Factor'}
        self.new_json = {}

    def validate_json(self, data1):
        try:
            # Dictionary objects in python have no guarenteed order.
            # Ordered dict makes sure the order is maintained.
            self.json_data = json.loads(data1.read(), object_pairs_hook=OrderedDict)
            # data = json.load(json_data)
            # validate(instance=data, schema=schema)
        except ValueError as err:
            print(err)

    def calc_power(self, volts, amps, pf):
        """ Calculates the apparent power(s),
                        the real power(p) and
                        the reactive power(q)
        """
        try:
            s = volts * amps
            p = s * (self.__power_factor if not pf else pf[0])
            q = math.sqrt(s ** 2 - p ** 2)
            return s, p, q
        except (ValueError, TypeError):
            return None, None, None

    def read_json_data(self):
        global volts, amps, pf
        allowed_names = self.v_names | self.i_names | self.pf_names
        for location, values in self.json_data.items():
            # Validate json data is in the expected format.
            # Check if data is of specific data type. Key values are in allowed names.
            # Check if power or voltage or current is not negative.
            if all(isinstance(k, str) and isinstance(v, (int, float)) and k in allowed_names and v >= 0
                   for k, v in values.items()):

                volts = [values[v] for v in self.v_names if v in values][0]
                amps = [values[i] for i in self.i_names if i in values][0]
                pf = [values[pf] for pf in self.pf_names if pf in values]

                # Call the function to calculate power.
                s, p, q = self.calc_power(volts, amps, pf)
                self.new_json[location] = {'s': s, 'p': p, 'q': q}
            else:
                raise Exception("Invalid Json data received")


# Run the program; expects a single argument which is the name of JSON file
if __name__ == "__main__":
    try:
        # with open(sys.argv[1]) as jsonData:
        f = open('data1.json', "r")
        cp = CalcPower()
        cp.validate_json(f)
        cp.read_json_data()
        print(cp.new_json)

    except Exception as exe:
        print(exe)
