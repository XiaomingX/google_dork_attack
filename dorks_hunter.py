#!/usr/bin/env python3
import random
import time
import tldextract
import argparse
from googlesearch import search
from fake_useragent import UserAgent

def parse_args():
    """
    Parse command-line arguments.
    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Simple Google dork search")
    parser.add_argument('--domain', '-d', required=True, help='Domain to scan')
    parser.add_argument('--results', '-r', type=int, default=10, help='Number of results per search, default 10')
    parser.add_argument('--output', '-o', help='Output file to save results')
    return parser.parse_args()

def save_to_file(file_path, data):
    """
    Save data to a file.
    Args:
        file_path (str): Path to the file.
        data (str): Data to save.
    """
    with open(file_path, "a") as f:
        f.write(data + "\n")

def create_dorks(domain, target):
    """
    Generate a dictionary of Google dork queries.
    Args:
        domain (str): Full domain name.
        target (str): Extracted domain (e.g., "example" from "example.com").
    Returns:
        dict: Description and corresponding dork queries.
    """
    return {
        "# .git folders": f"inurl:\"/.git\" {domain} -github",
        "# Backup files": f"site:{domain} ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup",
        "# Exposed documents": f"site:{domain} ext:doc | ext:pdf | ext:csv",
        "# Confidential documents": f"inurl:{target} confidential | \"employee only\" | proprietary filetype:pdf",
        "# Config files": f"site:{domain} ext:xml | ext:conf | ext:ini",
        "# Subdomains": f"site:*.{domain}",
        "# PHP errors": f"site:{domain} \"PHP Parse error\" | \"PHP Warning\"",
        "# Login pages": f"site:{domain} inurl:login | inurl:admin",
        "# Open redirects": f"site:{domain} inurl:redirect | inurl:src=http",
        "# Cloud buckets": f"site:.s3.amazonaws.com \"{target}\"",
        "# LinkedIn employees": f"site:linkedin.com employees {domain}",
    }

def perform_dork_search(dorks, domain, user_agent, max_results, output_file=None):
    """
    Perform Google dork searches and display/save results.
    Args:
        dorks (dict): Dork descriptions and queries.
        domain (str): Target domain.
        user_agent (UserAgent): Random user agent generator.
        max_results (int): Maximum number of results per dork.
        output_file (str): File path to save results (optional).
    """
    for description, query in dorks.items():
        print(f"\n{description}\n")
        if output_file:
            save_to_file(output_file, description)

        try:
            for i, result in enumerate(search(query, lang="en", user_agent=user_agent.random), start=1):
                print(result)
                if output_file:
                    save_to_file(output_file, result)

                time.sleep(random.uniform(1, 5))  # Random delay between requests

                if i >= max_results:
                    break
        except Exception as e:
            print(f"Error during search: {e}")

def main():
    """
    Main function to coordinate Google dork searches.
    """
    # Parse arguments
    args = parse_args()

    # Extract domain information
    extracted = tldextract.extract(args.domain)
    target = extracted.domain

    # Initialize UserAgent and generate dorks
    user_agent = UserAgent()
    dorks = create_dorks(args.domain, target)

    # Perform searches
    perform_dork_search(dorks, args.domain, user_agent, args.results, args.output)

if __name__ == '__main__':
    main()
