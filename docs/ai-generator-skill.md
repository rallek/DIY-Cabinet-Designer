# AI Generator Skill

Dieses Dokument beschreibt die Idee eines KI-gestützten Generators für Cabinet-JSON-Dateien.

Der Generator ist zunächst kein eigenes Programm. Er ist eine technische Beschreibung, mit der eine KI aus einer Möbelbeschreibung eine vollständige und gültige Cabinet-JSON erzeugen kann.

## Ziel

Eine KI soll aus einer natürlichsprachlichen Beschreibung eine technisch vollständige Korpus-Konfiguration erzeugen.

Beispiel-Eingabe:

```text
Erzeuge einen Unterschrank, 800 mm breit, 720 mm hoch, 560 mm tief,
18 mm Material, zwei Türen, ein Einlegeboden, System-32-Lochreihen.
```

Erwartete Ausgabe:

```text
Eine gültige Cabinet-JSON-Datei, die genau diesen Korpus beschreibt.
```

## Rolle der KI

Die KI soll nicht nur Text umformatieren, sondern fehlende Standardwerte sinnvoll ergänzen.

Dazu gehören z. B.:

- System-32-Defaultwerte
- sinnvolle Body-Namen
- Standard-Fugenmaße
- Standard-Lochreihen
- Standard-Rückwandannahmen
- Standard-Korpusbauweisen
- Default-Materialstärken, sofern nicht anders angegeben

Wichtig: Defaults müssen erkennbar und überschreibbar bleiben.

## Grundregeln für die KI

1. Eine erzeugte JSON beschreibt genau einen Korpus.
2. Alle Maße sind Millimeter.
3. Außenmaße sind die primären Eingabemaße.
4. Die JSON beschreibt Regeln, keine fertig berechneten Bauteilmaße.
5. Die JSON muss technisch vollständig sein.
6. Unklare Angaben sollen mit sinnvollen Defaults gefüllt werden.
7. Kritische fehlende Angaben sollen markiert oder abgefragt werden.
8. Garage-Cut-Integration muss berücksichtigt werden.
9. System-32-Logik soll verwendet werden, wo sie sinnvoll ist.
10. Die Ausgabe soll validierbar gegen ein JSON-Schema sein.

## Eingabearten

Die KI soll perspektivisch verschiedene Eingaben verarbeiten können:

### Kurze Möbelbeschreibung

```text
Hängeschrank 600 x 720 x 350, eine Tür, zwei Einlegeböden.
```

### Detaillierte Möbelbeschreibung

```text
Unterschrank 900 breit, 720 hoch, 560 tief.
Links zwei Schubladen, rechts eine Tür mit einem Einlegeboden dahinter.
18 mm Spanplatte, 4 mm eingenutete Rückwand, aufliegende Fronten mit 2 mm Fuge.
```

### Änderungsbeschreibung

```text
Nimm das Preset base_cabinet_2_doors und ändere die Breite auf 1000 mm.
Füge mittig eine Mittelwand hinzu und mache links drei Schubladen.
```

## Ausgabeprinzip

Die KI soll am Ende eine vollständige Cabinet-JSON erzeugen.

Nicht ausreichend sind:

- reine Stichpunkte
- unvollständige Fragmente
- berechnete Zuschnittlisten statt Regeln
- Fusion-Code statt JSON

## Umgang mit Defaults

Defaults dürfen verwendet werden, müssen aber aus dokumentierten Regeln stammen.

Beispiele:

- Einheit: mm
- System-32-Raster: 32 mm
- Standard-Abstand zur Vorderkante: 37 mm
- Standard-Lochdurchmesser für Lochreihen: 5 mm
- Standard-Fugenmaß: projektabhängig, z. B. 2 mm

Diese Werte sind Startannahmen und können im JSON überschrieben werden.

## Konstruktionslogik

Die KI soll Korpusdetails nicht als fertige Plattenmaße ausgeben.

Falsch:

```json
{
  "left_side": {
    "width": 720,
    "height": 560,
    "thickness": 18
  }
}
```

Richtig:

```json
{
  "cabinet": {
    "dimensions_mm": {
      "width": 800,
      "height": 720,
      "depth": 560
    }
  },
  "construction": {
    "carcass_style": "continuous_sides"
  }
}
```

Das Fusion-Add-in berechnet daraus die realen Body-Abmessungen.

## Preset-basierter Workflow

Langfristig soll die KI bestehende Presets nutzen können.

Beispiel:

1. Nutzer wählt oder beschreibt Möbeltyp.
2. KI sucht passendes Preset.
3. KI passt Preset an Anforderungen an.
4. KI erzeugt vollständige Cabinet-JSON.
5. Fusion Add-in lädt JSON und erzeugt Geometrie.

## Pull-Request-Modell

Neue Korpustypen und Möbelvarianten können später als Pull Request ergänzt werden.

Ein guter Pull Request für ein Preset sollte enthalten:

- neue Cabinet-JSON
- kurze Beschreibung
- erwarteter Möbeltyp
- verwendete Annahmen
- Hinweis auf verwendete System-32- oder Hardware-Defaults
- ggf. Screenshot aus Fusion

## Erste Ausbaustufe

Die erste Version dieses Skills sollte nur einfache Fälle unterstützen:

- ein rechteckiger Korpus
- Außenmaße
- Materialstärke
- Korpusbauweise
- Rückwandtyp
- Türen
- lose Einlegeböden
- einfache System-32-Lochreihen

Schubladen, Mittelwände, komplexe Frontaufteilungen und Hardware-Kataloge können danach ergänzt werden.

## Offene Punkte

- finales JSON-Schema
- konkreter Prompt für KI-Generierung
- Validierungslogik
- Beispielbibliothek
- Umgang mit fehlenden Pflichtangaben
- automatische Ableitung sinnvoller Defaults
- Testfälle für KI-generierte JSON-Dateien