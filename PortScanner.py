#This program takes the URL inputed by the user and returns the Domain Name, IP Address, and any Open Ports

from tld import get_tld, get_fld
import socket
import sys

"""
This method uses the URL given and returns the Top Domain Name
"""
def get_domain_name(url):
    domain_name = get_tld(url, as_object=True)
    return domain_name.fld

"""
This method uses the URL given and returns the first IP Address found
"""
def get_ip_address(host):
    ip_address = socket.gethostbyname(host)
    return ip_address

"""
This method uses the IP Addresses of the given URL and returns the Open Ports
"""
def port_scan(ip):
    try:
        for port in range(1,6000):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("Port {}: 	 Open".format(port))
            sock.close()

    except socket.gaierror:
        print("Host could not be identified." + "\n" + "Ending program..." + "\n")

    except KeyboardInterrupt:
        print("You canceled the scan" + "\n")
        sys.exit()

    except socket.error:
        print("Couldn't connect to the host." + "\n")
        sys.exit()

"""
This main method will print the information created by the methods
"""
def main():
    user_input = input("Enter a url: ")

    domain = get_domain_name(user_input)
    ip = get_ip_address(domain)
    ports = port_scan(get_ip_address(ip))

    print("URL: " + website + " \n" +
          "Domain Name: " + domain + " \n" +
          "IP Address: " + ip + " \n" +
          "Scanning Ports: ... " + ports + " \n")

#Calls the main method and runs the program
main()
