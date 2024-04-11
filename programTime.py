import time
import os

# Get the start time
start_time = time.time()

# Run the program we want to time
for i in range(1, 101):
    print(f"[{i} / 100]")
    os.system("cls")

# Get the time after the program has ran
end_time = time.time()

# print out how long it took to run the program
print("It took", end_time - start_time, "seconds to run the program")
# end time - the start time = time taken to run the program