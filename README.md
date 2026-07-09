# ADMBw-Extraktor v6.0

![Status](https://img.shields.io/badge/Status-Active-success)
![Standard](https://img.shields.io/badge/Standard-ADMBw%20v2025.10-blue)
![Framework](https://img.shields.io/badge/Framework-NAFv4-orange)
![Plattform](https://img.shields.io/badge/Platform-OpenWebUI-purple)

KI-gestützter Assistent zur Extraktion von Stereotypen, Beziehungen und Viewpoints aus natürlichsprachlichen Dokumenten gemäß **ADMBw v2025.10** (NAFv4).

> ⚠️ **Keine importierbaren Dateien.** Der Output dient als Modellierungshilfe zum manuellen Nachmodellieren in Sparx EA.

---

## 🚀 Ablauf (4 Optionen)

Der Extraktor stellt ZU BEGINN genau eine Frage:

| # | Option | Ergebnis |
|---|--------|----------|
| 1 | **Viewpoints modellieren** | KI schlägt Viewpoints vor, modelliert sie nacheinander (Metamodell + Instanz-Diagramm) |
| 2 | **ADMBw-Modell** | Prosa-Elemente direkt auf ADMBw-Stereotype gemappt (Mapping-Tabelle + Diagramm) |
| 3 | **Metamodell (generisch)** | Übertragbares Typ-Modell einer Architekturdomäne — keine Instanzen |
| 4 | **Stakeholder-Concern** | Fokussierte Modellierung eines spezifischen Erkenntnisinteresses |

Die KI wählt den jeweils besten Mermaid-Diagrammtyp selbst (`classDiagram`, `graph TD`, `sequenceDiagram`, `stateDiagram`, `gantt`, …).

---

## 📚 Wissensbasis

Vier Knowledge-Dateien (in OpenWebUI als RAG-Wissen eingebunden):

| Datei | Inhalt |
|-------|--------|
| `ADMBw-Knowledge-Stereotypes.md` | 317 Stereotype mit AppliesTo |
| `ADMBw-Knowledge-Viewpoints.md` | 53 Viewpoints mit erlaubten Elementen |
| `ADMBw-Knowledge-Topology.md` | Source → Connector → Target Regeln |
| `ADMBw-Knowledge-Connectors.md` | EA-Metatypen + Connector-Übersicht |

---

## ✅ Validierung (8-fach)

Jeder Output wird gegen alle vier Knowledge-Dateien geprüft:

| # | Check | Quelle |
|---|-------|--------|
| 1 | AppliesTo: Stereotype auf korrekte Metaklasse? | Stereotypes |
| 2 | Viewpoint-Konformität: Nur erlaubte Elemente? | Viewpoints |
| 3 | Konnektor-Metatyp korrekt? | Connectors |
| 4 | Metaconstraint: Source→Target erlaubt? | Topology |
| 5 | Vollständigkeit: Alle Prosa-Entitäten erfasst? | Prosa-Dokument |
| 6 | Namenskonsistenz über alle Artefakte | — |
| 7 | Metamodell: ALLE Typen + Beziehungen im Diagramm? | Viewpoints + Topology |
| 8 | Topologie-Richtung: Jede Kante Source→Connector→Target? | Topology |

**Eiserne Regeln:**
- ❌ Keine eigenen Stereotype erfinden
- ❌ Abstrakte Basisklassen (🔒) nie direkt verwenden

---

## 🔧 Einrichtung (OpenWebUI)

1. **Modell anlegen** → Inhalt von `system_prompt.md` ins Feld **System Prompt**
2. **Knowledge** → Vier `ADMBw-Knowledge-*.md`-Dateien hochladen und mit Modell verknüpfen
3. Fertig.

> 💡 Die PDF nicht in Knowledge laden — die MD-Dateien sind token-effizienter.

---

## 📦 Repository

| Datei | Zweck |
|-------|-------|
| `system_prompt.md` | System-Prompt (Kernlogik) |
| `ADMBw-Knowledge-Stereotypes.md` | Stereotyp-Katalog |
| `ADMBw-Knowledge-Viewpoints.md` | Viewpoint-Regeln |
| `ADMBw-Knowledge-Topology.md` | Topologie-Regeln |
| `ADMBw-Knowledge-Connectors.md` | Konnektor-Regeln |

---

**Autor:** Michael Estel (mit KI-Agent)
