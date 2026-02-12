from generate_key import generate_key
from deserialize import deserialize
from serialize import serialize

def safe_deserialize(key, serialized_data):

    new_key = generate_key(serialized_data)  # TODO: replace with a newly generated key from serialized_data
    
    if key == new_key:
        # TODO: return the result of deserialize(serialized_data)
        return deserialize(serialized_data)
        pass
    else:
        # TODO: raise Exception with message: 'New key does not match old key'
        raise Exception("New key does not match old key")
        pass

# Example usage
grades = {'Alice': 89, 'Bob': 72, 'Charles': 87}
serialized_data = serialize(grades)
deserialized_data = safe_deserialize(generate_key(serialized_data), serialized_data)
