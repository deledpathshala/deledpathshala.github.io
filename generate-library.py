#!/usr/bin/env python3
"""
Regenerates deled-notes-pdf.html from pdf-index.json.

Run:  python3 generate-library.py
"""
import json
from urllib.parse import unquote

SEM_ORDER = ["sem1", "sem2", "sem3", "sem4", "unknown"]
SEM_LABEL = {
    "sem1": "Semester 1",
    "sem2": "Semester 2",
    "sem3": "Semester 3",
    "sem4": "Semester 4",
    "unknown": "Other",
}
TYPE_ICON = {
    "Notes": ("\U0001F4D8", "ico--indigo"),
    "PYQ": ("\U0001F4D9", "ico--orange"),
    "PDF": ("\U0001F4C4", "ico--teal"),
    "Important": ("\u2B50", "ico--orange"),
    "Internship": ("\U0001F4D2", "ico--green"),
}


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def item_html(item):
    title = esc(item["title"])
    typ = item["type"]
    sem = item["semester"]
    size = item.get("sizeMB")
    url = item["url"]
    icon, ico_cls = TYPE_ICON.get(typ, ("\U0001F4C4", "ico--teal"))

    # clean download filename from URL
    filename = unquote(url.rsplit("/", 1)[-1])

    search = title.lower()
    meta_pills = f'<span class="pill pill--type">{typ}</span>'
    if size:
        meta_pills += f'<span class="pill pill--size">{size} MB</span>'
    meta_pills += f'<span class="pill pill--sem">{SEM_LABEL.get(sem, "Other")}</span>'

    return f"""
      <div class="pdfItem" data-sem="{sem}" data-type="{typ}" data-search="{search}">
        <div class="pdfItem__left">
          <div class="pdfItem__icon {ico_cls}">{icon}</div>
          <div>
            <div class="pdfItem__title">{title}</div>
            <div class="pdfItem__meta">{meta_pills}</div>
          </div>
        </div>
        <div class="pdfItem__right">
          <a class="btn btn--mini btn--ghost" href="{url}" target="_blank" rel="noopener">Open</a>
          <a class="btn btn--mini btn--primary" href="{url}" download="{esc(filename)}">Download</a>
        </div>
      </div>"""


def main():
    data = json.load(open("pdf-index.json", encoding="utf-8-sig"))

    groups = {s: [x for x in data if x["semester"] == s] for s in SEM_ORDER}

    lib_sections = []
    for sem in SEM_ORDER:
        items = groups[sem]
        if not items:
            continue
        label = SEM_LABEL[sem]
        cards = "".join(item_html(x) for x in items)
        lib_sections.append(f"""
      <div class="libSection" data-sem="{sem}">
        <div class="tipBox" id="{sem}">
          <div class="tipBox__title">\U0001F4DA {label} — PDFs</div>
          <div class="tipBox__text">Is semester ke notes / PYQ / practice PDFs niche list me hain.</div>
        </div>
        {cards}
      </div>""")

    list_html = "\n".join(lib_sections)

    page = HEAD.replace("{{LIST}}", list_html).replace("{{TOTAL}}", str(len(data)))
    open("deled-notes-pdf.html", "w", encoding="utf-8").write(page)
    print(f"Generated deled-notes-pdf.html with {len(data)} PDFs")


HEAD = """<!DOCTYPE html>
<html lang='hi'>
<head>
  <meta charset='utf-8' />
  <meta name='viewport' content='width=device-width, initial-scale=1' />
  <meta name='theme-color' content='#5a3df0' />
  <title>DELED Notes PDF (Semester-wise) | DELED Pathshala</title>
  <meta name='description' content='UP DELED (BTC) Semester 1-4 Notes PDFs, PYQ and practice material. Download semester-wise PDFs on DELED Pathshala.' />
  <link rel='canonical' href='https://deledpathshala.github.io/deled-notes-pdf.html' />
  <meta property='og:type' content='website' />
  <meta property='og:title' content='DELED Notes PDF (Semester-wise) | DELED Pathshala' />
  <meta property='og:description' content='UP DELED (BTC) Semester 1-4 Notes PDFs, PYQ and practice material. Download semester-wise PDFs on DELED Pathshala.' />
  <meta property='og:url' content='https://deledpathshala.github.io/deled-notes-pdf.html' />
  <meta property='og:site_name' content='DELED Pathshala' />
  <meta name='twitter:card' content='summary' />

  <link rel='preconnect' href='https://fonts.googleapis.com' />
  <link rel='preconnect' href='https://fonts.gstatic.com' crossorigin />
  <link href='https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Inter:wght@400;600;700;800;900&family=Noto+Sans+Devanagari:wght@400;500;600;700&display=swap' rel='stylesheet' />

  <link rel='stylesheet' href='./style.css' />
  <link rel='apple-touch-icon' sizes='180x180' href='/apple-touch-icon.png'>
  <link rel='icon' type='image/png' sizes='32x32' href='/favicon-32x32.png'>
  <link rel='icon' type='image/png' sizes='16x16' href='/favicon-16x16.png'>
</head>

<body>
  <div class='bg-decor' aria-hidden='true'>
    <div class='blob blob--1'></div>
    <div class='blob blob--2'></div>
    <div class='blob blob--3'></div>
  </div>

  <header class='topbar'>
    <div class='wrap topbar__inner'>
      <a class='brand' href='../'>
        <span class='brand__mark' aria-hidden='true'>
          <svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M2 4h6a4 4 0 0 1 4 4v13'/><path d='M22 4h-6a4 4 0 0 0-4 4v13'/><path d='M12 3v18'/></svg>
        </span>
        DELED Pathshala
      </a>

      <nav class='nav'>
        <a href='../'>Home</a>
        <a href='./deled-notes-pdf.html' class='is-active'>Notes PDF</a>
        <a href='./deled-series.html'>Series</a>
        <a href='./ctet-notes.html'>CTET</a>
        <a href='./supertet-mock.html'>SuperTET</a>
      </nav>

      <button class='menuBtn' id='menuBtn' aria-expanded='false' aria-controls='mobileMenu'>
        <svg width='18' height='18' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round'><path d='M4 6h16M4 12h16M4 18h16'/></svg> Menu
      </button>

      <div class='topbar__cta'>
        <a class='btn btn--mini btn--ghost' href='https://www.youtube.com/@Deled_Pathshala' target='_blank' rel='noopener'>YouTube</a>
        <a class='btn btn--mini btn--accent' href='https://t.me/Deled_Pathshala' target='_blank' rel='noopener'>Join</a>
      </div>
    </div>
  </header>

  <div class='mobileMenu' id='mobileMenu' hidden>
    <div class='mobileMenu__inner wrap'>
      <a href='../'>🏠 Home</a>
      <a href='./deled-notes-pdf.html'>📚 Notes PDF Library</a>
      <a href='./deled-series.html'>🎯 DELED Series</a>
      <a href='./ctet-notes.html'>📝 CTET Notes</a>
      <a href='./supertet-mock.html'>✍ SuperTET Mock</a>
      <div class='mobileMenu__hr'></div>
      <a href='https://t.me/Deled_Pathshala' target='_blank' rel='noopener'>✈ Join Telegram Channel</a>
      <a href='https://t.me/deled_pathshala_discussion' target='_blank' rel='noopener'>👋 Doubts / Quiz Group</a>
      <a href='https://www.youtube.com/@Deled_Pathshala' target='_blank' rel='noopener'>▶ YouTube Classes</a>
    </div>
  </div>

  <main>
    <section class='pageHero'>
      <div class='wrap'>
        <span class='kicker'>✦ PDF Library</span>
        <h1>Notes PDF <span class='grad-text'>Library</span></h1>
        <p class='lead'>UP DELED (BTC) Semester 1–4 के notes, PYQ और practice PDFs — search 🔍 करो, filter 🔀 लगाओ और download ⬇️ करो।</p>
        <div class='ctaRow'>
          <a class='btn btn--accent' href='https://t.me/Deled_Pathshala' target='_blank' rel='noopener'>✈ Join Telegram Channel</a>
          <a class='btn btn--soft' href='https://t.me/deled_pathshala_discussion' target='_blank' rel='noopener'>👋 Doubts / Quiz Group</a>
          <a class='btn btn--soft' href='./supertet-mock.html'>✎ Daily SuperTET Quiz</a>
        </div>
      </div>
    </section>

    <section class='page'>
      <div class='wrap page__inner'>
        <div class='libBar'>
          <div class='libSearchWrap'>
            <svg width='18' height='18' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round'><circle cx='11' cy='11' r='7'/><path d='m21 21-4.3-4.3'/></svg>
            <input class='libSearch' id='libSearch' type='search' placeholder='Search notes… (jaise: baal vikas, science, pyq)' />
          </div>
          <div class='libFilters' id='semFilters'>
            <button class='libTab libTab--active' data-sem='all'>All</button>
            <button class='libTab' data-sem='sem1'>Sem 1</button>
            <button class='libTab' data-sem='sem2'>Sem 2</button>
            <button class='libTab' data-sem='sem3'>Sem 3</button>
            <button class='libTab' data-sem='sem4'>Sem 4</button>
            <button class='libTab' data-sem='unknown'>Other</button>
          </div>
          <div class='libFilters' id='typeFilters'>
            <button class='libTab libTab--active' data-type='all'>All Types</button>
            <button class='libTab' data-type='Notes'>📚 Notes</button>
            <button class='libTab' data-type='PYQ'>📙 PYQ</button>
            <button class='libTab' data-type='PDF'>📄 PDF</button>
            <button class='libTab' data-type='Important'>⭐ Important</button>
            <button class='libTab' data-type='Internship'>📒 Internship</button>
          </div>
          <div class='libMeta'>
            <span class='libCount' id='libCount'>Total <b>{{TOTAL}}</b> PDFs</span>
          </div>
        </div>

        <div class='libList' id='libList'>{{LIST}}
        </div>

        <div class='emptyState' id='emptyState' style='display:none'>
          😔 Koi PDF nahin mili — <b>search/filter</b> badal kar dekhen, ya Telegram par maang lein.
        </div>
      </div>
    </section>
  </main>

  <footer class='footer'>
    <div class='wrap'>
      <div class='footer__top'>
        <div>
          <a class='brand' href='../'><span class='brand__mark' aria-hidden='true'><svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M2 4h6a4 4 0 0 1 4 4v13'/><path d='M22 4h-6a4 4 0 0 0-4 4v13'/><path d='M12 3v18'/></svg></span> DELED Pathshala</a>
          <p class='footer__desc'>UP DELED (BTC) notes PDFs, PYQ, quiz series और teaching exams की तैयारी — एक ही जगह विश्वसनीय सामग्री।</p>
        </div>
        <div>
          <h4>Study Material</h4>
          <ul>
            <li><a href='./deled-notes-pdf.html'>Notes PDF Library</a></li>
            <li><a href='./semester-1.html'>Semester 1</a></li>
            <li><a href='./semester-2.html'>Semester 2</a></li>
            <li><a href='./semester-3.html'>Semester 3</a></li>
            <li><a href='./semester-4.html'>Semester 4</a></li>
          </ul>
        </div>
        <div>
          <h4>Practice & Exams</h4>
          <ul>
            <li><a href='./deled-series.html'>DELED Series</a></li>
            <li><a href='./ctet-notes.html'>CTET Notes</a></li>
            <li><a href='./supertet-mock.html'>SuperTET Mock</a></li>
          </ul>
        </div>
        <div>
          <h4>Connect</h4>
          <div class='footer__social'>
            <a href='https://t.me/Deled_Pathshala' target='_blank' rel='noopener'>✈ Telegram</a>
            <a href='https://t.me/deled_pathshala_discussion' target='_blank' rel='noopener'>👋 Group</a>
            <a href='https://www.youtube.com/@Deled_Pathshala' target='_blank' rel='noopener'>▶ YouTube</a>
          </div>
        </div>
      </div>
      <div class='footer__bottom'>
        <span>© <span id='year'>2026</span> DELED Pathshala — UP D.El.Ed (BTC) Notes & Practice</span>
        <span>Made with ❤️ for DELED/BTC students</span>
      </div>
    </div>
  </footer>

  <script src='./app.js'></script>
</body>
</html>"""


if __name__ == "__main__":
    main()
