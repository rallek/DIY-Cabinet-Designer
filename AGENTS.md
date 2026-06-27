# AGENTS.md

## Zweck

Diese Datei enthält Arbeitsregeln für Agenten/Codex in diesem Repository.

Projektinhalt und fachliche Details stehen in:

- `README.md`
- `docs/vision.md`
- `docs/architecture.md`
- `docs/json-format.md`
- `docs/ai-generator-skill.md`
- `schemas/cabinet.schema.json`
- `presets/README.md`

Vor relevanten Änderungen diese Dateien lesen.

## Sprache und Stil

- Dokumentation auf Deutsch schreiben.
- Deutsche Umlaute normal verwenden.
- Code, JSON-Felder, Dateinamen und technische IDs auf Englisch schreiben.
- Kurz, klar und wartbar schreiben.
- Keine Projektbeschreibung in `AGENTS.md` duplizieren.

## Zentrale Regeln

- Eine Cabinet-JSON beschreibt genau einen Korpus.
- Alle Maße in JSON-Dateien sind Millimeter.
- JSON beschreibt Regeln, keine fertig berechneten Bauteilmaße.
- Presets sind Projektbestandteil, nicht nur Beispiele.
- Body-Namen sind standardmäßig Englisch.
- Garage-Cut-relevante Daten gehören in Attribute, nicht in Body-Namen.

## Konsistenzpflicht

Bei Änderungen an Regeln, Varianten oder Datenstrukturen immer prüfen, ob diese Dateien mit angepasst werden müssen:

- `docs/json-format.md`
- `docs/ai-generator-skill.md`
- `schemas/cabinet.schema.json`
- betroffene Dateien unter `presets/`

Das gilt besonders bei Änderungen an:

- Presets
- JSON-Feldern
- System-32-Logik
- Korpusbauweisen
- Rückwänden
- Türen
- Fronten
- Schubladen
- Mittelwänden
- Beschlägen
- Garage-Cut-Attributen

## Schema und Presets

Wenn neue JSON-Felder oder Varianten eingeführt werden:

1. Schema aktualisieren.
2. JSON-Dokumentation aktualisieren.
3. AI-Generator-Skill aktualisieren.
4. Passendes Preset ergänzen oder anpassen, falls sinnvoll.

Presets müssen gültige Cabinet-JSON-Dateien sein, sobald Schema-Validierung vorhanden ist.

## Garage-Cut

Dieses Projekt ergänzt `DIY-Garage-Cut-Fusion360-Addons`.

Material-, Katalog-, Attribut- und Exportlogik nicht unnötig duplizieren.

Wenn Bodies erzeugt oder beschrieben werden, Garage-Cut-Attribute mitdenken.

## Fusion

Das Add-in erzeugt zunächst neue Korpusse.

Bestehende Korpusse müssen nicht parametrisch bearbeitbar sein.

Reproduzierbarkeit soll über gespeicherte JSON-Konfigurationen entstehen.

## Dokumente

Wenn projektbezogene Dokumente erzeugt werden:

- Standardformat: Markdown
- Sprache: Deutsch
- Papierformat bei exportierten Dokumenten: DIN A4
- Maßeinheiten: Millimeter

## Arbeitsweise

Vor Änderungen:

1. Relevante Doku lesen.
2. Bestehende Struktur respektieren.
3. Keine unnötigen Umbauten.

Nach Änderungen:

1. Doku, Schema, Skill und Presets auf Konsistenz prüfen.
2. Änderungen kurz zusammenfassen.
3. Offene TODOs klar benennen.
