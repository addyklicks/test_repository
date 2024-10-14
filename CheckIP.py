# import ipaddress

# def is_internal_ip(ip):
#     try:
#         ip_obj = ipaddress.ip_address(ip)
#         # Check if it's private
#         if ip_obj.is_private:
#             return f"{ip} is internal (private)"
#         else:
#             return f"{ip} is external (public)"
#     except ValueError:
#         return f"{ip} is not a valid IP address"

# # Example IPs
# ips = ["192.168.54.1", "172.26.171.14", "8.8.8.8", "123.45.67.89"]

# for ip in ips:
#     print(is_internal_ip(ip))


import ipaddress

def is_internal_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        # Check if it's private
        if ip_obj.is_private:
            return f"{ip} is internal (private)"
        else:
            return f"{ip} is external (public)"
    except ValueError:
        return f"{ip} is not a valid IP address"

# Ask the user for an IP address
ip = input("Please enter an IP address: ")
print(is_internal_ip(ip))


