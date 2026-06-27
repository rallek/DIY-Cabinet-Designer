# Projektvision

DIY Cabinet Designer ist ein Open-Source-Add-in für Autodesk Fusion 360, das rechteckige Schrankkorpusse parametrisch aus JSON-basierten Konstruktionsregeln erzeugt.

Das Tool entsteht primär für den eigenen Möbelbau-Workflow, soll aber so dokumentiert und strukturiert werden, dass andere Maker und DIY-Anwender es ebenfalls nutzen und erweitern können.

Der Fokus liegt nicht auf maximaler CAD-Freiheit, sondern auf schneller, geführter Erzeugung wiederkehrender Möbelkonstruktionen.

## Kernnutzen

Der Cabinet Designer soll Arbeit sparen, wenn in Fusion 360 neue Schrankkorpusse erzeugt werden müssen.

Statt jeden Korpus manuell zu modellieren, soll eine Konfiguration geladen werden. Aus dieser erzeugt das Add-in eine Fusion-Komponente mit Bodies, Bohrungen, Lochreihen und Garage-Cut-Attributen.

## Unterstützte Möbeltypen

Zunächst werden nur rechteckige Korpusse unterstützt.

Geplante Möbeltypen:

- Unterschrank
- Hängeschrank
- Regal
- Schubladenschrank
- freier rechteckiger Korpus

Die Möbeltypen sind als Startvorlagen zu verstehen. Danach soll der konkrete Aufbau über JSON-Regeln beschrieben werden.

## Grundprinzipien

- Eine JSON-Datei beschreibt genau einen Korpus.
- Alle Maße werden in Millimetern angegeben.
- Die JSON beschreibt Regeln, nicht fertig berechnete Bauteilmaße.
- Fusion erzeugt daraus die tatsächliche Geometrie.
- Ein Korpus wird in Fusion als eigene Komponente erzeugt.
- Bauteile wie Seiten, Boden, Deckel, Türen, Schubladenteile und Einlegeböden werden als Bodies innerhalb dieser Komponente erzeugt.
- Die erzeugten Bodies werden direkt mit Garage-Cut-Attributen versehen.

## Konstruktionsumfang

Das Tool soll zunächst folgende Elemente unterstützen:

- rechteckiger Korpus
- zwei Korpusbauweisen:
  - durchgehender Boden und durchgehender Deckel
  - durchgehende Seitenteile
- auswählbare Rückwand:
  - eingenutete Rückwand
  - hinten aufgesetzte Rückwand
- variable Rückwandstärke, z. B. 3 mm, 4 mm, 6 mm, 8 mm oder Plattenmaterialstärke
- Türen
- Schubladen inklusive konstruktivem Innenleben
- lose Einlegeböden
- Mittelwände
- System-32-Lochreihen
- Topfbohrungen und Befestigungsbohrungen für Scharniere
- Bohrlogik für Schubladenauszüge

## System 32

DIY Cabinet Designer soll mit sinnvollen Standardwerten aus dem System 32 arbeiten.

Diese Werte werden als Defaults verwendet, bleiben aber änderbar. Typische Werte wie 37 mm Abstand zur Vorderkante oder ein 32-mm-Raster sollen also nicht hart verdrahtet sein.

Der Nutzer bzw. die JSON-Konfiguration soll Startpositionen von Lochreihen anpassen können. Sonderfälle wie 38 mm, 40 mm, 120 mm oder projektspezifische Werte müssen möglich bleiben.

## Beschläge

Beschläge müssen zunächst nicht als sichtbare 3D-Komponenten modelliert werden.

Wichtiger ist, dass die notwendigen Bohrungen, Topfbohrungen und Befestigungspunkte korrekt erzeugt oder als Fertigungsinformation hinterlegt werden.

Das Modell soll wissen, welcher Beschlag oder welche Beschlagklasse an einer Stelle vorgesehen ist. Die sichtbare 3D-Darstellung von Scharnieren, Auszügen oder anderen Beschlägen kann später ergänzt werden, besonders wenn passende CAD-Daten verfügbar sind.

## Fronten

Fronten müssen parametrisch definiert werden.

Unterstützt werden sollen mindestens:

- aufliegende Fronten
- innenliegende Fronten
- teilaufliegende Fronten
- einstellbares Fugenmaß

Türen, Schubladen und Einlegeböden sollen kombinierbar sein. Ein Korpus kann z. B. unten Schubladen und oben Türen besitzen. Hinter Türen können zusätzlich Einlegeböden liegen.

## Garage-Cut-Integration

Dieses Projekt ergänzt das bestehende Garage-Cut-Fusion-Add-in.

Die erzeugten Bodies müssen direkt mit passenden Garage-Cut-Attributen versehen werden, damit der spätere Export funktioniert.

Body-Namen sollen standardmäßig englisch sein. Sie dienen als technische Default-Namen, können aber in Fusion mit vorhandenen Tools überschrieben werden. Wenn ein Nutzer Body-Namen nachträglich ändert, gelten diese Namen für den Export.

Der Möbeltyp muss nicht im Body-Namen stehen. Diese Information ergibt sich aus der übergeordneten Fusion-Komponente.

Material, Stärke, Kanteninformationen und weitere Fertigungsdaten sollen nicht im Namen kodiert werden, sondern über Garage-Cut-Metadaten und JSON-Regeln entstehen.

## Nicht-Ziele der ersten Version

Nicht im Fokus der ersten Version:

- freie Möbelgeometrien außerhalb rechteckiger Korpusse
- technische Zeichnungen
- vollständige CNC-Ausgabe
- direkte Nachbearbeitung bereits erzeugter Korpusse in Fusion
- vollständige 3D-Darstellung aller Beschläge

Eine spätere Reproduzierbarkeit soll eher über gespeicherte JSON-Konfigurationen entstehen: Ein Korpus kann aus seiner Konfiguration erneut erzeugt werden, statt ein vorhandenes Modell parametrisch zurückzubauen.