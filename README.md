Unveil - Website Security Analyzer

Unveil is a Python-based tool that analyzes websites for potential security issues. It checks the SSL certificate, DNS resolution, domain age, and whether the domain is blacklisted. The tool aims to help identify websites that may have vulnerabilities or be untrustworthy.

Features

- SSL Certificate Check**: Verifies if the website has a valid SSL certificate.
- DNS Resolution**: Checks if the website domain resolves properly in DNS.
- Domain Age**: Analyzes if the domain is less than 1 year old (which could indicate a suspicious domain).
- Blacklist Check**: Placeholder function to check if the domain is blacklisted.
  
Requirements

To run this tool, you'll need the following Python libraries:

- requests
- whois
- dns.resolver (part of the dnspython package)
- ssl
- socket
- pyfiglet

You can install them using pip:

pip install requests python-whois dnspython pyfiglet
