"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    with open(neo_csv_path, 'r') as infile:
        neos_obj = csv.DictReader(infile)
        neos_list = []

        for neos in neos_obj:
            if neos['name'] == '':
                neos['name'] = None

            if neos['diameter']:
                neos['diameter'] = float(neos['diameter'])
            else:
                neos['diameter'] = float('nan')

            if neos['pha'] == 'Y':
                neos['pha'] = True
            else:
                neos['pha'] = False

            neos_list.append(NearEarthObject(**neos))
    return neos_list

def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path, 'r') as infile:
        cad_data = json.load(infile)['data']

        cad_list = []
        for cad_obj in cad_data:
            cas = {}
            cas['des'] = cad_obj[0]
            cas["cd"] = cad_obj[3]

            if cad_obj[4]:
                cas["dict"] = float(cad_obj[4])
            else:
                cas["dict"] = float('nan')

            if cad_obj[7]:
                cas["v_rev"] = float(cad_obj[7])
            else:
                cas["v_rev"] = float('nan')

            cad_list.append(CloseApproach(**cas))
    return cad_list
