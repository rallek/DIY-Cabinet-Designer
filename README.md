# DIY Cabinet Designer

DIY Cabinet Designer ist ein Open-Source-Add-in für Autodesk Fusion 360 zur Erzeugung rechteckiger Schrankkorpusse aus JSON-basierten Konstruktionsregeln.

Das Projekt entsteht primär als persönliches Produktivitätswerkzeug für den Möbelbau, soll aber so dokumentiert und strukturiert werden, dass andere Maker und DIY-Anwender es nutzen und erweitern können.

## Ziel

Das Tool soll wiederkehrende CAD-Arbeit beim Erzeugen neuer Schrankkorpusse reduzieren.

Aus einer strukturierten Cabinet-JSON-Datei erzeugt das Fusion-Add-in eine saubere 3D-Konstruktion mit benannten Bodies und Garage-Cut-Attributen.

Der Fokus liegt auf:

- rechteckigen Korpussen
- Unterschränken, Hängeschränken, Regalen und Schubladenschränken
- Türen, Schubladen, Einlegeböden und Mittelwänden
- System-32-Logik für Lochreihen, Topfbänder und Schubladenauszüge
- Garage-Cut-kompatiblen Body-Namen und Attributen
- KI-freundlichen JSON-Konfigurationen

## Grundidee

Fusion 360 bleibt das CAD-System.

DIY Cabinet Designer erzeugt neue Korpusse aus Regeln. Die Zuschnittlisten, Stücklisten und weitere Fertigungsdaten werden nicht direkt in diesem Projekt gelöst, sondern über das bestehende Garage-Cut-Toolset weiterverarbeitet.

Dieses Projekt baut auf folgendem Repository auf:

- <https://github.com/rallek/DIY-Garage-Cut-Fusion360-Addons>

Dort liegen Materiallogik, Metadaten, Attribute, Katalogansätze und Exportlogik, auf denen dieses Add-in aufbauen soll.

## Projektstatus

Frühe Konzeptphase.

Aktuell geht es darum, Zielbild, Datenmodell, JSON-Struktur und Architektur zu dokumentieren, bevor konkrete Implementierungsschritte erfolgen.

## Dokumentation

- [docs/vision.md](docs/vision.md)
- [docs/architecture.md](docs/architecture.md)
- [docs/json-format.md](docs/json-format.md)
- [docs/ai-generator-skill.md](docs/ai-generator-skill.md)
- [presets/README.md](presets/README.md)

## Geplante Projektstruktur

```text
DIY-Cabinet-Designer/
│
├── docs/
│   ├── vision.md
│   ├── architecture.md
│   ├── json-format.md
│   └── ai-generator-skill.md
│
├── presets/
│   └── README.md
│
├── schemas/
│   └── cabinet.schema.json
│
├── fusion_addin/
│   └── ...
│
└── README.md
```

## MVP-Idee

Ein erster brauchbarer Stand ist erreicht, wenn das Add-in eine Cabinet-JSON laden und daraus einen einfachen rechteckigen Korpus in Fusion erzeugen kann.

Der Nutzer soll mindestens festlegen können:

- Außenmaß: Breite, Höhe, Tiefe
- Materialstärke
- Korpusbauweise
- Rückwandtyp
- Lochreihen ja/nein
- Türen ja/nein
- Schubladen ja/nein
- Einlegeböden ja/nein

Das Ergebnis ist eine Fusion-Komponente mit sinnvoll benannten Bodies und Garage-Cut-Attributen.