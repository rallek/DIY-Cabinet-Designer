# Fusion-360-Add-in-Prototyp

Dieser Ordner enthält ein minimales Fusion-360-Python-Add-in-Skeleton für den DIY Cabinet Designer.

Der Prototyp erzeugt noch keine Korpus-Geometrie und verarbeitet keine JSON-Dateien. Er registriert nur einen einfachen Button/Command, um zu prüfen, ob das Add-in in Fusion 360 geladen und ausgeführt werden kann.

## In Fusion 360 einbinden

1. Fusion 360 öffnen.
2. In den Bereich `Utilities` wechseln.
3. `Scripts and Add-Ins` öffnen.
4. Zum Reiter `Add-Ins` wechseln.
5. Über das grüne Plus bzw. `Add-Ins from my computer` den Ordner auswählen:

```text
fusion_addin/DIYCabinetDesigner
```

6. Das Add-in `DIYCabinetDesigner` auswählen und starten.
7. Im Bereich `Utilities` sollte im Panel `Scripts and Add-Ins` ein Button `DIY Cabinet Designer` erscheinen.
8. Beim Klick auf den Button erscheint die Meldung:

```text
DIY Cabinet Designer prototype command started.
```

## Dateien

- `DIYCabinetDesigner/DIYCabinetDesigner.manifest` beschreibt das Fusion-360-Add-in.
- `DIYCabinetDesigner/DIYCabinetDesigner.py` enthält den minimalen Python-Einstiegspunkt mit `run(...)` und `stop(...)`.
- `DIYCabinetDesigner/resources/` ist für ein späteres Button-Icon vorgesehen.

## Icon-Platzhalter

Aktuell ist kein eigenes Button-Icon eingebunden. Ein finales Icon kann später unter `DIYCabinetDesigner/resources/` abgelegt und dann in `DIYCabinetDesigner.py` beim Erzeugen der Button-Definition referenziert werden.
