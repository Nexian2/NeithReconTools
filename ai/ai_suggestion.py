from ai.ai_suggestion_db import suggestion_database

def ai_suggestion(vuln_list):
    suggestions = []
    found = False

    for vuln in vuln_list:
        # Ambil teks dari dict atau string biasa
        if isinstance(vuln, dict):
            vuln_text = vuln.get("name", "") + " " + vuln.get("type", "")
        else:
            vuln_text = str(vuln)

        vuln_lower = vuln_text.lower()
        matched = False

        for keyword in suggestion_database:
            if keyword in vuln_lower:
                suggestions.append(f"[!] {keyword.upper()} DETECTED: {suggestion_database[keyword]}")
                matched = True
                found = True
                break

        if not matched:
            suggestions.append(f"[?] Tidak diketahui jenis kerentanan: \"{vuln_text}\"")

    if not found:
        suggestions.append("[✓] Tidak ditemukan kerentanan yang cocok dengan database AI.")
        suggestions.append("[i] Kemungkinan target sudah aman dari OWASP Top 10 umum.")

    return suggestions