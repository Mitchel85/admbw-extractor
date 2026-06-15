import sys

readme_path = 'README.md'
with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

warning_text = """

### ⚠️ Wichtiger Hinweis zur Zielsetzung
Der **ADMBw-Extraktor** produziert bewusst **keine fertigen, importierbaren Architekturmodelle** (wie z.B. XMI). 

Er dient ausschließlich der **Vorbereitung der Modellierung**: Das Tool extrahiert architekturrelevante Informationen aus Prosa und stellt sie übersichtlich im Chat oder als HTML-Artefakt dar. Dieser Output dient dem Architekten als **strukturierte Vorlage zum Ablesen und manuellen Nachmodellieren** im eigentlichen Werkzeug (z.B. Sparx Enterprise Architect). Die ID-Vergabe und finale semantische Validierung erfolgen zwingend dort.
"""

target = "Regelkonformität zu garantieren.\n\n---"
replacement = "Regelkonformität zu garantieren.\n" + warning_text + "\n---"

if target in content:
    new_content = content.replace(target, replacement)
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success")
else:
    print("Target string not found!")
