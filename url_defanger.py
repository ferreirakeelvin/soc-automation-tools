#!/usr/bin/env python3

import urllib.parse
import sys

def defang_url(url):
    defanged = url.replace("http", "hxxp")
    defanged = defanged.replace(".", "[.]")
    return defanged

def extract_domain(url):
    if not url.startswith(("http://", "https://")):
        url = "http://" + url
        
    parsed_url = urllib.parse.urlparse(url)
    return parsed_url.netloc

def main():
    print("=== SOC Tool: URL Defanger & IoC Extractor ===")
    
    if len(sys.argv) > 1:
        suspect_url = sys.argv[1]
    else:
        suspect_url = input("Cole a URL suspeita para análise: ")

    domain = extract_domain(suspect_url)
    safe_url = defang_url(suspect_url)

    print("\n[+] Resultados da Triagem:")
    print(f"URL Original     : {suspect_url}")
    print(f"Domínio Alvo     : {domain}")
    print(f"URL Segura (Defanged): {safe_url}")

if __name__ == "__main__":
    main()
