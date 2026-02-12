from generate_key import generate_key
from deserialize import deserialize

def guarded_deserialize(expected_key, data):

    # TODO: generate new key from data
    new_key = generate_key(data)

    # TODO: if keys match → return deserialize(data)
    if new_key == expected_key:
        return deserialize(data)
    # TODO: if keys do NOT match → return False
    else:
        return False