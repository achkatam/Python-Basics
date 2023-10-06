from print_data import send_info
import os

result = send_info()

os.remove('data.json')

print(result)
