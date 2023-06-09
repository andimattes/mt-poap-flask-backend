import json
from modules.schemaValidator import validate


def loadConfig():
    with open("config.json") as json_data_file:
        data = json.load(json_data_file)
        validate(data)
        return data


def storeConfig(config):
    validate(config)
    with open("config.json", "w") as outfile:
        json.dump(config, outfile, indent=4)


def getHeader(withBearer=True):
    config = loadConfig()
    header = {"X-API-Key": config["auth"]["api_key"], "Content-Type": "application/json"}

    if withBearer:
        header["Authorization"] = f"Bearer {config['auth']['access_token']}"
    return header


if __name__ == "__main__":
    config = loadConfig()
    config["test"] = "test"
    storeConfig(config)
    config = loadConfig()
