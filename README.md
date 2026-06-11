🚀 ADMBw-Extraktor – Einfache Anleitung
❓ Was macht der ADMBw-Extraktor?
Der ADMBw-Extraktor ist ein KI-Tool, das Fachtexte automatisch in ADMBw-NAFv4-Architekturmodelle umwandelt. Er liest Dokumente, extrahiert relevante Informationen und erstellt daraus standardkonforme Modelle mit Diagrammen – Viewpoint für Viewpoint, mit 7-facher Qualitätsprüfung.

📁 Dateien (5 Stück)
System Prompt.txt – Steuert den gesamten Workflow

ADMBw-Knowledge-Stereotypes.md – Alle 317 Stereotype mit Regeln

ADMBw-Knowledge-Viewpoints.md – Metamodell-Regeln pro Viewpoint

ADMBw-Knowledge-Connectors.md – Konnektor-Regeln und Viewpoint-Liste

Dokumentation-ADMBw.pdf – Offizielle ADMBw-NAFv4-Dokumentation

🔧 Einrichtung in OpenWebUI (3 Minuten)
Schritt 1: System-Prompt laden
Gehen Sie zu Settings → System Prompt und kopieren Sie den Inhalt aus System Prompt.txt hinein. Speichern Sie die Einstellungen.

Schritt 2: Knowledge-Dateien hinterlegen
Gehen Sie zu Knowledge → Upload und laden Sie alle 4 Knowledge-Dateien hoch. Aktivieren Sie die RAG-Semantiksuche.

Schritt 3: Testen
Geben Sie als Start-Prompt ein: Starte den ADMBw-Extraktor Workflow. Analysiere das angehängte Dokument.

🔄 Ablauf (3 Schritte)
Schritt 1 – Vorschlag: Die KI liest Ihr Dokument und schlägt passende Viewpoints vor. Sie bestätigen oder ändern die Vorschläge.

Schritt 2 – Extraktion: Die KI extrahiert Viewpoint für Viewpoint mit 7-fachem Double-Check. Sie prüfen jedes Ergebnis und geben Feedback.

Schritt 3 – Export: Zusammenfassung aller Viewpoints. Optionaler HTML-Gesamtexport verfügbar.

✅ Wichtig zu wissen
Die KI wartet nach jedem Schritt auf Ihr Feedback – sie extrahiert nicht alle Viewpoints auf einmal.

Jeder Viewpoint enthält einen 7-fach Double-Check für Qualitätssicherung.

HTML-Export ist pro Viewpoint oder als Gesamtexport verfügbar.

Mermaid-Diagramme folgen strikten Syntax-Regeln (keine Guillemets, korrektes Escaping).

💡 Nutzung in anderen KI-Systemen
ChatGPT / Claude / Lokale LLMs: Kopieren Sie den System-Prompt in Custom Instructions oder System Message. Fügen Sie die Knowledge-Dateien als Upload hinzu. Verwenden Sie den gleichen Start-Prompt.