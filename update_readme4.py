import sys
import re

readme_path = 'README.md'
with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'Der \*\*ADMBw-Extraktor\*\* ist ein KI-gestützter Agent.*?eingestuften Daten achten!', re.DOTALL)

new_text = """Der **ADMBw-Extraktor** ist ein KI-gestützter Agent (maßgeschneidert für OpenWebUI), der architekturrelevante Fachtexte (Prosa) automatisch analysiert. Er nutzt einen streng iterativen Prozess mit einem 7-fachen Double-Check, um die extrahierten Informationen regelkonform aufzubereiten.

### ⚠️ Wichtiger Hinweis zur Zielsetzung
Der Extraktor produziert bewusst **keine fertigen, importierbaren Architekturmodelle** (wie z.B. XMI). Das Tool extrahiert die Informationen und stellt sie übersichtlich im Chat oder als HTML-Artefakt dar. Dieser Output dient dem Architekten als **strukturierte Vorlage zum Ablesen und manuellen Nachmodellieren** im eigentlichen Werkzeug (z.B. Sparx Enterprise Architect). Die ID-Vergabe und finale semantische Validierung am ADMBw-Metamodell erfolgen zwingend dort.

> 🔒 **Sicherheitshinweis:** Bitte zwingend auf den korrekten Umgang mit eingestuften Daten achten!"""

if pattern.search(content):
    new_content = pattern.sub(new_text, content)
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success")
else:
    print("Pattern not found!")
