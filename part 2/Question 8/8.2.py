from generate_key import generate_key
from deserialize import deserialize

def validate_and_load(expected_key, data):

    # TODO: generate new key from data
    new_key = generate_key(data)

    # TODO: if expected_key matches new_key,
    if expected_key == new_key:
        return deserialize(data)

    # TODO: otherwise raise:
    # Exception("Invalid integrity check")
    else:
        raise Exception("Invalid integrity check")
