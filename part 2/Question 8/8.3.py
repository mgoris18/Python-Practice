from generate_key import generate_key
from deserialize import deserialize

def secure_load(old_key, payload):

    # TODO: generate a new key from payload
    new_key = generate_key(payload)

    # TODO: if keys do NOT match, raise:
    # Exception("Integrity validation failed")
    if new_key != old_key:
        raise Exception("Integrity validation failed")

    # TODO: if validation passes, return deserialize(payload)
    else:
        return deserialize(payload)
