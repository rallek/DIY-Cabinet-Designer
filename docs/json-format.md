# Cabinet-JSON-Format

Dieses Dokument beschreibt die Grundidee des Cabinet-JSON-Formats.

Das Format ist noch nicht final. Es dient als Arbeitsgrundlage für Schema, Presets, KI-Generator und Fusion-Add-in.

## Grundregeln

- Eine JSON-Datei beschreibt genau einen Korpus.
- Alle Maße werden in Millimetern angegeben.
- Die JSON beschreibt Regeln, nicht fertig berechnete Bauteilmaße.
- Das Fusion-Add-in berechnet aus diesen Regeln die konkrete Geometrie.
- Die JSON soll technisch vollständig und eindeutig sein.
- Menschenlesbarkeit ist hilfreich, aber nicht wichtiger als Validierbarkeit und KI-Verwendbarkeit.

## Grobe Struktur

Eine Cabinet-JSON kann perspektivisch diese Bereiche enthalten:

```json
{
  "schema_version": "0.1",
  "cabinet": {},
  "materials": {},
  "construction": {},
  "back_panel": {},
  "system32": {},
  "layout": {},
  "fronts": {},
  "drawers": {},
  "hardware": {},
  "garage_cut": {}
}
```

Diese Struktur ist ein Vorschlag und wird später durch ein echtes JSON-Schema präzisiert.

## Cabinet

Allgemeine Daten zum Korpus.

Beispiel:

```json
{
  "cabinet": {
    "id": "base_cabinet_001",
    "type": "base_cabinet",
    "name": "Base Cabinet 001",
    "dimensions_mm": {
      "width": 800,
      "height": 720,
      "depth": 560
    }
  }
}
```

Die Maße sind Außenmaße.

## Materials

Materialien sollen möglichst als Referenzen auf das bestehende Garage-Cut-Katalogsystem gespeichert werden.

Beispiel:

```json
{
  "materials": {
    "carcass": {
      "material_ref": "sheet_white_18",
      "thickness_mm": 18
    },
    "back_panel": {
      "material_ref": "hdf_white_4",
      "thickness_mm": 4
    }
  }
}
```

Die exakte Kopplung an den Garage-Cut-Katalog ist noch offen.

## Construction

Die Korpusbauweise beschreibt, welche Platten durchgehend sind.

Beispiel:

```json
{
  "construction": {
    "carcass_style": "continuous_sides"
  }
}
```

Mögliche Werte:

- `continuous_sides`
- `continuous_top_bottom`

## Back panel

Die Rückwand soll auswählbar sein.

Beispiel:

```json
{
  "back_panel": {
    "type": "grooved",
    "thickness_mm": 4,
    "groove_depth_mm": 6,
    "groove_offset_from_back_mm": 10
  }
}
```

Mögliche Typen:

- `none`
- `grooved`
- `applied_back`

## System 32

System-32-Werte sollen als Defaults gelten und überschreibbar sein.

Beispiel:

```json
{
  "system32": {
    "enabled": true,
    "hole_spacing_mm": 32,
    "front_offset_mm": 37,
    "default_hole_diameter_mm": 5,
    "rows": [
      {
        "id": "left_front_row",
        "side": "left",
        "position": "front",
        "start_z_mm": 64,
        "end_z_mm": 640
      }
    ]
  }
}
```

Startpositionen und Offsets müssen anpassbar bleiben.

## Layout

Die Innenaufteilung wird durch Regeln beschrieben.

Beispiele für mögliche Elemente:

- Bereiche
- Mittelwände
- feste konstruktive Böden
- lose Einlegeböden
- Türen
- Schubladen

Noch offen ist, ob das Layout eher als Zeilen-/Spaltenmodell, Bereichsbaum oder freie Zonenstruktur beschrieben wird.

## Fronts

Fronten sollen parametrisch definiert werden.

Mögliche Typen:

- `overlay`
- `inset`
- `partial_overlay`

Beispiel:

```json
{
  "fronts": {
    "default_type": "overlay",
    "gap_mm": 2
  }
}
```

## Drawers

Schubladen sollen konstruktiv relevant sein, nicht nur optische Fronten.

Das Add-in soll daraus Holzmaße für Schubladenseiten, Rückstück, Vorderstück und Boden ableiten können.

Beispiel:

```json
{
  "drawers": {
    "default_box": {
      "material_ref": "sheet_white_12",
      "bottom_material_ref": "hdf_white_4",
      "bottom_type": "grooved"
    }
  }
}
```

Die genaue Auszugslogik ist noch offen und hängt von späteren Hardware-Katalogen ab.

## Hardware

Hardware wird zunächst nicht zwingend als 3D-Geometrie erzeugt.

Wichtiger sind:

- Topfbohrungen
- Befestigungsbohrungen
- Schubladenauszug-Bohrbilder
- Referenz auf Beschlagtyp oder Beschlagklasse

Beispiel:

```json
{
  "hardware": {
    "hinges": {
      "default_ref": "concealed_hinge_35mm_system32"
    },
    "drawer_slides": {
      "default_ref": "drawer_slide_system32_generic"
    }
  }
}
```

## Garage Cut

Garage-Cut-Informationen werden auf die erzeugten Bodies geschrieben.

Mögliche Daten:

- Bauteiltyp
- Materialreferenz
- Kanteninformationen
- Fertigungshinweise
- Export-Flag
- Bemerkungen

Beispiel:

```json
{
  "garage_cut": {
    "export_enabled": true,
    "default_edge_banding": {
      "front": "edge_white_1mm"
    }
  }
}
```

## Offene Fragen

- Exakte Referenzierung von Material- und Beschlagkatalogen
- Finales Layout-Modell
- Validierungsregeln für konstruktiv unmögliche Konfigurationen
- Umgang mit wiederholbaren Presets
- Speicherung der JSON-Konfiguration im Fusion-Modell