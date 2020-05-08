create_user = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "username": {
            "type": "string"
        },
        "password": {
            "type": "string",
            "minLength": 8
        },
        "email": {
            "type": "string",
            "pattern": "([a-z0-9\._%+!$&*=^|~#%{}\-].*)@([a-z0-9\-]+\.){1,}([a-z]{2,22})",
            "format": "email"
        },
        "birthdate": {
            "type": "string",
            "pattern": "\d\d\d\d-\d\d-\d\d",
            "format": "date"
        },
        "role": {
            "type": "string"
        },
        "immatriculation": {
            "type": "string",
            "maxLength": 7
        }
    },
    "required": [
        "username",
        "password",
        "email",
        "role"
    ]
}

update_user = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "username": {
            "type": "string"
        },
        "password": {
            "type": "string",
            "minLength": 8
        },
        "email": {
            "type": "string",
            "pattern": "([a-z0-9\._%+!$&*=^|~#%{}\-].*)@([a-z0-9\-]+\.){1,}([a-z]{2,22})",
            "format": "email"
        },
        "birthdate": {
            "type": "string",
            "pattern": "\d\d\d\d-\d\d-\d\d",
            "format": "date"
        },
        "role": {
            "type": "string"
        },
        "immatriculation": {
            "type": "string",
            "maxLength": 7
        }
    },
    "required": [
        "username",
        "password",
    ]
}