# Port-scanner
This is a small script i developed in order to learn more about ports and port scanning just for fun. The script allows you to scan the port/ports from a target IP with your own IP.
For example, you can run the code by writing in the command line: <br><br>
    ```python3 port-scan.py 127.0.0.1 --single 80``` <br><br>
Or: <br><br>
    ```python3 port-scan.py scanme.nmap.org --multiple 80 443 22 62430```

# Command line:

python3 port-scanner.py [Your running IP] [Target IP] [--single or --multiple] [port(s)]

# Important disclaimer

**I am not responsible for the usage of this script. Do not run the script on a network that is not yours**, you are allowed to run the script on <a href="http://scanme.nmap.org/">scanme.nmap.org<a> or on a local IP.
