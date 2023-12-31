import sys
def hex_to_ascii(hex_string):

    hex_values = hex_string.split()

    try:

        ascii_text = ''.join([chr(int(hex_value, 16)) for hex_value in hex_values])

        return ascii_text

    except ValueError as e:

        print(f"Error: {e}")

        return ""
def convert_hex_file_to_ascii(input_file, output_file):
    try:

        with open(input_file, 'r') as f:

            hex_data = f.read()

            ascii_text = hex_to_ascii(hex_data)

            with open(output_file, 'w') as out:

                out.write(ascii_text)

            print(f"Conversion completed. ASCII text saved to {output_file}")

    except IOError as e:

        print(f"Error: {e}")

if __name__ == "__main__":

    if len(sys.argv) != 3:

        print("Usage: python script.py input_file output_file")

    else:

        input_file = sys.argv[1]

        output_file = sys.argv[2]

        convert_hex_file_to_ascii(input_file, output_file)

