# 🎯 ADMBw Extraktions-Assistent v 1.0

Ein KI-gestützter Prompt-Assistent zur Unterstützung von ADMBw-zertifizierten Architektur-Modellierern bei der Extraktion von Stereotypen und Beziehungen aus natürlichsprachlichen Dokumenten.

## ⚠️ Wichtiger Hinweis

**Dieses Tool erzeugt keine fertigen oder importierbaren Dateien.**  
Es unterstützt Modellierer dabei, ADMBw-konforme Modelle **manuell nachzuvollziehen und zu erstellen**. Alle Extraktionsergebnisse dienen als **Entscheidungshilfe und Dokumentation** – die eigentliche Modellierung erfolgt in Ihrem Modellierungswerkzeug (z. B. Enterprise Architect).

---

## 🎯 Zielsetzung

- ✅ **Unterstützung bei der Modellierung** – Strukturierte Extraktion aus Prosa-Dokumenten
- ✅ **ADMBw-Konformität sicherstellen** – Validierung gegen offizielle Knowledge-Bases [v2025.10]
- ✅ **Iterativer Workflow** – Schrittweise Validierung mit dem Nutzer
- ✅ **Transparente Entscheidungen** – Nachvollziehbare Stereotyp- und Connector-Zuordnungen
- ✅ **Zentraler Export** – Konsolidiertes HTML-Artefakt zur Dokumentation aller Ergebnisse

---

## 📋 Workflow-Übersicht

| Phase | Beschreibung |
|-------|--------------|
| **1. Concern-Ermittlung** | Erkenntnisinteresse des Modellierers erfassen |
| **2. Viewpoint-Vorschlag** | Passende ADMBw-Viewpoints identifizieren & validieren |
| **3. Stereotyp-Extraktion** | Begriffe aus Prosa ADMBw-Stereotypen zuordnen [9] |
| **4. Beziehungs-Extraktion** | Source→Connector→Target nach Topology-Regeln [10] |
| **5. Mermaid-Visualisierung** | KI-wählt passenden Diagrammtyp pro Viewpoint |
| **6. Export** | Konsolidiertes HTML-Artefakt mit allen Ergebnissen |

---

## 📚 Erforderliche Wissensquellen

Der Assistent konsultiert bei jeder Extraktion folgende Knowledge-Bases:

| Datei | Inhalt |
|-------|--------|
| `ADMBw-Knowledge-Viewpoints.md` [11] | Erlaubte Meta-Model-Elemente pro Viewpoint (53 Viewpoints) |
| `ADMBw-Knowledge-Topology.md` [10] | Gerichtete Kanten (Source→Connector→Target) |
| `ADMBw-Knowledge-Stereotypes.md` [9] | Alle 317 ADMBw-Stereotype mit AppliesTo & TaggedValues |
| `ADMBw-Knowledge-Connectors.md` [8] | EA-Metatypen + erlaubte Stereotype + Viewpoint-Übersicht |

---

## 🛡️ Qualitätssicherung

- **Abstrakte Stereotype** werden markiert (🔒) – nur konkrete Subtypen verwenden
- **Viewpoint-Konformität** – Elemente nur in erlaubten Viewpoints
- **Topology-Validierung** – Jede Beziehung folgt Source→Connector→Target-Regeln
- **Connector-Metatyp** – Stereotyp muss zum EA-Metatyp passen

---

## 🚀 Verwendung

1. Prompt in Ihre KI-Umgebung laden
2. Mit **Phase 1** starten und Concern formulieren
3. Iterativ durch alle Phasen arbeiten
4. Am Ende **konsolidiertes HTML-Artefakt** exportieren

---

## 📄 Lizenz & Haftung

Dieser Prompt dient als **Unterstützungswerkzeug** für ADMBw-zertifizierte Modellierer. Die Verantwortung für die Korrektheit der erstellten Modelle liegt beim Nutzer.

---

*ADMBw v2025.10 | Keine importierbaren Artefakte | Manuelle Nachmodellierung erforderlich*

Dieser Text wurde von dem IT-System QAKI generiert. Es handelt sich hierbei um ein experimentelles System. 
