import re

with open("system_prompt.md", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update Phase 1 End (Ask for Option A/B)
old_phase1_end = """**Frage an den Nutzer (Gatekeeper):**
> Trifft das dein Ziel genau, oder soll ich den Fokus noch anpassen? (Falls nicht angegeben: Bitte nenne mir dein genaues Ziel/Erkenntnisinteresse für dieses Dokument).
⏳ _Warte auf dein Feedback._
```"""

new_phase1_end = """**Frage an den Nutzer (Gatekeeper):**
> 1. Trifft das dein Ziel genau, oder soll ich den Fokus noch anpassen?
> 2. **Bitte wähle deinen Modellierungs-Pfad:**
>    - **Option A (Standard-Viewpoints):** Wir leiten nach der Extraktion direkt die passenden NAF-Viewpoints ab und gehen diese einzeln durch.
>    - **Option B (Custom Concern-Metamodell):** Wir bauen zuerst eine ebenenübergreifende Gesamtsicht (individuelles Metamodell), um das große Ganze zu prüfen. Du kannst danach immer noch Standard-Viewpoints generieren lassen!
⏳ _Warte auf dein Feedback und deine Pfad-Entscheidung (A oder B)._
```"""
text = text.replace(old_phase1_end, new_phase1_end)

# 2. Add Metamodell-Brücken-Regel to Phase 2
old_phase2_step3 = """3. **Ordne Stereotype zu (STRIKTE VORGABE):** Schlage JEDES gefundene Element in der Datei `ADMBw-Knowledge-Stereotypes.md` nach. Suche dort nach exakten Treffern.
   * 🚫 **ZERO TOLERANCE:** Du darfst unter KEINEN UMSTÄNDEN eigene Stereotype oder Metaklassen erfinden!
   * Verwende AUSSCHLIESSLICH die exakten Bezeichnungen aus dieser MD-Datei. Findest du keinen passenden Stereotyp, MUSST du den Nutzer warnen."""

new_phase2_step3 = """3. **Ordne Stereotype zu (STRIKTE VORGABE):** Schlage JEDES gefundene Element in der Datei `ADMBw-Knowledge-Stereotypes.md` nach. Suche dort nach exakten Treffern.
   * 🚫 **ZERO TOLERANCE:** Du darfst unter KEINEN UMSTÄNDEN eigene Stereotype oder Metaklassen erfinden!
   * Verwende AUSSCHLIESSLICH die exakten Bezeichnungen aus dieser MD-Datei. Findest du keinen passenden Stereotyp, MUSST du den Nutzer warnen.
4. **Metamodell-Brücken-Regel (Failing Forward):** Wenn der Text Element A direkt mit Element C verbindet, das Regelwerk (`ADMBw-Knowledge-Connectors.md`) diese direkte Kante aber verbietet, darfst du KEINEN Konnektor erfinden. Suche den erlaubten Zwischenschritt (z.B. A -> B -> C) und füge das fehlende Element B als `(implizit / ausstehend)` markiert zum Graphen hinzu."""
text = text.replace(old_phase2_step3, new_phase2_step3)

text = text.replace("4. **Erstelle eine Vorschlagsliste:**", "5. **Erstelle eine Vorschlagsliste (Master-Graph):**")
text = text.replace("5. **STOPP & WARTEN:**", "6. **STOPP & WARTEN:**")
text = text.replace("6. **Warte auf Nutzerfeedback.**", "7. **Warte auf Nutzerfeedback.**")

# 3. Rewrite Phase 3 to handle the Fork (A vs B)
old_phase3 = """### 🔄 SCHRITT 3: VIEWPOINT-ABLEITUNG & ITERATIVE VERARBEITUNG
Nachdem der Nutzer den Architektur-Graphen (Schritt 2) bestätigt hat, ordnest du nun die passenden Viewpoints zu.

#### Phase 3a: Viewpoint-Zuordnung
1. **Analysiere das freigegebene Metamodell-Netz** aus Schritt 2.
2. **Viewpoints filtern:** Öffne die Datei `ADMBw-Knowledge-Viewpoints.md`. Suche dort exakt nach der Überschrift des jeweiligen Viewpoints (z.B. `## S1`). Unter dieser Überschrift steht eine Liste. **NUR** Elemente, die in dieser spezifischen Liste stehen, dürfen in das Metamodell dieses Viewpoints aufgenommen werden!
3. Melde dem Nutzer, welche Viewpoints generiert werden.

#### Phase 3b: Ausgabe pro Viewpoint (MARKDOWN + HTML-OPTION)"""

new_phase3 = """### 🔄 SCHRITT 3: ABZWEIGUNG (OPTION A vs. OPTION B)
Nachdem der Nutzer den Master-Graphen (Schritt 2) bestätigt hat, reagierst du auf seine Pfad-Entscheidung aus Schritt 1.

#### Wenn der Nutzer "Option B (Custom Concern-Metamodell)" gewählt hat:
1. Generiere sofort eine **Custom Concern-View**. Diese Sicht ist ebenenübergreifend und beinhaltet ALLE Elemente und Relationen aus dem validierten Master-Graphen.
2. Erstelle dafür das Markdown-Artefakt (analog zu Phase 3b, aber ohne Viewpoint-Kürzel, Titel z.B. "Custom Concern-View").
3. Wende auch hier den strengen 7-fachen Double-Check an.
4. **Nach der Ausgabe von Option B fragst du den Nutzer:** *"Möchten Sie auf Basis dieses validierten Custom Metamodells nun standardisierte NAF-Viewpoints ableiten lassen (Wechsel zu Option A)?"*

#### Wenn der Nutzer "Option A (Standard-Viewpoints)" gewählt hat (oder von B hierher wechselt):
1. **Analysiere das freigegebene Master-Netz**.
2. **Viewpoints filtern:** Öffne die Datei `ADMBw-Knowledge-Viewpoints.md`. Suche dort exakt nach der Überschrift des jeweiligen Viewpoints (z.B. `## S1`). **NUR** Elemente, die in dieser spezifischen Liste stehen, dürfen in die Sicht dieses Viewpoints aufgenommen werden!
3. Melde dem Nutzer, welche Viewpoints generiert werden, und warte auf sein Go für den ersten.

#### Phase 3b: Ausgabe (MARKDOWN + HTML-OPTION)"""
text = text.replace(old_phase3, new_phase3)

# 4. Enhance Double Check 3
old_check3 = "| 3 | Beziehungstyp-Validierung | Prüfe jede Beziehung zwingend in der Datei `ADMBw-Knowledge-Connectors.md`. Suche die Kombination aus Start- und Ziel-Element. Erlaube NUR Verbindungen, die dort exakt definiert sind. |"
new_check3 = "| 3 | Beziehungstyp-Validierung (Matrix-Check) | JEDE Kante MUSS als exakte Dreierkombination (Quelle -> Konnektor -> Ziel) in `ADMBw-Knowledge-Connectors.md` stehen. Erlaube KEINE anderen Verbindungen! |"
text = text.replace(old_check3, new_check3)


with open("system_prompt.md", "w", encoding="utf-8") as f:
    f.write(text)

print("Patched successfully")
