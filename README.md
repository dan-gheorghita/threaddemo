# threadDemo.py

**Analysis of the Python Code**

The provided Python code is a simple demonstration of multithreading using the `threading` library. Here's a breakdown of what the code does:

### Importing Libraries

```python
import threading, time
```

The code imports the necessary libraries for threading (`threading`) and the time module (`time`).

### Printing Program Messages

```python
print('Start of program.')
```

The code prints a message to indicate the start of the program.

### Defining a Function for Taking a Nap

```python
def takeANap():
    time.sleep(5)
    print('Wake up!')
```

This function simulates a 5-second sleep using the `time.sleep()` function. After waking up, it prints a message to indicate that it has finished sleeping.

### Creating and Starting a New Thread

```python
threadObj = threading.Thread(target=takeANap)
threadObj.start()
```

Here, a new thread object