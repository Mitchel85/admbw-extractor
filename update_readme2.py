import sys

readme_path = 'README.md'
with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

security_text = "\n> 🔒 **Sicherheitshinweis:** Bitte zwingend auf den korrekten Umgang mit eingestuften Daten achten!\n\n---"
target = "zwingend dort.\n\n---"

if target in content:
    new_content = content.replace(target, "zwingend dort.\n" + security_text)
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success")
else:
    print("Target string not found! Content tail:")
    print(content[:500])
