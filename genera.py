# Genera il sito di Liquid DE: una pagina, due lingue (it/en), immagini in img/.
import html, pathlib

OUT = pathlib.Path(__file__).parent / "www"

# Ogni sezione: id, titolo it/en, immagini [(file, didascalia it, en)], testo it/en,
# dettagli tecnici it/en (lista).
SEZIONI = [
 ("intro-scrivania", "La scrivania", "The desktop",
  [("scrivania", "La scrivania vuota: in basso la dock, in alto l'Isola nascosta.", "The empty desktop: dock at the bottom, the Island hidden at the top.")],
  "Liquid DE parte da un'idea sola: una scrivania elastica, quasi liquida. Il testo resta fermo e nitido, si muove la forma. Niente pannelli fissi che rubano spazio: la barra (l'Isola) sta nascosta oltre il bordo alto e scende quando la chiami, la dock in basso si fa da parte quando una finestra le passa sopra, e tutto il resto esce dai bordi e dagli angoli dello schermo — la «Riva».",
  "Liquid DE is built around one idea: an elastic, almost liquid desktop. Text stays still and sharp, shapes move. No fixed panels eating space: the bar (the Island) hides past the top edge and comes down when called, the dock at the bottom steps aside when a window moves over it, and everything else comes out of the screen edges and corners — the «Shore».",
  [("Tre programmi, due canali dichiarati: compositore (C), demone (Dart), interfaccia (QML su Quickshell).", "Three programs, two declared channels: compositor (C), daemon (Dart), interface (QML on Quickshell)."),
   ("Superfici della shell su wlr-layer-shell, con namespace propri (liquid-isola, liquid-stanze, liquid-cassetto…).", "Shell surfaces use wlr-layer-shell with their own namespaces (liquid-isola, liquid-stanze, liquid-cassetto…).")]),
 ("isola", "L'Isola", "The Island",
  [("isola", "L'Isola scende portando il puntatore sul bordo alto.", "The Island comes down when the pointer rests on the top edge."),
   ("oggi", "Toccando il tempo: la giornata, ora per ora, e i prossimi giorni.", "Tapping the weather: the day hour by hour and the coming days."),
   ("calendario", "Toccando l'ora o la data: il calendario, con il tempo previsto sui giorni.", "Tapping the time or date: the calendar, with the forecast on its days.")],
  "Una capsula che galleggia in mezzo: ora, data, tempo, musica che suona, programmi del vassoio, segni di stato e la campanella. Ogni voce apre la sua faccia della stessa carta: l'ora porta al calendario, il sole al meteo, la campanella alle notifiche. Si trascina in alto o in basso, e con «a scomparsa» restituisce alle finestre tutto lo schermo.",
  "A capsule floating in the middle: time, date, weather, what is playing, tray apps, status icons and the bell. Each item opens its own face of the same card: the time leads to the calendar, the sun to the weather, the bell to notifications. It can be dragged to the top or bottom, and in auto-hide mode it gives the whole screen back to windows.",
  [("Il compositore sente la sosta sul bordo (3 px, 160 ms) e annuncia `evento bordo {\"quale\":\"alto\"}`: nessuna superficie invisibile resta sopra le finestre.", "The compositor detects the dwell on the edge (3 px, 160 ms) and announces `evento bordo {\"quale\":\"alto\"}`: no invisible surface is left over windows."),
   ("Sopra una finestra a schermo intero la sosta è di 500 ms (o subito con Super), per non disturbare giochi e film.", "Over a fullscreen window the dwell is 500 ms (or immediate with Super), so games and films are not disturbed."),
   ("Meteo da Open-Meteo, chiesto dal demone e tenuto in cache.", "Weather from Open-Meteo, fetched by the daemon and cached.")]),
 ("notifiche", "Notifiche", "Notifications",
  [("notifica", "Una notifica arriva e prende per un attimo il posto dell'Isola.", "A notification arrives and briefly takes the Island's place."),
   ("notifiche", "La campanella: la storia delle notifiche, «Svuota» e «Giornata».", "The bell: notification history, «Clear» and «Day».")],
  "Le notifiche non coprono il lavoro con riquadri: passano dentro l'Isola, si leggono e se ne vanno. La storia resta nella campanella. «Non disturbare» le tiene zitte, e sulla schermata di blocco si sceglie quanto mostrare (solo quante, tutto, niente).",
  "Notifications do not cover your work with boxes: they pass through the Island, get read and leave. History stays behind the bell. «Do not disturb» silences them, and on the lock screen you choose how much to show (count only, everything, nothing).",
  [("Server org.freedesktop.Notifications di Quickshell, azioni e urgenza rispettate; urgente = 10 s in vista.", "Quickshell's org.freedesktop.Notifications server, actions and urgency honoured; urgent = 10 s on screen.")]),
 ("centro", "Centro di controllo", "Control centre",
  [("centro", "Wi-Fi, Bluetooth, luce notturna, non disturbare, risparmio, modo gioco, volume e spegnimento.", "Wi-Fi, Bluetooth, night light, do not disturb, power saving, game mode, volume and power.")],
  "Si apre dall'angolo in alto a destra o con Super+A. Spegni, Riavvia ed Esci si tengono premuti finché il pulsante non si riempie: un clic per sbaglio non spegne niente.",
  "Opens from the top-right corner or with Super+A. Power off, Restart and Log out must be held until the button fills: a stray click turns nothing off.",
  [("Stato di rete e radio da NetworkManager e rfkill, audio da PipeWire, luminosità da brightnessctl.", "Network and radio state from NetworkManager and rfkill, audio from PipeWire, brightness from brightnessctl.")]),
 ("menu", "Il menù delle app", "The app menu",
  [("menu-cerca", "Si tocca Super e si scrive: la ricerca trova le app anche per funzione.", "Tap Super and type: search finds apps by what they do, too.")],
  "Il «Sottomarino» emerge dall'angolo in basso a sinistra o toccando Super. Si scrive subito: «navigare il web» trova i browser, «foto» trova i visualizzatori. Categorie, «Cosa vuoi fare», le più usate e l'elenco dalla A alla Z.",
  "The «Submarine» surfaces from the bottom-left corner or by tapping Super. Just type: «browse the web» finds browsers, «photos» finds viewers. Categories, «What do you want to do», most used and the A–Z list.",
  [("App lette dai file .desktop in XDG_DATA_DIRS (anche Flatpak), sinonimi italiani, frequenza e ora d'uso tenute dal demone.", "Apps read from .desktop files in XDG_DATA_DIRS (Flatpak too), Italian synonyms, usage frequency and time kept by the daemon.")]),
 ("dock", "La dock", "The dock",
  [("dock", "Icone che crescono verso il puntatore; il trattino sotto dice che l'app è aperta.", "Icons grow towards the pointer; the dash below says the app is open."),
   ("menu-scrivania", "Il menù della scrivania (clic destro): app, terminale, file, sfondo, blocco.", "The desktop menu (right click): apps, terminal, files, wallpaper, lock.")],
  "Una fila di icone che si ingrandiscono al passaggio. Un'app è un'icona, anche con più finestre: il clic porta davanti, con più finestre gira fra loro. Il menù di un'icona apre una nuova finestra, la toglie o la fissa, e elenca le finestre una per una. Si trascina per riordinare.",
  "A row of icons that grow as you pass over them. One app is one icon, even with several windows: a click brings it forward, with several windows it cycles through them. An icon's menu opens a new window, pins or unpins it, and lists windows one by one. Drag to reorder.",
  [("Ingrandimento con una sola molla per tutta la fila: le icone si muovono insieme invece di rincorrersi.", "Magnification driven by a single spring for the whole row: icons move together instead of chasing each other."),
   ("Modo «elude»: si sposta quando una finestra le passa sopra, senza riservare spazio.", "«Evade» mode: it moves away when a window passes over it, without reserving space.")]),
 ("stanze", "Le stanze", "Rooms",
  [("stanze", "Le stanze aperte (Super+Tab o spinta sul bordo): ogni stanza con le icone delle sue finestre.", "Rooms open (Super+Tab or edge push): each room with the icons of its windows.")],
  "Gli spazi di lavoro si chiamano stanze. Si aprono spingendo il puntatore contro il bordo di lato o con Super+Tab; si cambia stanza con Super+1…0, Super+Ctrl+frecce o la rotellina con Super. Cambiando stanza da tastiera, la colonna sbuca un attimo per dire dove si è arrivati. Stanze e Appunti si scambiano di lato trascinandone uno verso l'altro bordo.",
  "Workspaces are called rooms. They open by pushing the pointer against a side edge or with Super+Tab; switch rooms with Super+1…0, Super+Ctrl+arrows or Super+scroll. When switching from the keyboard, the column peeks out for a moment to show where you landed. Rooms and Clipboard swap sides by dragging one towards the other edge.",
  [("Il bordo di lato si apre con una SPINTA (90 px di movimento oltre il bordo), non con una sosta: fermarsi lì per la barra di scorrimento non apre niente.", "A side edge opens with a PUSH (90 px of movement past the edge), not a dwell: resting there to reach a scrollbar opens nothing."),
   ("Dieci stanze nel compositore; le finestre X11 nascoste non contano come occupanti.", "Ten rooms in the compositor; hidden X11 windows do not count as occupants.")]),
 ("appunti", "Gli appunti", "Clipboard",
  [("appunti", "Il Cassetto: testo e immagini copiati, con ricerca.", "The Drawer: copied text and images, with search.")],
  "Il Cassetto ricorda quello che copi, anche le immagini. Si apre con Super+V o spingendo sul suo bordo; un tocco rimette una voce negli appunti, Canc la toglie, «Svuota» chiede conferma.",
  "The Drawer remembers what you copy, images too. Open it with Super+V or by pushing its edge; a tap puts an item back on the clipboard, Delete removes it, «Clear» asks for confirmation.",
  [("Cronologia da cliphist (wl-paste --watch), anteprime delle immagini in una cartella di runtime.", "History from cliphist (wl-paste --watch), image previews in a runtime folder.")]),
 ("tasti", "Tenere premuto Super", "Holding Super",
  [("tasti", "Tenendo Super i tasti compaiono sulla scrivania, dove stanno le cose che aprono.", "Holding Super shows the keys on the desktop, where the things they open live."),
   ("scorciatoie", "Super+K: tutte le scorciatoie, con la ricerca.", "Super+K: every shortcut, searchable.")],
  "Toccato, Super apre il menù; tenuto premuto, fa comparire sulla scrivania i tasti principali, ognuno nel posto dove esce la cosa che apre. Super+K mostra l'elenco completo. Le scorciatoie seguono quelle di Windows 11: Super+E, D, L, V, I, A, N, Maiusc+S.",
  "Tapped, Super opens the menu; held, it shows the main keys on the desktop, each where its target appears. Super+K shows the full list. Shortcuts follow Windows 11: Super+E, D, L, V, I, A, N, Shift+S.",
  [("Scorciatoie in un file di testo (config/scorciatoie.minerva) letto dal compositore: tocco, tieni, ripeti, anche a schermo bloccato.", "Shortcuts live in a text file (config/scorciatoie.minerva) read by the compositor: tap, hold, repeat, even when locked.")]),
 ("finestre", "Le finestre", "Windows",
  [("imp-finestre", "Impostazioni › Finestre: barra del titolo, colore intorno alla finestra attiva, materiale, elasticità.", "Settings › Windows: title bar, colour around the active window, material, elasticity.")],
  "La barra del titolo la disegna il compositore, con riduci, ingrandisci, schermo intero e chiudi. Trascinando una finestra contro un bordo occupa metà schermo, negli angoli un quarto. Materiali: vetro (sfocatura) o acquerello; cornice animata intorno alla finestra attiva; «mercurio» che fonde le finestre vicine; elastico che fa ondeggiare la finestra mentre la sposti.",
  "The compositor draws the title bar, with minimise, maximise, fullscreen and close. Dragging a window against an edge fills half the screen, into a corner a quarter. Materials: glass (blur) or watercolour; an animated frame around the active window; «mercury» merging nearby windows; elasticity that makes the window wobble while you move it.",
  [("Chi chiede la barra con xdg-decoration (Chrome con «barra di sistema», Qt) la ottiene; chi se la disegna (Firefox, GTK) resta senza la nostra.", "Apps that request the bar via xdg-decoration (Chrome with «system title bar», Qt) get it; apps drawing their own (Firefox, GTK) do not get ours."),
   ("Nuove finestre al centro dello spazio utile, a cascata se il posto è preso.", "New windows centred in the usable area, cascaded if the spot is taken."),
   ("XWayland pigro: parte al primo programma X11 (Steam, Wine) e si ferma quando non serve.", "Lazy XWayland: starts with the first X11 program (Steam, Wine) and stops when not needed.")]),
 ("file", "File", "Files",
  [("file", "Il gestore file: colonna dei posti, schede, viste, dischi.", "The file manager: places column, tabs, views, drives.")],
  "Due riquadri affiancati, schede, nuova finestra vera. Copia, taglia e incolla con i trasferimenti che si mettono in pausa; cestino con ripristino; comprimi ed estrai (zip, 7z, rar, iso, tar); proprietà con permessi a caselle; dischi da montare, espellere e formattare; modalità amministratore con la finestra della password; trasmetti alla TV.",
  "Two side-by-side panes, tabs, a real new window. Copy, cut and paste with pausable transfers; trash with restore; compress and extract (zip, 7z, rar, iso, tar); properties with checkbox permissions; drives to mount, eject and format; administrator mode with the password window; cast to the TV.",
  [("È un processo a sé (filemanager.qml): un errore lì non spegne la barra.", "It is its own process (filemanager.qml): an error there cannot take the bar down."),
   ("Le operazioni sui file le fa il demone (fs_*), una sola coda di trasferimenti per tutte le finestre.", "File operations are done by the daemon (fs_*), one transfer queue for all windows.")]),
 ("editor", "Editor", "Editor",
  [("editor", "Editor di testo con schede, numeri di riga, trova e sostituisci.", "Text editor with tabs, line numbers, find and replace.")],
  "Un editor di testo semplice: schede, trova e sostituisci, vai alla riga, a capo, zoom, carattere a larghezza fissa. Il salvataggio è atomico, e i file di sistema si aprono e si salvano chiedendo la password.",
  "A simple text editor: tabs, find and replace, go to line, word wrap, zoom, monospace font. Saving is atomic, and system files open and save by asking for the password.",
  []),
 ("anteprima", "Anteprima", "Preview",
  [("anteprima", "Anteprima: un'immagine, e la sua cartella diventa l'album.", "Preview: one image, and its folder becomes the album.")],
  "Aprendo un'immagine, la cartella diventa l'album: zoom, adatta, dimensione reale, ruota, schermo intero, provino a contatto, dettagli. La Galleria ordina le foto per giorni e anni, con preferiti e doppioni.",
  "Opening an image turns its folder into the album: zoom, fit, actual size, rotate, fullscreen, contact sheet, details. The Gallery sorts photos by days and years, with favourites and duplicates.",
  [("Indice fotografico nel demone, miniature con ffmpegthumbnailer per i video.", "Photo index in the daemon, thumbnails via ffmpegthumbnailer for videos.")]),
 ("media", "Media", "Media",
  [("media", "Il lettore, con il visualizzatore dell'audio.", "The player, with the audio visualiser.")],
  "Lettore audio e video con playlist, ripeti e casuale, finestra picture-in-picture e visualizzatore. «Taglia» accorcia un file sulla sua forma d'onda; «Download» cerca e scarica.",
  "Audio and video player with playlist, repeat and shuffle, picture-in-picture and visualiser. «Trim» shortens a file on its waveform; «Download» searches and fetches.",
  [("Qt Multimedia con backend FFmpeg; taglio e forma d'onda con ffmpeg nel demone.", "Qt Multimedia with the FFmpeg backend; trimming and waveform via ffmpeg in the daemon.")]),
 ("calcolatrice", "Calcolatrice", "Calculator",
  [("calcolatrice", "Calcolatrice: parentesi, radice, potenza, percentuale e memoria.", "Calculator: parentheses, root, power, percent and memory.")],
  "Quattro operazioni, parentesi, √, x², π, percentuale, memoria. Si usa anche solo dalla tastiera.",
  "Four operations, parentheses, √, x², π, percent, memory. Works from the keyboard alone.",
  [("Analizzatore delle espressioni scritto apposta: niente eval.", "A purpose-written expression parser: no eval.")]),
 ("attivita", "Attività", "Activity",
  [("attivita", "Processore, memoria, rete, scambio e temperatura; le app con i nomi umani.", "CPU, memory, network, swap and temperature; apps with human names.")],
  "Il cruscotto del computer: grafici di processore, memoria, rete, scambio e temperatura. Le app aperte con il loro nome vero invece del nome del processo; «Chiudi» con gentilezza e, se non basta, «Termina». Si apre anche con Ctrl+Maiusc+Esc.",
  "The computer's dashboard: graphs for CPU, memory, network, swap and temperature. Open apps by their real name rather than their process name; «Close» politely and, if that is not enough, «Kill». Also opens with Ctrl+Shift+Esc.",
  []),
 ("custodia", "Custodia", "Custodia",
  [("custodia", "Custodia: un progetto, cosa c'è da salvare, quando.", "Custodia: a project, what needs saving, when.")],
  "La storia e la sicurezza delle tue cartelle, senza dover sapere cos'è git. «Salva» tiene ogni versione; «Punto di ritorno» fa una copia di tutto; «Torna a…» si può sempre annullare. Le destinazioni: una cartella, un disco esterno o GitHub, con l'accesso dal browser e la chiave nel portachiavi.",
  "The history and safety of your folders, without having to know what git is. «Save» keeps every version; «Restore point» copies everything; «Go back to…» can always be undone. Destinations: a folder, an external drive or GitHub, with browser sign-in and the key kept in the keyring.",
  [("Nessuna operazione che può perdere lavoro parte senza un punto di ritorno prima; se il punto non riesce, l'operazione non parte.", "No operation that could lose work runs without a restore point first; if the point fails, the operation does not run."),
   ("Firma dei salvataggi presa dall'account GitHub con l'indirizzo noreply; controllo dei segreti prima di ogni invio.", "Save signatures taken from the GitHub account with the noreply address; secret scanning before every push.")]),
 ("manutenzione", "Manutenzione", "Maintenance",
  [("manutenzione", "Cosa occupa spazio, e cosa si può togliere senza danni.", "What takes up space, and what can safely go.")],
  "Guarda cosa occupa posto sul computer, famiglia per famiglia, e dice per ognuna se torna da sola o no. Si pulisce solo quello che si vede e si spunta.",
  "Shows what takes space on the computer, family by family, and says for each whether it comes back on its own. Only what is shown and ticked gets cleaned.",
  []),
 ("impostazioni", "Impostazioni", "Settings",
  [("imp-aspetto", "Aspetto: stili pronti (Liquid, Minerva, Mac, Windows) e temi di colore.", "Appearance: ready styles (Liquid, Minerva, Mac, Windows) and colour themes."),
   ("imp-barra-dock", "Barra e dock: dove stanno, come si comportano, angoli e bordi.", "Bar and dock: where they sit, how they behave, corners and edges."),
   ("imp-schermo", "Schermo: risoluzione, frequenza, scala, rotazione.", "Display: resolution, refresh rate, scale, rotation."),
   ("imp-accessibilita", "Accessibilità: grandezza del testo, lente, puntatore.", "Accessibility: text size, magnifier, pointer.")],
  "Diciannove sezioni: aspetto, scrivania, finestre, barra e dock, schermo, notifiche, alimentazione, audio, rete, Bluetooth, tastiera e mouse, data e lingua, accessibilità, app predefinite, avvio, account online, utente, accesso e l'aiuto. Sotto ogni interruttore una riga spiega cosa fa. Le modifiche allo schermo tornano indietro da sole se non le confermi.",
  "Nineteen sections: appearance, desktop, windows, bar and dock, display, notifications, power, audio, network, Bluetooth, keyboard and mouse, date and language, accessibility, default apps, startup, online accounts, user, login and help. A line under every switch explains what it does. Display changes revert by themselves unless confirmed.",
  [("Tutte le impostazioni in un file JSON tenuto dal demone; ogni finestra le riceve con l'evento settings_changed.", "All settings live in one JSON file owned by the daemon; every window receives them via the settings_changed event.")]),
]

ARCH_IT = [
 ("Compositore — minerva-wayland", "C, circa 17.000 righe, su una copia privata di wlroots 0.20.2 compilata come libreria statica. Gli effetti (sfocatura, angoli, cornice, elastico, mercurio) stanno dentro la scena del fork. Renderer GLES2; XWayland; protocolli per i giochi (fifo-v1, commit-timing-v1, presentation-time); wlr-screencopy per le schermate."),
 ("Demone — minervad", "Dart compilato, circa 36.000 righe: impostazioni, file, rete, audio, Bluetooth, accesso, Custodia, meteo, foto, processi, terminale. Parla con la shell su un socket Unix in $XDG_RUNTIME_DIR: JSON, un messaggio per riga, con una parola d'ordine che il demone scrive per sé."),
 ("Interfaccia — minerva-shell", "QML su Quickshell, circa 82.000 righe: scrivania, barra, dock, pannelli, schermata di blocco e di accesso, e le app. Le app sono processi separati: un errore in una non spegne la barra."),
 ("Sessione e sicurezza", "Accesso con greetd; blocco con PAM (file /etc/pam.d/liquid-de); finestra della password nostra sopra polkit-agent-1; portali xdg-desktop-portal-wlr per condividere lo schermo; sessione di recupero con un solo terminale per riparare."),
]
ARCH_EN = [
 ("Compositor — minerva-wayland", "C, about 17,000 lines, on a private copy of wlroots 0.20.2 built as a static library. Effects (blur, corners, frame, elasticity, mercury) live inside the fork's scene graph. GLES2 renderer; XWayland; gaming protocols (fifo-v1, commit-timing-v1, presentation-time); wlr-screencopy for screenshots."),
 ("Daemon — minervad", "Compiled Dart, about 36,000 lines: settings, files, network, audio, Bluetooth, login, Custodia, weather, photos, processes, terminal. Talks to the shell over a Unix socket in $XDG_RUNTIME_DIR: JSON, one message per line, with a password the daemon writes for itself."),
 ("Interface — minerva-shell", "QML on Quickshell, about 82,000 lines: desktop, bar, dock, panels, lock and login screens, and the apps. Apps are separate processes: an error in one cannot take the bar down."),
 ("Session and security", "Login with greetd; lock with PAM (/etc/pam.d/liquid-de); our own password window on top of polkit-agent-1; xdg-desktop-portal-wlr portals for screen sharing; a recovery session with a single terminal for repairs."),
]

SCORCIATOIE = [
 ("Super", "Menù delle app", "App menu"), ("Super (tenuto)", "I tasti sulla scrivania", "Keys on the desktop"),
 ("Super+A", "Centro di controllo", "Control centre"), ("Super+O", "Oggi: tempo e calendario", "Today: weather and calendar"),
 ("Super+N", "Notifiche", "Notifications"), ("Super+V", "Appunti", "Clipboard"), ("Super+Tab", "Stanze", "Rooms"),
 ("Super+1…0", "Vai alla stanza", "Go to room"), ("Super+Maiusc+1…0", "Porta la finestra nella stanza", "Move window to room"),
 ("Super+E", "File", "Files"), ("Super+I", "Impostazioni", "Settings"), ("Super+Invio", "Terminale", "Terminal"),
 ("Super+D", "Scrivania libera", "Show desktop"), ("Super+L", "Blocca", "Lock"), ("Super+K", "Tutte le scorciatoie", "All shortcuts"),
 ("Super+←/→", "Metà sinistra / destra", "Left / right half"), ("Super+↑/↓", "Ingrandisci / torna com'era", "Maximise / restore"),
 ("Super+F", "Schermo intero", "Fullscreen"), ("Super+Q · Alt+F4", "Chiudi la finestra", "Close window"),
 ("Alt+Tab", "Le ultime finestre usate", "Recent windows"), ("Super+Maiusc+S · Stamp", "Schermata", "Screenshot"),
 ("Ctrl+Maiusc+Esc", "Attività", "Activity"), ("Super+Ctrl+R", "Risveglia l'interfaccia", "Wake the interface"),
]

def e(t): return html.escape(t)
def codice(t):
    # `x` → <code>x</code>
    parti = t.split("`"); out = []
    for i, p in enumerate(parti): out.append(f"<code>{e(p)}</code>" if i % 2 else e(p))
    return "".join(out)
def bi(it, en, tag="span", cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<{tag}{c} lang="it">{codice(it)}</{tag}><{tag}{c} lang="en">{codice(en)}</{tag}>'

nav = "".join(f'<a href="#{s[0]}">{bi(s[1], s[2])}</a>' for s in SEZIONI)
corpo = []
for sid, tit_it, tit_en, imgs, t_it, t_en, tec in SEZIONI:
    figure = "".join(
        f'<figure><a href="img/{f}.webp"><img src="img/{f}.webp" loading="lazy" alt="{e(ci)}"></a>'
        f'<figcaption>{bi(ci, ce)}</figcaption></figure>' for f, ci, ce in imgs)
    tecnica = ""
    if tec:
        voci = "".join(f"<li>{bi(a, b)}</li>" for a, b in tec)
        tecnica = (f'<details><summary>{bi("Dettagli tecnici", "Technical details")}</summary><ul>{voci}</ul></details>')
    corpo.append(f'<section id="{sid}"><h2>{bi(tit_it, tit_en)}</h2>{bi(t_it, t_en, "p")}'
                 f'<div class="figure">{figure}</div>{tecnica}</section>')

arch = "".join(f'<div class="card"><h3>{bi(a, c)}</h3>{bi(b, d, "p")}</div>'
               for (a, b), (c, d) in zip(ARCH_IT, ARCH_EN))
tasti = "".join(f"<tr><td><kbd>{e(k)}</kbd></td><td>{bi(i, n)}</td></tr>" for k, i, n in SCORCIATOIE)

SCHEMA = """<svg viewBox="0 0 760 300" role="img" aria-label="Architettura">
<defs><marker id="f" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="currentColor"/></marker></defs>
<g font-family="inherit" font-size="15" fill="currentColor">
<rect x="20" y="20" width="220" height="110" rx="14" class="b1"/><text x="130" y="60" text-anchor="middle" font-weight="700">minerva-shell</text><text x="130" y="84" text-anchor="middle" class="t2">QML · Quickshell</text><text x="130" y="106" text-anchor="middle" class="t2">scrivania · app</text>
<rect x="520" y="20" width="220" height="110" rx="14" class="b2"/><text x="630" y="60" text-anchor="middle" font-weight="700">minervad</text><text x="630" y="84" text-anchor="middle" class="t2">Dart</text><text x="630" y="106" text-anchor="middle" class="t2">sistema · file · rete</text>
<rect x="20" y="170" width="220" height="110" rx="14" class="b3"/><text x="130" y="210" text-anchor="middle" font-weight="700">minerva-wayland</text><text x="130" y="234" text-anchor="middle" class="t2">C · wlroots 0.20.2</text><text x="130" y="256" text-anchor="middle" class="t2">finestre · effetti</text>
<rect x="520" y="170" width="220" height="110" rx="14" class="b4"/><text x="630" y="210" text-anchor="middle" font-weight="700">Linux</text><text x="630" y="234" text-anchor="middle" class="t2">PipeWire · NetworkManager</text><text x="630" y="256" text-anchor="middle" class="t2">BlueZ · udisks · PAM</text>
<line x1="245" y1="75" x2="515" y2="75" stroke="currentColor" stroke-width="2" marker-start="url(#f)" marker-end="url(#f)"/><text x="380" y="66" text-anchor="middle" class="t2">socket Unix · JSON</text>
<line x1="130" y1="135" x2="130" y2="165" stroke="currentColor" stroke-width="2" marker-start="url(#f)" marker-end="url(#f)"/><text x="140" y="155" class="t2">canale di testo · layer-shell</text>
<line x1="630" y1="135" x2="630" y2="165" stroke="currentColor" stroke-width="2" marker-start="url(#f)" marker-end="url(#f)"/><text x="640" y="155" class="t2">D-Bus · processi</text>
</g></svg>"""

PAGINA = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Liquid DE</title>
<meta name="description" content="Liquid DE: un ambiente desktop per Linux su Wayland, elastico e quasi liquido.">
<link rel="icon" href="img/logo.png">
<style>
:root {{ --fondo:#070b12; --carta:#0f1622; --riga:#1f2a3a; --testo:#e7edf5; --tenue:#9aa8bb; --accento:#2fd3e6; --accento2:#8b7cf6; }}
:root[data-theme=light] {{ --fondo:#f4f6fa; --carta:#ffffff; --riga:#dde3ec; --testo:#0f1622; --tenue:#526074; --accento:#0b8fa3; --accento2:#6d5ae6; }}
@media (prefers-color-scheme: light) {{ :root:not([data-theme=dark]) {{ --fondo:#f4f6fa; --carta:#ffffff; --riga:#dde3ec; --testo:#0f1622; --tenue:#526074; --accento:#0b8fa3; --accento2:#6d5ae6; }} }}
* {{ box-sizing:border-box; }}
html {{ scroll-behavior:smooth; }}
body {{ margin:0; background:var(--fondo); color:var(--testo); font:17px/1.6 "Inter","Adwaita Sans",system-ui,sans-serif; }}
[lang=en] {{ display:none; }}
html[data-lang=en] [lang=it] {{ display:none; }} html[data-lang=en] [lang=en] {{ display:revert; }}
header {{ position:sticky; top:0; z-index:5; backdrop-filter:blur(14px); background:color-mix(in srgb,var(--fondo) 80%,transparent); border-bottom:1px solid var(--riga); }}
.barra {{ max-width:1180px; margin:auto; display:flex; gap:16px; align-items:center; padding:10px 16px; }}
.marchio {{ font-weight:800; letter-spacing:.02em; font-size:20px; white-space:nowrap; }}
.marchio b {{ color:var(--accento); }}
nav {{ display:flex; gap:4px; overflow-x:auto; flex:1; scrollbar-width:none; }}
nav a {{ color:var(--tenue); text-decoration:none; padding:6px 10px; border-radius:999px; font-size:14px; white-space:nowrap; }}
nav a:hover {{ background:var(--carta); color:var(--testo); }}
button {{ background:var(--carta); color:var(--testo); border:1px solid var(--riga); border-radius:999px; padding:6px 12px; font:inherit; font-size:14px; cursor:pointer; }}
main {{ max-width:1180px; margin:auto; padding:0 16px 80px; }}
.eroe {{ padding:72px 0 40px; }}
.eroe h1 {{ font-size:clamp(40px,7vw,76px); line-height:1.02; margin:0 0 18px; letter-spacing:-.02em; }}
.eroe h1 span.l {{ background:linear-gradient(90deg,var(--accento),var(--accento2)); -webkit-background-clip:text; background-clip:text; color:transparent; }}
.eroe p {{ font-size:20px; color:var(--tenue); max-width:760px; margin:0; }}
section {{ padding:48px 0; border-top:1px solid var(--riga); }}
h2 {{ font-size:30px; margin:0 0 12px; }}
section > p {{ max-width:820px; color:var(--testo); }}
.figure {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr)); gap:18px; margin-top:22px; }}
figure {{ margin:0; background:var(--carta); border:1px solid var(--riga); border-radius:16px; overflow:hidden; }}
figure img {{ display:block; width:100%; height:auto; }}
figcaption {{ padding:10px 14px; color:var(--tenue); font-size:15px; }}
details {{ margin-top:18px; background:var(--carta); border:1px solid var(--riga); border-radius:14px; padding:12px 16px; max-width:900px; }}
summary {{ cursor:pointer; font-weight:600; color:var(--accento); }}
details ul {{ margin:10px 0 0; padding-left:20px; color:var(--tenue); }}
code {{ font-family:"Noto Sans Mono",ui-monospace,monospace; font-size:.88em; background:color-mix(in srgb,var(--accento) 12%,transparent); padding:1px 5px; border-radius:6px; }}
.cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr)); gap:16px; margin-top:22px; }}
.card {{ background:var(--carta); border:1px solid var(--riga); border-radius:16px; padding:18px; }}
.card h3 {{ margin:0 0 6px; font-size:18px; }} .card p {{ margin:0; color:var(--tenue); font-size:15px; }}
.schema {{ color:var(--testo); margin-top:26px; max-width:860px; }}
.schema .b1 {{ fill:color-mix(in srgb,var(--accento) 16%,var(--carta)); stroke:var(--accento); }}
.schema .b2 {{ fill:color-mix(in srgb,var(--accento2) 16%,var(--carta)); stroke:var(--accento2); }}
.schema .b3,.schema .b4 {{ fill:var(--carta); stroke:var(--riga); }}
.schema .t2 {{ fill:var(--tenue); font-size:13px; }}
table {{ width:100%; max-width:820px; border-collapse:collapse; margin-top:18px; }}
td {{ padding:9px 10px; border-bottom:1px solid var(--riga); vertical-align:top; }}
kbd {{ font-family:"Noto Sans Mono",ui-monospace,monospace; font-size:14px; background:var(--carta); border:1px solid var(--riga); border-bottom-width:2px; border-radius:7px; padding:2px 8px; white-space:nowrap; }}
footer {{ border-top:1px solid var(--riga); color:var(--tenue); font-size:14px; padding:28px 16px; text-align:center; }}
/* ── Effetti ─────────────────────────────────────────────── */
.liquido {{ position:fixed; inset:0; z-index:-1; overflow:hidden; pointer-events:none; }}
.liquido i {{ position:absolute; width:46vmax; height:46vmax; border-radius:50%; filter:blur(80px); opacity:.35; mix-blend-mode:screen; animation:vaga 28s ease-in-out infinite alternate; }}
.liquido i:nth-child(1) {{ background:var(--accento); left:-10vmax; top:-12vmax; }}
.liquido i:nth-child(2) {{ background:var(--accento2); right:-14vmax; top:20vh; animation-duration:34s; animation-delay:-8s; }}
.liquido i:nth-child(3) {{ background:#1b5cff; left:20vw; bottom:-20vmax; animation-duration:40s; animation-delay:-16s; opacity:.22; }}
:root[data-theme=light] .liquido i, .chiaro .liquido i {{ mix-blend-mode:multiply; opacity:.18; }}
@keyframes vaga {{ 0% {{ transform:translate(0,0) scale(1); border-radius:48% 52% 55% 45%; }} 50% {{ transform:translate(8vw,6vh) scale(1.15); border-radius:60% 40% 45% 55%; }} 100% {{ transform:translate(-6vw,10vh) scale(.95); border-radius:42% 58% 50% 50%; }} }}
.avanza {{ position:fixed; top:0; left:0; height:3px; width:100%; transform-origin:0 50%; transform:scaleX(0); background:linear-gradient(90deg,var(--accento),var(--accento2)); z-index:10; }}
.eroe h1 span.l {{ background-size:200% 100%; animation:scorre 8s linear infinite; }}
@keyframes scorre {{ to {{ background-position:200% 0; }} }}
.eroe .vetrina {{ margin-top:42px; perspective:1400px; }}
.eroe .vetrina img {{ width:100%; border-radius:20px; border:1px solid var(--riga); box-shadow:0 40px 120px -30px color-mix(in srgb,var(--accento) 45%,transparent); transform:rotateX(14deg) scale(.96); transform-origin:50% 0; transition:transform .9s cubic-bezier(.2,.8,.2,1); }}
.eroe .vetrina.su img {{ transform:rotateX(0) scale(1); }}
.chips {{ display:flex; flex-wrap:wrap; gap:10px; margin-top:26px; }}
.chips span {{ border:1px solid var(--riga); background:color-mix(in srgb,var(--carta) 70%,transparent); backdrop-filter:blur(10px); padding:6px 14px; border-radius:999px; font-size:14px; color:var(--tenue); }}
.appare {{ opacity:0; transform:translateY(40px) scale(.98); transition:opacity .9s ease, transform .9s cubic-bezier(.2,.8,.2,1); }}
.appare.vista {{ opacity:1; transform:none; }}
figure {{ transition:transform .35s cubic-bezier(.2,.8,.2,1), box-shadow .35s; will-change:transform; }}
figure:hover {{ box-shadow:0 30px 80px -30px color-mix(in srgb,var(--accento) 55%,transparent); }}
figure img {{ transition:transform .6s cubic-bezier(.2,.8,.2,1); }}
figure:hover img {{ transform:scale(1.02); }}
h2 {{ background:linear-gradient(90deg,var(--testo),color-mix(in srgb,var(--accento) 70%,var(--testo))); -webkit-background-clip:text; background-clip:text; color:transparent; }}
section {{ position:relative; }}
section h2::before {{ content:""; display:block; width:42px; height:4px; border-radius:4px; margin-bottom:14px; background:linear-gradient(90deg,var(--accento),var(--accento2)); }}
@media (prefers-reduced-motion: reduce) {{ .liquido i, .eroe h1 span.l {{ animation:none; }} .appare {{ opacity:1; transform:none; transition:none; }} figure, figure img, .eroe .vetrina img {{ transition:none; transform:none; }} html {{ scroll-behavior:auto; }} }}
@media (max-width:640px) {{ .barra {{ flex-wrap:wrap; }} nav {{ order:3; width:100%; }} body {{ font-size:16px; }} }}
</style>
</head>
<body>
<div class="liquido" aria-hidden="true"><i></i><i></i><i></i></div><div class="avanza" id="avanza"></div>
<header><div class="barra">
<div class="marchio"><b>Liquid</b> DE</div>
<nav>{nav}<a href="#architettura">{bi("Architettura","Architecture")}</a><a href="#scorciatoie">{bi("Scorciatoie","Shortcuts")}</a></nav>
<button id="lingua" type="button" aria-label="Lingua / Language">EN</button>
<button id="tema" type="button" aria-label="Tema / Theme">◐</button>
</div></header>
<main>
<div class="eroe">
<h1>{bi('Un desktop <span class="l">liquido</span>.'.replace('<span class="l">','⟦').replace('</span>','⟧'), 'A <span class="l">liquid</span> desktop.'.replace('<span class="l">','⟦').replace('</span>','⟧'))}</h1>
{bi("Liquid DE è un ambiente desktop per Linux su Wayland: compositore, demone, interfaccia, schermata di accesso e app di sistema, scritti insieme. Solido ma liquido: il testo resta fermo e nitido, si muove la forma.",
    "Liquid DE is a desktop environment for Linux on Wayland: compositor, daemon, interface, login screen and system apps, written together. Solid yet liquid: text stays still and sharp, shapes move.", "p")}
<div class="chips"><span>Wayland</span><span>wlroots 0.20.2</span><span>Quickshell · QML</span><span>Dart</span><span>GPL-3.0</span></div>
<div class="vetrina" id="vetrina"><img src="img/oggi.webp" alt="Liquid DE"></div>
</div>
{''.join(corpo)}
<section id="architettura"><h2>{bi("Architettura","Architecture")}</h2>
{bi("Tre programmi che si parlano solo attraverso due canali dichiarati, mai per scorciatoie. Ognuno può ripartire senza portare giù gli altri.",
    "Three programs that talk only through two declared channels, never through shortcuts. Each can restart without taking the others down.", "p")}
<div class="schema">{SCHEMA}</div>
<div class="cards">{arch}</div></section>
<section id="scorciatoie"><h2>{bi("Scorciatoie","Shortcuts")}</h2>
<table>{tasti}</table></section>
</main>
<footer>{bi("Liquid DE — GPL-3.0. Le schermate vengono da una sessione dimostrativa con dati di esempio.","Liquid DE — GPL-3.0. Screenshots come from a demo session with sample data.")}</footer>
<script>
(function(){{
  var h=document.documentElement, L=document.getElementById('lingua'), T=document.getElementById('tema');
  function lingua(l){{ h.dataset.lang=l; h.lang=l; L.textContent=l==='it'?'EN':'IT'; try{{localStorage.setItem('lingua',l);}}catch(e){{}} }}
  var l0='it'; try{{ l0=localStorage.getItem('lingua')||((navigator.language||'it').slice(0,2)==='it'?'it':'en'); }}catch(e){{}}
  lingua(l0);
  L.onclick=function(){{ lingua(h.dataset.lang==='it'?'en':'it'); }};
  try{{ var t=localStorage.getItem('tema'); if(t) h.dataset.theme=t; }}catch(e){{}}
  var muto = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var A=document.getElementById('avanza');
  function scorri(){{ var m=document.documentElement.scrollHeight-innerHeight; A.style.transform='scaleX('+(m>0?scrollY/m:0)+')'; }}
  addEventListener('scroll',scorri,{{passive:true}}); scorri();
  var V=document.getElementById('vetrina'); setTimeout(function(){{ V.classList.add('su'); }}, 250);
  var el=document.querySelectorAll('section > *, .card, figure');
  if(!muto && 'IntersectionObserver' in window){{
    el.forEach(function(x){{ x.classList.add('appare'); }});
    var io=new IntersectionObserver(function(v){{ v.forEach(function(k){{ if(k.isIntersecting){{ k.target.classList.add('vista'); io.unobserve(k.target); }} }}); }},{{rootMargin:'0px 0px -8% 0px'}});
    el.forEach(function(x){{ io.observe(x); }});
    document.querySelectorAll('figure').forEach(function(f){{
      f.addEventListener('pointermove',function(ev){{ var r=f.getBoundingClientRect(), x=(ev.clientX-r.left)/r.width-.5, y=(ev.clientY-r.top)/r.height-.5; f.style.transform='perspective(900px) rotateY('+(x*6)+'deg) rotateX('+(-y*6)+'deg) translateY(-4px)'; }});
      f.addEventListener('pointerleave',function(){{ f.style.transform=''; }});
    }});
  }}
  T.onclick=function(){{ var scuro=h.dataset.theme?h.dataset.theme==='dark':!matchMedia('(prefers-color-scheme: light)').matches; h.dataset.theme=scuro?'light':'dark'; try{{localStorage.setItem('tema',h.dataset.theme);}}catch(e){{}} }};
}})();
</script>
</body>
</html>
"""
PAGINA = PAGINA.replace("⟦", '<span class="l">').replace("⟧", "</span>")
(OUT / "index.html").write_text(PAGINA, encoding="utf-8")
print("scritto", len(PAGINA), "caratteri")
