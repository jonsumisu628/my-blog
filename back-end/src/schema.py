create_user_schema = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The User Create Schema",
  "default": None,
  "required": [
    "name",
    "email",
    "display_name",
    "password"
  ],
  "properties": {
    "name": {
      "$id": "#/properties/name",
      "type": "string",
      "title": "The Name Schema",
      "default": "",
      "examples": [
        "John Smith"
      ],
      "pattern": "^(.*)$"
    },
    "email": {
      "$id": "#/properties/email",
      "type": "string",
      "title": "The Email Schema",
      "default": "",
      "examples": [
        "john@rabbit-null.com"
      ],
      "pattern": "^[^@]+@[^@]+\.[^@]+$",
      "format": "email"
    },
    "display_name": {
      "$id": "#/properties/display_name",
      "type": "string",
      "title": "The Display_name Schema",
      "default": "",
      "examples": [
        "john"
      ],
      "pattern": "^(.*)$"
    },
    "avatar_url": {
      "$id": "#/properties/avatar_url",
      "type": "string",
      "title": "The Avatar_url Schema",
      "description": "",
      "default": "",
      "examples": [
        "https://storage.rabbit-null.com/users/john-smith/avatar.png"
      ],
      "minLength": 11,
      "maxLength": 255,
      "pattern": "^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+$",
      "format": "uri"
    },
    "password": {
      "$id": "#/properties/password",
      "type": "string",
      "title": "The Password Schema",
      "description": "Character string of 8 to 100 characters including one or more half-width alphabetic characters and half-width numerals",
      "default": "",
      "examples": [
        "sample-p@ssw0d"
      ],
      "pattern": "^(.*)$"
    }
  }
}
