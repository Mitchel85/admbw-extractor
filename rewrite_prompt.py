import re

with open('system_prompt.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Teil 0 (Quellen) - Remove PDF, add State Machine rule
old_teil0 = """| ① | **Prosa-Dokument** | .txt/.pdf/.docx | Der zu analysierende Fachtext |
| ② | **ADMBw-Dokumentation** | .pdf (Knowledge) | Offizielle ADMBw-NAFv4-Modellierungsrichtlinie |
| ③ | **ADMBw-Regelwerk** | Knowledge-Dateien | Stereotype-Katalog, Konnektor-Regeln, Metamodell-Regeln pro Viewpoint |

**Quelle ②+③ sind in OpenWebUI als Knowledge/Dateien hinterlegt. Nutze sie über RAG-Semantiksuche bei Fragen zu spezifischen Stereotypen, Viewpoints oder Konnektoren.**"""

new_teil0 = """| ① | **Prosa-Dokument** | .txt/.pdf/.docx | Der zu analysierende Fachtext |
| ② | **ADMBw-Regelwerk** | .md-Dateien | Stereotype-Katalog, Konnektor-Regeln, Viewpoint-Regeln |

**WICHTIG: Das Regelwerk (Quelle ②) besteht aus drei Markdown-Dateien. Nutze diese Dateien als strikte Nachschlagewerke anhand der Wegweiser in den Phasen. Es existieren KEINE anderen Regeln.**"""

text = text.replace(old_teil0, new_teil0)

# 2. Inject State Machine Rule at beginning of Teil 1
state_machine_rule = """
> 🛑 **STRIKTE REGEL ZUR ITERATION (STATE MACHINE):** Du darfst NIEMALS zwei Phasen gleichzeitig bearbeiten. Beende deine Antwort am Ende jeder Phase ZWINGEND mit einer Freigabefrage an den Nutzer (STOPP & WARTEN). Generiere keinen Text der Folgephase, bevor der Nutzer nicht explizit sein "Go" gegeben hat.
"""
text = text.replace("## TEIL 1: ITERATIVER WORKFLOW (CONCERN-DRIVEN & ELEMENT-FIRST)\n## ═══════════════════════════════════════════════════════════", "## TEIL 1: ITERATIVER WORKFLOW (CONCERN-DRIVEN & ELEMENT-FIRST)\n## ═══════════════════════════════════════════════════════════" + state_machine_rule)


# 3. Update Phase 2 (Stereotype Zero Tolerance)
old_phase2_step3 = "3. **Ordne Stereotype zu:** Mappe die gefundenen Entitäten und Beziehungen auf die zulässigen ADMBw-Stereotype (Konsultiere Knowledge: Stereotypes & Connectors)."
new_phase2_step3 = """3. **Ordne Stereotype zu (STRIKTE VORGABE):** Schlage JEDES gefundene Element in der Datei `ADMBw-Knowledge-Stereotypes.md` nach. Suche dort nach exakten Treffern.
   * 🚫 **ZERO TOLERANCE:** Du darfst unter KEINEN UMSTÄNDEN eigene Stereotype oder Metaklassen erfinden!
   * Verwende AUSSCHLIESSLICH die exakten Bezeichnungen aus dieser MD-Datei. Findest du keinen passenden Stereotyp, MUSST du den Nutzer warnen."""

text = text.replace(old_phase2_step3, new_phase2_step3)


# 4. Update Phase 3a (Viewpoint Pointers)
old_phase3_step2 = "2. Wähle **nur jene ADMBw-Viewpoints**, die den Concern am besten abbilden und in denen die extrahierten Stereotype zulässig sind (Konsultiere Knowledge: Viewpoints)."
new_phase3_step2 = "2. **Viewpoints filtern:** Öffne die Datei `ADMBw-Knowledge-Viewpoints.md`. Suche dort exakt nach der Überschrift des jeweiligen Viewpoints (z.B. `## S1`). Unter dieser Überschrift steht eine Liste. **NUR** Elemente, die in dieser spezifischen Liste stehen, dürfen in das Metamodell dieses Viewpoints aufgenommen werden!"

text = text.replace(old_phase3_step2, new_phase3_step2)


# 5. Update Teil 2 Check 3 (Connectors)
old_check3 = "| 3 | Beziehungstyp-Validierung | JEDE Beziehung verwendet einen EA-Metatyp aus der Konnektortabelle |"
new_check3 = "| 3 | Beziehungstyp-Validierung | Prüfe jede Beziehung zwingend in der Datei `ADMBw-Knowledge-Connectors.md`. Suche die Kombination aus Start- und Ziel-Element. Erlaube NUR Verbindungen, die dort exakt definiert sind. |"

text = text.replace(old_check3, new_check3)

# 6. Cleanup conflicting PDF mentions
text = text.replace("gemäß ADMBw-Dokumentation", "gemäß ADMBw-Regelwerk")
text = text.replace("aus PDF-Dokumentation einhalten", "aus dem Regelwerk einhalten")
text = text.replace("Der DOKUMENTATION (PDF) vertrauen", "Den Markdown-Regelwerken vertrauen")

with open('system_prompt.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Prompt successfully rewritten.")
