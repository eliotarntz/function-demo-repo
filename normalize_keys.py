import sys
import yaml
import re
import json

def to_snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def normalize_keys_recursive(obj):
    if isinstance(obj, dict):
        new_dict = {}
        for key, value in obj.items():
            new_key = to_snake_case(str(key))
            new_dict[new_key] = normalize_keys_recursive(value)
        return new_dict
    elif isinstance(obj, list):
        return [normalize_keys_recursive(item) for item in obj]
    else:
        return obj

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python normalize_keys.py <input_yaml_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as f:
            data = yaml.safe_load(f)

        normalized_data = normalize_keys_recursive(data)

        # Output normalized data as JSON to stdout (easier for next step)
        print(json.dumps(normalized_data, indent=2))

    except Exception as e:
        print(f"Error processing {input_file}: {e}", file=sys.stderr)
        sys.exit(1)