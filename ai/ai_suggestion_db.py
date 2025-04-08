suggestion_database = {
"sql injection": "Use prepared statements (parameterized queries) or an ORM like SQLAlchemy.",
"xss": "Escape all HTML output and use Content Security Policy (CSP).",
"insecure deserialization": "Use a secure format like JSON, don't eval() external data.",
"broken authentication": "Implement rate limiting and multi-factor authentication.",
"security misconfiguration": "Make sure the server is up to date, delete backup/test files, and check permissions.",
"sensitive data exposure": "Use HTTPS and encrypt sensitive data during storage and transfer.",
"xml external entities": "Disable external parsing in the XML parser.",
"broken access control": "Use role-based access control and validate access on the server side.",
"using components with known vulnerabilities": "Update all libraries and perform regular CVE checks.",
"insufficient logging & monitoring": "Enable logging for all important activities and real-time alerts.",
"directory listing": "Disable directory indexing on the webserver.",
"open port": "Close unused ports and use a firewall.",
}