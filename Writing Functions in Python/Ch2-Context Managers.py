#Chapter 2 - Context Managers


#The number of cats
# Open "alice.txt" and assign the file to "file"
import contextlib
import os
import time

with open('Datasets/alice.txt') as file:
  text = file.read()

n = 0
for word in text.split():
  if word.lower() in ['cat', 'cats']:
    n += 1

print('Lewis Carroll uses the word "cat" {} times'.format(n))
print("=========================================================")


#The speed of cats
# image = get_image_from_instagram()
#
# # Time how long process_with_numpy(image) takes to run
# with timer():
#   print('Numpy version')
#   process_with_numpy(image)
#
# # Time how long process_with_pytorch(image) takes to run
# with timer():
#   print('Pytorch version')
#   process_with_pytorch(image)
print("=========================================================")


#The timer() context manager
# Add a decorator that will make timer() a context manager
@contextlib.contextmanager
def timer():
  """Time the execution of a context block.

  Yields:
    None
  """
  start = time.time()
  # Send control back to the context block
  yield
  end = time.time()
  print('Elapsed: {:.2f}s'.format(end - start))

with timer():
  print('This should take approximately 0.25 seconds')
  time.sleep(0.25)
print("=========================================================")


#A read-only open() context manager
@contextlib.contextmanager
def open_read_only(filename):
  """Open a file in read-only mode.

  Args:
    filename (str): The location of the file to read

  Yields:
    file object
  """
  read_only_file = open(filename, mode='r')
  # Yield read_only_file so it can be assigned to my_file
  yield read_only_file
  # Close read_only_file
  read_only_file.close()

with open_read_only('Datasets/my_file.txt') as my_file:
  print(my_file.read())
print("=========================================================")


#Scraping the NASDAQ
# Use the "stock('NVDA')" context manager
# and assign the result to the variable "nvda"
# with stock('NVDA') as nvda:
#   # Open "NVDA.txt" for writing as f_out
#   with open('NVDA.txt', 'w') as f_out:
#     for _ in range(10):
#       value = nvda.price()
#       print('Logging ${:.2f} for NVDA'.format(value))
#       f_out.write('{:.2f}\n'.format(value))
print("=========================================================")


#Changing the working directory
@contextlib.contextmanager
def in_dir(directory):
  """Change current working directory to `directory`,
  allow the user to run some code, and change back.

  Args:
    directory (str): The path to a directory to work in.
  """
  current_dir = os.getcwd()
  print(current_dir)
  os.chdir(directory)

  # Add code that lets you handle errors
  try:
    yield
  # Ensure the directory is reset,
  # whether there was an error or not
  finally:
    os.chdir(current_dir)

with in_dir('/Users/jackilrajnicant/PycharmProjects/datacamp-python-data-engineer-track/Writing Functions in Python/Datasets'):
    print(os.listdir())
print("=========================================================")