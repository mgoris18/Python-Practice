from generate_key import generate_key
from deserialize import deserialize

def final_safe_load(key, serialized):

    # TODO: generate new key from serialized
    new_key = generate_key(serialized)

    # TODO: if mismatch → raise Exception("Tampering detected")
    if new_key == key:
        return deserialize(serialized)
    else:
        raise Exception("Tampering detected")

    # TODO: return deserialized object
