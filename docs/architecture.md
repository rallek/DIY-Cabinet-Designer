# Architektur

DIY Cabinet Designer soll als KI-gestützter Korpus-Generator mit Fusion 360 als Ausführungsumgebung entwickelt werden.

Die zentrale Architekturidee ist:

```text
Möbelidee / Beschreibung
        ↓
KI-Generator / Preset
        ↓
validierte Cabinet-JSON
        ↓
Fusion Add-in
        ↓
Fusion-Komponente mit Bodies, Bohrungen und Garage-Cut-Attributen
        ↓
optional: Weiterarbeit in Fusion 360
        ↓
Garage-Cut-CSV-Export
        ↓
Zuschnittprogramm und weitere Fertigungswerkzeuge
```

Fusion 360 ist damit nicht die primäre Entwurfsoberfläche, sondern vor allem CAD-, Geometrie- und Ausführungsumgebung. Der eigentliche Entwurf wird perspektivisch über KI, Presets und validierte Cabinet-JSON-Dateien beschrieben.

## Schichten

### 1. Cabinet-JSON

Die Cabinet-JSON ist das zentrale Eingabeformat.

Sie beschreibt einen Korpus durch Regeln:

- Außenmaße
- Materialreferenzen
- Korpusbauweise
- Rückwand
- Innenaufteilung
- Türen
- Schubladen
- Einlegeböden
- Mittelwände
- Lochreihen
- Beschlaglogik
- Kanteninformationen
- Fertigungshinweise

Die JSON enthält keine fertig berechneten Zuschnittmaße. Diese berechnet das Add-in.

### 2. Presets

Presets sind konkrete Cabinet-JSON-Dateien.

Sie sind nicht nur Beispiele, sondern Teil des Projekts. Neue Möbel- oder Korpuskonfigurationen können später über Pull Requests ergänzt werden.

Beispiele:

- Unterschrank mit zwei Türen
- Hängeschrank mit einer Tür
- Schubladenschrank mit drei Schubladen
- Regal mit Einlegeböden

### 3. KI-Generator-Skill

Der Generator ist zunächst kein eigenes Programm, sondern eine KI-freundliche Spezifikation.

Ziel ist, dass eine KI aus einer Möbelbeschreibung eine technisch gültige Cabinet-JSON-Datei erzeugen kann.

Der KI-Generator ist perspektivisch die eigentliche Entwurfslogik des Projekts. Er übersetzt Anforderungen, Varianten und Presets in eine eindeutige technische Beschreibung.

Dafür braucht das Projekt:

- klare Regeln
- ein JSON-Schema
- gute Presets
- Validierungsregeln
- Beispiele für Eingaben und erwartete Ausgaben

### 4. Fusion Add-in

Das Fusion Add-in lädt eine Cabinet-JSON-Datei und erzeugt daraus Geometrie.

Das Add-in soll möglichst wenig Entwurfslogik in Dialoge verlagern. Seine Hauptaufgabe ist die robuste Ausführung der JSON-Regeln in Fusion.

Aufgaben des Add-ins:

- JSON-Datei laden
- JSON validieren
- Maße und Konstruktionsregeln auswerten
- Fusion-Komponente erzeugen
- Bodies erzeugen
- Bohrungen und Lochreihen erzeugen
- Garage-Cut-Attribute setzen
- sinnvolle Body-Namen vergeben

### 5. Weiterarbeit in Fusion

Der erzeugte Korpus kann in Fusion 360 weiterbearbeitet werden.

Das ist eine Möglichkeit, aber nicht zwingend Teil des Hauptworkflows. Ein Korpus soll auch direkt aus der erzeugten Geometrie und den Garage-Cut-Attributen weiterverarbeitet werden können.

### 6. Garage-Cut-Integration

Das bestehende Garage-Cut-Fusion-Add-in bleibt verantwortlich für:

- Materiallogik
- Kataloge
- Bauteil-Metadaten
- Kanteninformationen
- Exportlogik
- CSV-Ausgabe
- weitere externe Fertigungsdaten

DIY Cabinet Designer soll diese Daten vorbereiten, nicht ersetzen.

Der CSV-Export aus Garage Cut ist der Übergang zu Zuschnittprogrammen und weiteren Fertigungswerkzeugen.

## Fusion-Modellstruktur

Ein erzeugter Korpus soll in Fusion als eigene Komponente entstehen.

Innerhalb dieser Komponente liegen die einzelnen Bodies.

Beispiel:

```text
Base Cabinet 001
├── left_side
├── right_side
├── bottom
├── top
├── back_panel
├── shelf_01
├── door_01
├── door_02
├── drawer_01_front
├── drawer_01_left_side
├── drawer_01_right_side
├── drawer_01_back
└── drawer_01_bottom
```

Die Komponente gibt den Möbelkontext. Die Body-Namen beschreiben den Bauteiltyp.

## Reproduzierbarkeit

Das Tool soll zunächst neue Korpusse erzeugen, nicht bestehende Korpusse parametrisch bearbeiten.

Eine spätere Bearbeitung kann über gespeicherte JSON-Konfigurationen gelöst werden:

1. JSON ändern
2. Korpus neu erzeugen
3. vorhandenes Modell bei Bedarf ersetzen oder vergleichen

Damit bleibt die Logik einfacher und robuster als eine vollständige Rückwärtsparametrisierung bestehender Fusion-Geometrie.

## Offene Architekturfragen

- Wie genau wird die Garage-Cut-Materialbibliothek referenziert?
- Wo liegen Beschlagkataloge für Scharniere, Auszüge und System-32-Komponenten?
- Wird JSON direkt im Fusion-Add-in ausgewählt oder über Preset-Listen geladen?
- Wie wird validiert, ob eine Konfiguration konstruktiv sinnvoll ist?
- Soll das Add-in später erzeugte JSON-Konfigurationen im Fusion-Modell als Attribute speichern?
- Wie viel Bedienoberfläche braucht das Fusion-Add-in, wenn der Entwurf primär über KI und JSON entsteht?