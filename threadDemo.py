import threading, time # Import the necessary libraries for threading and time module

print('Start of program.') # Print the start of the program message

def takeANap(): # Define a function for taking a nap
    time.sleep(5) # Simulate a 5-second sleep
    print('Wake up!') # Print a message after waking up

threadObj = threading.Thread(target=takeANap) # Create a new thread object with the target function
threadObj.start() # Start the new thread

print('End of program.') # Print the end of the program message