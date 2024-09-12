
import re
import os

class UniqueIntegers:
    @staticmethod
    def processFile(inputFilePath: str, outputFilePath: str):
        unique_integers = set()  # Create a set to store unique integers
        
        with open(inputFilePath, 'r') as infile:
            for line in infile:
                line = line.strip()  # Remove any leading/trailing whitespace
                if line:
                    match = re.fullmatch(r'^-?\d+$', line)  # Match a single integer
                    if match:
                        number = int(match.group())
                        unique_integers.add(number)  # Add integer to the set
        
        sorted_integers = sorted(unique_integers)  # Sort the unique integers
        
        with open(outputFilePath, 'w') as outfile:
            for number in sorted_integers:
                outfile.write(f"{number}\n")  # Write each integer on a new line

# Example usage
if __name__ == "__main__":
    input_directory = 'C:/Users/Administrator/Desktop/Unique integers/unique_integers/dsa/hw01/sample_inputs'
    output_directory = 'C:/Users/Administrator/Desktop/Unique integers/unique_integers/dsa/hw01/sample_results'

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Process each .txt file in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.txt'):  # Process only .txt files
            input_path = os.path.join(input_directory, filename)
            output_filename = f"{filename}_results.txt"
            output_path = os.path.join(output_directory, output_filename)
            UniqueIntegers.processFile(input_path, output_path)  # Process the file
