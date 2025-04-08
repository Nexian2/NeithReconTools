from modules.owasp_scanner import scan_owasp_top_10
from modules.malware_scanner import scan_url_malware
from modules.vuln_scanner import scan_basic_vulns
from utils.report_writer import save_pdf_report
from ai.ai_suggestion import ai_suggestion  # Benerin importnya

def show_ascii_art():
    ascii = """
 _   _      _   _     _       _                      
| \\ | | ___| |_| |__ (_)_ __ | |__   __ _ _ __  _ __ 
|  \\| |/ _ \\ __| '_ \\| | '_ \\| '_ \\ / _` | '_ \\| '__|
| |\\  |  __/ |_| | | | | | | | | | | (_| | |_) | |   
|_| \\_|\\___|\\__|_| |_|_|_| |_|_| |_|\\__,_| .__/|_|   
                                          |_|        
"""
    print(ascii)

def main():
    show_ascii_art()
    target = input("[?] Enter Target URL/IP: ")

    print("[+] Scanning for OWASP Top 10...")
    owasp_results = scan_owasp_top_10(target)

    print("[+] Scanning for malware...")
    malware_results = scan_url_malware(target)

    print("[+] Scanning for basic vulnerabilities...")
    vuln_results = scan_basic_vulns(target)

    all_results = {
        "OWASP Top 10": owasp_results,
        "Malware": malware_results,
        "Common Vulns": vuln_results,
    }

    # AI Suggestion Result
    print("[+] Menganalisis hasil dengan AI Suggestion...")
    combined_vulns = owasp_results + malware_results + vuln_results
    ai_results = ai_suggestion(combined_vulns)

    print("\n[AI Suggestion Result]")
    for suggestion in ai_results:
        print("- " + suggestion)

    save_pdf_report(target, all_results)
    print(f"[+] Scan completed. Report saved to scan_report.pdf")

if __name__ == "__main__":
    main()