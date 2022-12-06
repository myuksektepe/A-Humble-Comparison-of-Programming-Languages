import json
import time


def toBinary(a):
    l, m = [], []
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m


# JSON file read
json_start_time = time.time()
f = open('countries.json')
data = json.load(f)
f.close()
json_end_time = time.time()
json_elapsed_time = json_end_time - json_start_time
print(f"Execution time to JSON file reading: {json_elapsed_time} seconds")

# Find items startswith 'D'
for_loop_start_time = time.time()
dataForD = []
for country in data:
    if str(country).startswith('D'):
        dataForD.append(country)
    for city in data[country]:
        if str(city).startswith('D'):
            dataForD.append(city)
for_loop_end_time = time.time()
for_loop_elapsed_time = for_loop_end_time - for_loop_start_time
print(f"Execution time to For loop: {for_loop_elapsed_time} seconds")

# Find and sum the length of each item
total_length_start_time = time.time()
total_length = 0
for item in dataForD:
    total_length += len(item)
total_length_end_time = time.time()
total_length_elapsed_time = total_length_end_time - total_length_start_time
print(f"Execution time to Find total length: {total_length_elapsed_time} seconds")

# Create long string
long_string_start_time = time.time()
long_string = ""
for item in dataForD:
    long_string += str(item)
long_string = long_string.replace(" ", "")
long_string_end_time = time.time()
long_string_elapsed_time = long_string_end_time - long_string_start_time
print(f"Execution time to Create the long string: {long_string_elapsed_time} seconds")

# Convert long string to binary
to_binary_start_time = time.time()
binary = toBinary(long_string)
to_binary_end_time = time.time()
to_binary_elapsed_time = to_binary_end_time - to_binary_start_time
print(f"Execution time to Convert to binary: {to_binary_elapsed_time} seconds")
print("-------------")

total_execution_time = json_elapsed_time + for_loop_elapsed_time + total_length_elapsed_time + long_string_elapsed_time + to_binary_elapsed_time
print(f"Execution total time: {total_execution_time} seconds")
