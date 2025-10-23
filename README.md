# Doorbell Fingerprint

Custom Integration für Home Assistant OS, die eine Fingerprint Benutzerverwaltung über die Sidebar anbietet.

## Funktionen

- Sidebar-Menüpunkt "Fingerprint" mit Fingerabdruck-Icon
- Einfaches Frontend mit Überschrift "Fingerprint Benutzerverwaltung"
- Vollständig in Home Assistant integriert, kein manuelles Kopieren von Dateien nötig

## Installation

1. Füge in HACS unter **Integrationen > Drei-Punkte-Menü > Custom Repositories** die URL dieses Repositories hinzu:  
   `https://github.com/marimpler/doorbell-fingerprint`

2. Wähle als Kategorie `Integration` und füge hinzu.

3. Suche in HACS nach "Doorbell Fingerprint" und installiere die Integration.

4. Starte Home Assistant neu.

5. In der Sidebar erscheint nun der Menüpunkt **Fingerprint** mit Fingerabdruck-Icon.

6. Klicke auf **Fingerprint**, um die Benutzerverwaltung zu öffnen (es erscheint die Überschrift „Fingerprint Benutzerverwaltung“).

## Nutzung

Diese Integration ist derzeit eine Basis für deine weitere Entwicklung der Fingerprint-Verwaltung.

---

## Entwickler-Hinweise

- Frontend-Code liegt im `frontend/` Ordner und wird automatisch geladen.
- Backend-Setup ist minimal, kann erweitert werden.

---

## Lizenz

MIT Lizenz © 2025 [marimpler](https://github.com/marimpler)
