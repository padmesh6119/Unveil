import requests
import whois
import dns.resolver
import ssl
import socket
import pyfiglet
import time

# Utility function for stylish output using figlet
def display_banner():
    ascii_banner = pyfiglet.figlet_format("Unveil")
    print(ascii_banner)
    # Adding your name and credits in a smaller font style
    print("\nDeveloped by: Padmesh")
    print("Credits: Unveil uses whois, requests, dnspython, and pyfiglet libraries.")

# Function to check SSL certificate
def check_ssl(url):
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname=url) as s:
            s.connect((url, 443))
        return True
    except Exception as e:
        return False

# Function to get Whois information
def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        return None

# Function to check DNS records
def check_dns(domain):
    try:
        dns.resolver.resolve(domain, 'A')
        return True
    except dns.resolver.NoAnswer:
        return False
    except Exception as e:
        return False

# Function to check if domain is blacklisted using an API (placeholder for real check)
def check_blacklist(domain):
    # Here you can use API calls to check blacklists like VirusTotal or others
    # Placeholder for blacklist check, assume domain is not blacklisted for demo purposes
    return False

# Function to check if domain is suspicious based on age
def check_domain_age(domain):
    w = get_whois_info(domain)
    if w:
        creation_date = w.creation_date
        if creation_date and isinstance(creation_date, list):
            age = (time.time() - time.mktime(creation_date[0].timetuple())) / (60 * 60 * 24 * 365)
            if age < 1:  # Domains less than 1 year old may be suspicious
                return True
    return False

# Main function to process the URL
def analyze_website(url):
    print(f"Analyzing: {url}")
    
    domain = url.split("//")[-1].split("/")[0]  # Extract domain part
    
    # Initialize list to collect reasons if any issues arise
    reasons = []
    valid = True
    
    # 1. Check SSL certificate
    ssl_valid = check_ssl(domain)
    if not ssl_valid:
        reasons.append("Invalid SSL Certificate")
        valid = False
    
    # 2. Check DNS resolution
    dns_resolved = check_dns(domain)
    if not dns_resolved:
        reasons.append("DNS Resolution Failed")
        valid = False
    
    # 3. Check Whois for domain age
    domain_age_suspicious = check_domain_age(domain)
    if domain_age_suspicious:
        reasons.append("Domain Age Suspect (less than 1 year)")
        valid = False
    
    # 4. Check if it's blacklisted
    blacklisted = check_blacklist(domain)
    if blacklisted:
        reasons.append("Domain is Blacklisted")
        valid = False
    
    # Summary of results
    if valid:
        print("\nWebsite is VALID!")
    else:
        print("\nWebsite is INVALID!")
        print("Reasons:")
        for reason in reasons:
            print(f"- {reason}")

# Main function to start the tool
def main():
    display_banner()
    
    # User input for the website URL
    url = input("Enter website URL (e.g., https://example.com): ")
    
    # Analyze the website
    analyze_website(url)

# Run the main function
if __name__ == "__main__":
    main()
