#!/usr/bin/python3
'''Log Parsing'''
from sys import stdin


# Create dictionary to store the number of lines for each status code
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}

# Initialize the total file size to zero
file_size = 0


def print_stats():
    '''Prints the current stats'''
    print("File size: {}".format(file_size))
    for key, val in sorted(status_codes.items()):
        if val > 0:
            print("{}: {}".format(key, val))


# def signal_handler(sig, frame):
#    '''Handles signal to print stats when script is interrupted'''
#    print_stats()
#    sys.exit(0)

# Register the signal handler for the SIGINT signal (CTRL+C)
# signal.signal(signal.SIGINT, signal_handler)


# Read lines from standard input and parse them
if __name__ == "__main__":
    try:
        for n, line in enumerate(stdin, 1):
            try:
                element = line.split()
#        ip, _, _, _, _, _, _ = parts[:7]
#        code = int(parts[8])
                file_size += int(element[-1])
#        total_size += size
                if element[-2] in status_codes.keys():
                    status_codes[element[-2]] += 1
#        line_count += 1
#        if line_count == 10:
#            print_stats()
            except (IndexError, ValueError):
                # If the line is not in the specified format, skip it
                pass
            if not n % 10:
                print_stats()
    except KeyboardInterrupt:
        print_stats()
        raise
    # Print the final statistics when there is no more input
    print_stats()
