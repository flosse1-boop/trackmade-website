#!/usr/bin/env python3
"""Baut die Seiten von trackmade.de (DE + EN) aus gemeinsamen Bausteinen. Aufruf: python3 tools/build.py"""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = "Florian Felix Scheuermann"
STREET = "Nördliche Auffahrtsallee 45"
CITY = "80638 München"
COUNTRY_DE, COUNTRY_EN = "Deutschland", "Germany"
MAIL = "support@trackmade.de"
STAND_DE, STAND_EN = "Stand: 17. November 2026", "Last updated: November 17, 2026"

def page(lang, title, body, path, other):
    up = "../" if lang == "en" else ""
    nav = ({"home": "", "privacy": "datenschutz.html", "imprint": "impressum.html", "support": "support.html"} if lang == "de"
           else {"home": "", "privacy": "privacy.html", "imprint": "imprint.html", "support": "support.html"})
    labels = ({"privacy": "Datenschutz", "imprint": "Impressum", "support": "Support"} if lang == "de"
              else {"privacy": "Privacy", "imprint": "Legal Notice", "support": "Support"})
    switch = ("English", f"en/{other}") if lang == "de" else ("Deutsch", f"../{other}")
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{'Trackmade – deine eigene Tracking-App fürs iPhone.' if lang == 'de' else 'Trackmade – your own tracking app for iPhone.'}">
<link rel="stylesheet" href="{up}style.css">
<link rel="icon" href="{up}img/icon.png">
<link rel="apple-touch-icon" href="{up}img/apple-touch-icon.png">
</head>
<body>
<header><div class="wrap">
  <a class="brand" href="{up}{'' if lang == 'de' else 'en/'}"><img src="{up}img/icon.png" alt=""> Trackmade</a>
  <a class="lang" href="{switch[1]}">{switch[0]}</a>
</div></header>
{body}
<footer><div class="wrap">
  <span>© 2026 Trackmade</span>
  <nav>
    <a href="{nav['support']}">{labels['support']}</a>
    <a href="{nav['privacy']}">{labels['privacy']}</a>
    <a href="{nav['imprint']}">{labels['imprint']}</a>
  </nav>
</div></footer>
</body>
</html>
"""

def write(rel, html):
    p = os.path.join(ROOT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(html); print("✓", rel)

# ---------- Startseite ----------
HOME_DE = """<main class="wrap">
<section class="hero">
  <img class="icon" src="img/icon.png" alt="Trackmade-Icon">
  <h1>Track, was dir wichtig ist.<br>Genau so, wie du willst.</h1>
  <p>Wasser, Training, Gewohnheiten, Abos, To-dos, Essensplan – oder dein ganz eigenes Modul. Deine Widgets ergeben zusammen ein Bild von deinem Alltag.</p>
  <span class="badge soon">Bald im App Store</span>
  <p class="platform"> Nur für iPhone · iOS 27 oder neuer</p>
</section>
<section class="screen"><img src="img/screen-home.png" alt="Trackmade Startseite mit Widgets"></section>
<section class="features">
  <div class="feature"><b><span class="dot"></span>Alles anpassbar</b><span>Fertige Vorlagen oder eigene Module aus Bausteinen. Du entscheidest, was du trackst.</span></div>
  <div class="feature"><b><span class="dot"></span>Widgets überall</b><span>In der App und auf dem Home-Bildschirm, mit Knöpfen zum direkten Eintragen.</span></div>
  <div class="feature"><b><span class="dot"></span>Deine Daten bleiben deine</b><span>Kein Konto, kein Server, keine Werbung. Alles bleibt auf deinem iPhone und, wenn du willst, in deiner iCloud.</span></div>
  <div class="feature"><b><span class="dot"></span>Einmal kaufen</b><span>Kostenlos starten. Premium einmalig, ohne Abo, mit 7 Tagen gratis zum Testen.</span></div>
</section>
</main>"""
HOME_EN = HOME_DE.replace('img/', '../img/').replace('screen-home.png', 'screen-home-en.png') \
  .replace("Track, was dir wichtig ist.<br>Genau so, wie du willst.", "Track what matters to you.<br>Exactly your way.") \
  .replace("Wasser, Training, Gewohnheiten, Abos, To-dos, Essensplan – oder dein ganz eigenes Modul. Deine Widgets ergeben zusammen ein Bild von deinem Alltag.",
           "Water, workouts, habits, subscriptions, to-dos, meal plans – or a module that’s all your own. Together, your widgets form a picture of your day.") \
  .replace("Bald im App Store", "Coming soon to the App Store").replace("Nur für iPhone · iOS 27 oder neuer", "iPhone only · iOS 27 or later").replace("Trackmade-Icon", "Trackmade icon") \
  .replace("Trackmade Startseite mit Widgets", "Trackmade home screen with widgets") \
  .replace("Alles anpassbar", "Fully customizable") \
  .replace("Fertige Vorlagen oder eigene Module aus Bausteinen. Du entscheidest, was du trackst.", "Ready-made templates or your own modules built from blocks. You decide what to track.") \
  .replace("Widgets überall", "Widgets everywhere") \
  .replace("In der App und auf dem Home-Bildschirm, mit Knöpfen zum direkten Eintragen.", "In the app and on your Home Screen, with buttons to log right away.") \
  .replace("Deine Daten bleiben deine", "Your data stays yours") \
  .replace("Kein Konto, kein Server, keine Werbung. Alles bleibt auf deinem iPhone und, wenn du willst, in deiner iCloud.", "No account, no server, no ads. Everything stays on your iPhone and, if you like, in your iCloud.") \
  .replace("Einmal kaufen", "Buy once") \
  .replace("Kostenlos starten. Premium einmalig, ohne Abo, mit 7 Tagen gratis zum Testen.", "Start for free. Premium is a one-time purchase, no subscription, with a 7-day free trial.")

# ---------- Datenschutz ----------
PRIV_DE = f"""<main class="wrap doc">
<h1>Datenschutzerklärung</h1>
<p class="stand">{STAND_DE}</p>

<div class="box">
<p><b>Kurz gesagt:</b> Trackmade hat kein Konto, keinen eigenen Server, keine Werbung und kein Tracking. Was du in der App einträgst, bleibt auf deinem iPhone – und, wenn du es einschaltest, in deiner eigenen iCloud. Wir sehen deine Daten nicht.</p>
</div>

<h2>1. Verantwortlicher</h2>
<p>{NAME}<br>{STREET}<br>{CITY}<br>{COUNTRY_DE}<br>E-Mail: <a href="mailto:{MAIL}">{MAIL}</a></p>

<h2>2. Daten in der App</h2>
<p>Module, Einträge, Fotos, Regeln, Vorlagen und Einstellungen speichert Trackmade ausschließlich lokal auf deinem Gerät. Damit die Widgets auf dem Home-Bildschirm dieselben Daten anzeigen, liegen sie in einem gemeinsamen Speicherbereich von App und Widget auf deinem iPhone. Trackmade baut keine Verbindung zu eigenen Servern auf und überträgt keine Inhalte an uns oder an Dritte.</p>

<h2>3. iCloud-Sicherung (freiwillig)</h2>
<p>Wenn du die iCloud-Sicherung einschaltest, legt Trackmade einmal am Tag eine Kopie deiner Daten in deinem eigenen iCloud Drive ab (Ordner „Trackmade“). Die Speicherung erfolgt bei Apple unter deinem Apple Account; wir haben darauf keinen Zugriff. Für die Verarbeitung durch Apple gilt die <a href="https://www.apple.com/legal/privacy/">Datenschutzrichtlinie von Apple</a>. Du kannst die Sicherung jederzeit in der App ausschalten und die Sicherungen in der Dateien-App löschen. Rechtsgrundlage: Art. 6 Abs. 1 lit. b DSGVO (von dir gewünschte Funktion).</p>

<h2>4. Apple Health</h2>
<p>Mit deiner Erlaubnis liest Trackmade folgende Werte aus Apple Health:</p>
<ul>
<li>für das Modul „Schritte &amp; Bewegung“: Schritte, Strecke, Stockwerke, aktive Kalorien und Trainingsminuten,</li>
<li>für das Modul „Körpergewicht“: dein Körpergewicht, zum Beispiel von einer mit Apple Health verbundenen Waage. Das Gewicht wird außerdem genutzt, um ohne Apple Watch die Kalorien beim Gehen zu schätzen.</li>
</ul>
<p>Trackmade schreibt nichts in Apple Health. Die Gesundheitsdaten werden nur auf deinem Gerät angezeigt, nicht weitergegeben und nicht für Werbung genutzt. Damit die Widgets auf dem Home-Bildschirm auch bei gesperrtem iPhone etwas anzeigen können, legt Trackmade die zuletzt gelesenen Werte zusätzlich in seinem eigenen Speicher auf deinem Gerät ab. Diese Kopie kommt nicht in die iCloud-Sicherung von Trackmade. Gewichte, die du selbst in Trackmade einträgst, sind normale Einträge wie in jedem anderen Modul (siehe Punkt 2). Du kannst den Zugriff jederzeit in den iPhone-Einstellungen unter „Health“ widerrufen. Rechtsgrundlage: deine Einwilligung (Art. 6 Abs. 1 lit. a und Art. 9 Abs. 2 lit. a DSGVO).</p>

<h2>5. Kamera und Fotos</h2>
<p>Für Foto-Felder kannst du mit deiner Erlaubnis Fotos aufnehmen oder aus deiner Mediathek wählen. Die Fotos werden nur in Trackmade auf deinem Gerät gespeichert (und, falls eingeschaltet, in deiner iCloud-Sicherung).</p>

<h2>6. Mitteilungen</h2>
<p>Erinnerungen, zum Beispiel vor Abo-Abbuchungen oder für Aufgaben, plant Trackmade direkt auf deinem iPhone. Dafür werden keine Daten an uns oder an Dritte gesendet. Du kannst Mitteilungen jederzeit in den iPhone-Einstellungen ausschalten.</p>

<h2>7. Käufe</h2>
<p>Trackmade Premium und die Testphase kaufst du über den App Store. Die Zahlung wickelt ausschließlich Apple ab; wir erhalten keine Zahlungs- oder Kontodaten. Die App fragt bei Apple nur ab, ob ein Kauf vorliegt. Es gilt die <a href="https://www.apple.com/legal/privacy/">Datenschutzrichtlinie von Apple</a>.</p>

<h2>8. Keine Analyse, keine Werbung</h2>
<p>Trackmade enthält keine Werbung, keine Analyse- oder Tracking-Werkzeuge und keine Software von Drittanbietern, die Daten über dich sammelt.</p>

<h2>9. Absturzberichte und TestFlight</h2>
<p>Wenn du in deinen iPhone-Einstellungen das Teilen von Analysedaten mit App-Entwicklern erlaubst, stellt Apple uns anonymisierte Absturzberichte zur Verfügung. Wenn du Trackmade über TestFlight testest, erhalten wir von Apple außerdem dein freiwilliges Feedback (mit Screenshots) sowie Absturzberichte und den Namen und die E-Mail-Adresse, mit der du eingeladen wurdest. Wir nutzen diese Angaben nur, um Fehler zu beheben und die App zu verbessern. Rechtsgrundlage: Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an einer fehlerfreien App).</p>

<h2>10. Diese Website</h2>
<p>trackmade.de wird über GitHub Pages bereitgestellt (GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA). Beim Aufruf verarbeitet GitHub technisch notwendige Daten wie deine IP-Adresse, Datum und Uhrzeit sowie den Browser, um die Seite auszuliefern und vor Missbrauch zu schützen. GitHub ist unter dem EU-US Data Privacy Framework zertifiziert. Die Website setzt keine Cookies und verwendet keine Analyse-Werkzeuge. Rechtsgrundlage: Art. 6 Abs. 1 lit. f DSGVO. Mehr dazu in der <a href="https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement">Datenschutzerklärung von GitHub</a>.</p>

<h2>11. Kontakt per E-Mail</h2>
<p>Wenn du uns schreibst, verwenden wir deine E-Mail-Adresse und deine Nachricht nur, um dein Anliegen zu bearbeiten, und löschen sie, wenn sie dafür nicht mehr gebraucht werden. Rechtsgrundlage: Art. 6 Abs. 1 lit. b bzw. f DSGVO.</p>

<h2>12. Deine Daten löschen</h2>
<p>Alle Daten in der App löschst du, indem du Trackmade von deinem iPhone löschst. Sicherungen in iCloud löschst du in der Dateien-App unter iCloud Drive → Trackmade.</p>

<h2>13. Deine Rechte</h2>
<p>Du hast das Recht auf Auskunft, Berichtigung, Löschung und Einschränkung der Verarbeitung, auf Datenübertragbarkeit, auf Widerspruch gegen Verarbeitungen auf Grundlage berechtigter Interessen sowie das Recht, eine Einwilligung jederzeit für die Zukunft zu widerrufen. Da wir deine App-Daten nicht erhalten, betrifft das vor allem E-Mails und Angaben aus TestFlight. Du kannst dich außerdem bei einer Datenschutz-Aufsichtsbehörde beschweren, zum Beispiel beim Bayerischen Landesamt für Datenschutzaufsicht (BayLDA), Promenade 18, 91522 Ansbach.</p>

<h2>14. Änderungen</h2>
<p>Wenn sich die App oder die Rechtslage ändert, passen wir diese Datenschutzerklärung an. Es gilt die jeweils hier veröffentlichte Fassung.</p>
</main>"""

PRIV_EN = f"""<main class="wrap doc">
<h1>Privacy Policy</h1>
<p class="stand">{STAND_EN}</p>

<div class="box">
<p><b>In short:</b> Trackmade has no account, no server of its own, no ads and no tracking. What you enter in the app stays on your iPhone – and, if you turn it on, in your own iCloud. We never see your data.</p>
</div>

<h2>1. Controller</h2>
<p>{NAME}<br>{STREET}<br>{CITY}<br>{COUNTRY_EN}<br>Email: <a href="mailto:{MAIL}">{MAIL}</a></p>

<h2>2. Data in the app</h2>
<p>Trackmade stores modules, entries, photos, rules, templates and settings only locally on your device. So that the Home Screen widgets can show the same data, it lives in a storage area shared by the app and its widget on your iPhone. Trackmade does not connect to any server of ours and does not send any content to us or to third parties.</p>

<h2>3. iCloud backup (optional)</h2>
<p>If you turn on iCloud backup, Trackmade saves a copy of your data to your own iCloud Drive once a day (folder “Trackmade”). It is stored by Apple under your Apple Account; we have no access to it. <a href="https://www.apple.com/legal/privacy/">Apple’s Privacy Policy</a> applies. You can turn the backup off in the app at any time and delete backups in the Files app. Legal basis: Art. 6(1)(b) GDPR (a feature you requested).</p>

<h2>4. Apple Health</h2>
<p>With your permission, Trackmade reads the following from Apple Health:</p>
<ul>
<li>for the “Steps &amp; Activity” module: steps, distance, floors, active calories and exercise minutes,</li>
<li>for the “Body Weight” module: your body weight, for example from a scale connected to Apple Health. Your weight is also used to estimate walking calories if you don’t have an Apple Watch.</li>
</ul>
<p>Trackmade never writes to Apple Health. Health data is only displayed on your device; it is not shared or used for advertising. So that Home Screen widgets can show something while your iPhone is locked, Trackmade also keeps the most recently read values in its own storage on your device. This copy is not included in Trackmade’s iCloud backup. Weights you enter yourself in Trackmade are regular entries like in any other module (see section 2). You can revoke access at any time in your iPhone settings under “Health”. Legal basis: your consent (Art. 6(1)(a) and Art. 9(2)(a) GDPR).</p>

<h2>5. Camera and photos</h2>
<p>For photo fields, you can take photos or pick them from your library with your permission. Photos are stored only within Trackmade on your device (and in your iCloud backup, if enabled).</p>

<h2>6. Notifications</h2>
<p>Reminders, for example before subscription charges or for tasks, are scheduled directly on your iPhone. No data is sent to us or to third parties. You can turn notifications off at any time in your iPhone settings.</p>

<h2>7. Purchases</h2>
<p>You buy Trackmade Premium and the free trial through the App Store. Payment is handled entirely by Apple; we receive no payment or account details. The app only asks Apple whether a purchase exists. <a href="https://www.apple.com/legal/privacy/">Apple’s Privacy Policy</a> applies.</p>

<h2>8. No analytics, no ads</h2>
<p>Trackmade contains no ads, no analytics or tracking tools and no third-party software that collects data about you.</p>

<h2>9. Crash reports and TestFlight</h2>
<p>If you allow sharing analytics with app developers in your iPhone settings, Apple provides us with anonymized crash reports. If you test Trackmade via TestFlight, Apple also provides us with your voluntary feedback (including screenshots), crash reports, and the name and email address you were invited with. We use this information only to fix bugs and improve the app. Legal basis: Art. 6(1)(f) GDPR (legitimate interest in a bug-free app).</p>

<h2>10. This website</h2>
<p>trackmade.de is hosted on GitHub Pages (GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA). When you visit, GitHub processes technically necessary data such as your IP address, date and time, and browser in order to deliver the site and protect it from abuse. GitHub is certified under the EU-US Data Privacy Framework. This website sets no cookies and uses no analytics. Legal basis: Art. 6(1)(f) GDPR. See <a href="https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement">GitHub’s Privacy Statement</a>.</p>

<h2>11. Contact by email</h2>
<p>If you email us, we use your email address and message only to handle your request and delete them once they are no longer needed. Legal basis: Art. 6(1)(b) or (f) GDPR.</p>

<h2>12. Deleting your data</h2>
<p>To delete all data in the app, delete Trackmade from your iPhone. To delete iCloud backups, use the Files app under iCloud Drive → Trackmade.</p>

<h2>13. Your rights</h2>
<p>You have the right of access, rectification, erasure, restriction of processing, data portability, to object to processing based on legitimate interests, and to withdraw consent at any time with effect for the future. Since we do not receive your app data, this mainly concerns emails and TestFlight information. You also have the right to lodge a complaint with a data protection supervisory authority, for example the Bavarian Data Protection Authority (BayLDA), Promenade 18, 91522 Ansbach, Germany.</p>

<h2>14. Changes</h2>
<p>If the app or the law changes, we will update this privacy policy. The version published here applies.</p>
</main>"""

# ---------- Impressum ----------
IMP_DE = f"""<main class="wrap doc">
<h1>Impressum</h1>
<h2>Angaben gemäß § 5 DDG</h2>
<p>{NAME}<br>{STREET}<br>{CITY}<br>{COUNTRY_DE}</p>
<h2>Kontakt</h2>
<p>E-Mail: <a href="mailto:{MAIL}">{MAIL}</a></p>
<h2>Verbraucherstreitbeilegung</h2>
<p>Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
</main>"""
IMP_EN = f"""<main class="wrap doc">
<h1>Legal Notice</h1>
<h2>Information according to § 5 DDG (German Digital Services Act)</h2>
<p>{NAME}<br>{STREET}<br>{CITY}<br>{COUNTRY_EN}</p>
<h2>Contact</h2>
<p>Email: <a href="mailto:{MAIL}">{MAIL}</a></p>
<h2>Consumer dispute resolution</h2>
<p>We are neither willing nor obliged to participate in dispute resolution proceedings before a consumer arbitration board.</p>
</main>"""

# ---------- Support ----------
def faq(items): return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items)
SUP_DE = f"""<main class="wrap doc faq">
<h1>Support</h1>
<p>Fragen, Fehler oder Wünsche? Schreib uns: <a href="mailto:{MAIL}"><b>{MAIL}</b></a>. Wir antworten so schnell wie möglich.</p>
<h2>Häufige Fragen</h2>
{faq([
 ("Wie bekomme ich Trackmade Premium?", "In der App unter Gestaltung → Trackmade Premium. Du kannst 7 Tage kostenlos testen und Premium danach einmalig kaufen – ohne Abo."),
 ("Ich habe Premium gekauft, es wird aber nicht angezeigt.", "Öffne die Kaufseite und tippe auf „Käufe wiederherstellen“. Achte darauf, mit derselben Apple-ID angemeldet zu sein, mit der du gekauft hast."),
 ("Wie sichere ich meine Daten?", "Schalte in der App die iCloud-Sicherung ein (Menü „…“ → iCloud-Sicherung). Trackmade sichert dann einmal am Tag in deine iCloud. Auf einem neuen iPhone bietet Trackmade beim ersten Start an, die Sicherung zu laden."),
 ("Wie lege ich ein Widget auf den Home-Bildschirm?", "Home-Bildschirm lange drücken → „+“ → Trackmade → Größe wählen. Danach lange auf das Widget drücken → „Widget bearbeiten“ → Modul auswählen."),
 ("Wie stelle ich die Sprache um?", "Trackmade folgt der Sprache deines iPhones. Nur für Trackmade änderst du sie unter Einstellungen → Apps → Trackmade → Sprache."),
 ("Wie lösche ich meine Daten?", "Lösch die App von deinem iPhone. iCloud-Sicherungen löschst du in der Dateien-App unter iCloud Drive → Trackmade."),
])}
<p style="margin-top:28px"><a href="datenschutz.html">Datenschutzerklärung</a> · <a href="impressum.html">Impressum</a></p>
</main>"""
SUP_EN = f"""<main class="wrap doc faq">
<h1>Support</h1>
<p>Questions, bugs or ideas? Email us: <a href="mailto:{MAIL}"><b>{MAIL}</b></a>. We’ll get back to you as soon as we can.</p>
<h2>FAQ</h2>
{faq([
 ("How do I get Trackmade Premium?", "In the app under Appearance → Trackmade Premium. Try it free for 7 days, then buy Premium once – no subscription."),
 ("I bought Premium but it isn’t showing.", "Open the purchase screen and tap “Restore Purchases”. Make sure you’re signed in with the same Apple Account you used to buy."),
 ("How do I back up my data?", "Turn on iCloud backup in the app (menu “…” → iCloud Backup). Trackmade then backs up to your iCloud once a day. On a new iPhone, Trackmade offers to load the backup on first launch."),
 ("How do I add a widget to my Home Screen?", "Touch and hold your Home Screen → “+” → Trackmade → choose a size. Then touch and hold the widget → “Edit Widget” → choose a module."),
 ("How do I change the language?", "Trackmade follows your iPhone’s language. To change it for Trackmade only, go to Settings → Apps → Trackmade → Language."),
 ("How do I delete my data?", "Delete the app from your iPhone. To delete iCloud backups, use the Files app under iCloud Drive → Trackmade."),
])}
<p style="margin-top:28px"><a href="privacy.html">Privacy Policy</a> · <a href="imprint.html">Legal Notice</a></p>
</main>"""

write("index.html", page("de", "Trackmade – deine eigene Tracking-App", HOME_DE, "index.html", ""))
write("en/index.html", page("en", "Trackmade – your own tracking app", HOME_EN, "en/index.html", ""))
write("datenschutz.html", page("de", "Datenschutz – Trackmade", PRIV_DE, "datenschutz.html", "privacy.html"))
write("en/privacy.html", page("en", "Privacy Policy – Trackmade", PRIV_EN, "en/privacy.html", "datenschutz.html"))
write("impressum.html", page("de", "Impressum – Trackmade", IMP_DE, "impressum.html", "imprint.html"))
write("en/imprint.html", page("en", "Legal Notice – Trackmade", IMP_EN, "en/imprint.html", "impressum.html"))
write("support.html", page("de", "Support – Trackmade", SUP_DE, "support.html", "support.html"))
write("en/support.html", page("en", "Support – Trackmade", SUP_EN, "en/support.html", "support.html"))
open(os.path.join(ROOT, "CNAME"), "w").write("trackmade.de\n")
