ossi_tool3
-------------------------

It is a Python (3.x) script to emulate Avaya SAT (Communication Manager Site Administration Tool)
to execute multiple commands, and write output data into the CSV file for later processing.
It should be ideal tool to repeat a command multiple times which not available as import in
Avaya Site Administration Tool (eg. list usage).

As input arguments need to define the followings:
    - host
    - Username
    - Password
    - Input file
    - Output file

For all available option use "ossi_tool3 -h" 

---------------
Usage examples:
---------------

#ossi_tool3 192.168.10.10 sampleuser -ppassword -i commands.csv -o outputfile.csv
#ossi_tool3 192.168.10.10 sampleuser -ppassword -c "list vdn" -o outputfile.csv
#ossi_tool3 192.168.10.10 sampleuser -ppassword -c "list usage vdn xxxx" -o outputfile.csv

---------------------
Installation (Linux):
---------------------

You can easily install ossi_tool3 with pip. It takes care about the prerequisits.
Usage
#pip3 install ossi_tool3

-----------------------
Installation (Windows):
-----------------------

Due to different ssh approch on Windows the pexpect and the ossi_tool3 is not available. For Windows use WSL
(Windows Subsystem for Linux ).
Please read about WSL here: https://docs.microsoft.com/en-us/windows/wsl/

If you have working linux subsystem, you can follow the Linux description.


-------------
Known issues:
-------------

- If the RSA key of the host where want to connect not in the .ssh/known_hosts file, than it drops an exception.
    Workaround:
    ssh to the host with regular ssh and accept the RSA key.
- Some of the 'list measurement' commands does not provide general output, so it will drop error
