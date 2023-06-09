import jsonschema
import sys

# Define the JSON schema to validate against
schema = {
    "type": "object",
    "properties": {
        "auth": {
            "type": "object",
            "properties": {
                "api_key": {"type": "string"},
                "access_token": {"type": "string"},
                "last_refresh": {"type": "string"},
                "client_id": {"type": "string"},
                "client_secret": {"type": "string"},
                "audience": {"type": "string"},
                "grant_type": {"type": "string"},
            },
            "required": [
                "api_key",
                "access_token",
                "last_refresh",
                "client_id",
                "client_secret",
                "audience",
                "grant_type",
            ],
            "additionalProperties": False,
        },
        "event_id": {"type": "string"},
        "secret_code": {"type": "string"},
    },
    "required": ["auth", "event_id", "secret_code"],
    "additionalProperties": False,
}


# Validate the JSON data against the schema
def validate(data):
    try:
        jsonschema.validate(data, schema)
    except jsonschema.exceptions.ValidationError as err:
        sys.exit("[ERR] in schema validation: " + err.message)
