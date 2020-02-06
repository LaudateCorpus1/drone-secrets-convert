#!/usr/bin/env python3

import sys
import textwrap

import oyaml as yaml
from collections import OrderedDict

class DroneSecretsConvert:
    def __init__(self, drone_file=None):
        """
        Class for converting old Drone 1.0rc6 secrets format to the latest standard

        :keyword drone_file: path to file (Mandatory)
        """
        if drone_file is None:
            raise Exception("Keyword drone_file required")

        yaml.warnings({'YAMLLoadWarning': False})

        try:
            f = open(drone_file).read()
            self.yaml_data = list((yaml.load_all(f)))
        except:
            raise Exception("Unable to read YAML from file")
    

    def _get_secrets(self):
        """
        Returns the secrets 

        :return: dict
        :rtype: dict
        """

        for i in self.yaml_data:
            if i['kind'] == "secret":
                return i


    def get_pipelines(self):
        """
        Returns everything but secrets
        
        :return: string
        :rtype: string
        """
        pipeline_step = ""

        for i in self.yaml_data:
            if i['kind'] != "secret":
                step = OrderedDict(i)
                pipeline_step = pipeline_step + "---\n"
                pipeline_step = pipeline_step + yaml.dump(step)

        return pipeline_step


    def convert_secrets(self):
        """
        Converts the secrets to the new Drone format
        
        :return: string
        :rtype: string
        """
        secrets = self._get_secrets()
        converted = ""

        for i in secrets['external_data']:
            secret = """
                ---
                kind: secret
                name: %s
                get:
                  path: %s\n""" % (i, secrets['external_data'][i]['path'])
            converted = converted + textwrap.dedent(secret)

        return converted


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="path to file")
    parser.add_argument("-c", "--complete", help="Return the complete YAML, not just the secrets", action="store_true")
    args = parser.parse_args()

    x = DroneSecretsConvert(drone_file=args.file)

    if args.complete:
        print(x.get_pipelines())

    print(x.convert_secrets())
