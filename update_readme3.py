import sys

readme_path = 'README.md'
with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = "und in standardkonforme **ADMBw-NAFv4-Architekturmodelle** übersetzt."
replacement = "und als **strukturierte Vorlage für die ADMBw-NAFv4-Modellierung** aufbereitet."

if target in content:
    new_content = content.replace(target, replacement)
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success")
else:
    print("Target string not found!")
