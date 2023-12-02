import csv

file_path = 'python/day_1/input.csv'
list_input = []

def extract_first_and_last_int(line):
    if isinstance(line, list) and len(line) > 0 and isinstance(line[0], str):
        string_line = line[0]

        first_int = None
        last_int = None

        for char in string_line:
            if char.isdigit():
                if first_int is None:
                    first_int = int(char)
                last_int = int(char)

        if first_int is not None and last_int is not None:
            concatenated_result = int(str(first_int) + str(last_int))
            convert_result = int(concatenated_result)
            return convert_result
        else:
            return None, None

with open(file_path, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        first_and_last_int = extract_first_and_last_int(row)
        list_input.append(first_and_last_int)

print(sum(list_input))