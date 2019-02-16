#This program takes the URL inputed by the user and returns the Domain Name, IP Address, and any Open Ports

from tld import get_tld
import os

"""
This method uses the URL given and returns the Domain Name
"""
def get_domain_name(url):
    domain_name = get_tld(url)
    return domain_name


"""
This method uses the URL given and returns the first IP Address found
"""
def get_ip_address(url):
    commmand = "host " + url
    data = os.popen(command)
    results = str(data.read())
    temp = results.find("has address") + 12
    ip_address = results[temp:].splitlines()[0]
    return ip_address


"""
This method uses the IP Addresses of the given URL and returns the Open Ports
"""
def port_scan(ip):
    command = "nmap " + ip
    scan = os.popen(command)
    ports = str(scan.read())
    return ports


"""
This main method will print the information created by the methods
"""
def main():
    user_input = input("Enter a url: ")
    domain = get_domain_name(user_input)
    ip = get_ip_address(user_input)
    ports = port_scan(get_ip_address(user_input))

    print("URL: " + website + " \n" +
          "Domain Name: " + domain + " \n" +
          "IP Address: " + ip + " \n" +
          "Open Ports: " + ports + " \n")

#Calls the main method and runs the program
main()
