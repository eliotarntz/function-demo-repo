import sys
import json

def get_value_by_path(data, path):
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None # Path not found
    return current

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_config.py <normalized_json_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    all_valid = True

    try:
        with open(input_file, 'r') as f:
            normalized_config = json.load(f)

        # Get the list of required fields from the config itself
        required_fields = get_value_by_path(normalized_config, 'validation_required_fields')

        if not required_fields or not isinstance(required_fields, list):
            print("Error: 'validation_required_fields' key not found or not a list in config.", file=sys.stderr)
            sys.exit(1)

        print("--- Running Partial Schema Validation ---")
        for field_path in required_fields:
            value = get_value_by_path(normalized_config, field_path)
            if value is None or value == '':
                print(f"Validation FAILED: Required field '{field_path}' is missing or empty.")
                all_valid = False
            else:
                print(f"Validation PASSED: Required field '{field_path}' is present.")
        print("---------------------------------------")

    except Exception as e:
        print(f"Error during validation: {e}", file=sys.stderr)
        sys.exit(1) # Exit with error on script failure

    if not all_valid:
        print("Validation failed. Aborting build.")
        sys.exit(1) # Exit with error if validation checks fail
    else:
        print("All required fields validated successfully.")
        sys.exit(0) # Exit successfully