import subprocess

# IN CASE YOU NEED TO CHANGE THE PERMISSIONS OF A FILE

xml_file_path = 'your_file_path_here'

# Close the file if it's open in another application

# Change the file permissions using the icacls command and change the username to your username
subprocess.run(['icacls', xml_file_path, '/grant', 'username:F'])