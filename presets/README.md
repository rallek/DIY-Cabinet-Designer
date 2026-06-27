# Presets

Dieser Ordner enthält Cabinet-JSON-Dateien für typische Korpusse und Möbelvarianten.

Presets sind nicht nur Beispiele. Sie sind ein Kernbestandteil des Projekts.

Sie dienen als:

- Startpunkte für konkrete Möbel
- Testfälle für das Fusion-Add-in
- Trainings- und Referenzmaterial für den AI Generator Skill
- Grundlage für spätere Pull Requests aus der Community

## Geplante Struktur

```text
presets/
│
├── base-cabinet/
│   ├── simple_2_doors.json
│   └── drawer_stack_3_drawers.json
│
├── wall-cabinet/
│   └── simple_1_door.json
│
├── shelf/
│   └── simple_shelf.json
│
└── README.md
```

## Anforderungen an Presets

Ein Preset soll:

- genau einen Korpus beschreiben
- eine gültige Cabinet-JSON-Datei sein
- Maße in Millimetern verwenden
- Regeln statt fertig berechneter Bauteilmaße enthalten
- Garage-Cut-Informationen berücksichtigen
- System-32-Defaults nutzen, wo sinnvoll
- nur projektrelevante Annahmen treffen

## Namenskonvention

Dateinamen sollen kleingeschrieben sein und Bindestriche oder Unterstriche verwenden.

Beispiele:

```text
simple_2_doors.json
drawer_stack_3_drawers.json
base_cabinet_left_drawers_right_door.json
```

## Spätere Pull Requests

Neue Presets können später über Pull Requests ergänzt werden.

Ein gutes Preset sollte zusätzlich dokumentieren:

- wofür es gedacht ist
- welche Defaults verwendet wurden
- welche Möbelvariante es beschreibt
- ob besondere System-32- oder Hardware-Annahmen enthalten sind

## Aktueller Status

Noch keine finalen Presets vorhanden.

Zuerst müssen JSON-Format und Schema stabilisiert werden.