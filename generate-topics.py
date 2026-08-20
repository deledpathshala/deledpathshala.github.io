#!/usr/bin/env python3
"""Generates deled-series.html, ctet-notes.html, supertet-mock.html."""

SERIES_BODY = """
        <div class="tipBox" data-reveal>
          <div class="tipBox__title">🎯 अबको क्या मिलेगा?</div>
          <div class="tipBox__text">
            • DELED quizzes (topic-wise + revision style)<br/>
            • Daily practice sets (regular updates channel par)<br/>
            • Group me quiz participation (24×7 active discussion + practice)<br/>
            • PYQ/important questions based practice (exam pattern ke hisaab se)
          </div>
        </div>

        <h2 class="h2 mt28">How to participate (simple)</h2>
        <p class="subLead">Bas channel join karke group me participate karo — practice automatic routine ban jaati hai.</p>

        <div class="featureGrid" style="margin-top:16px">
          <article class="feature" data-reveal><div class="feature__icon ico--indigo">1️⃣</div><h3>Step 1</h3><p>Telegram channel join karo: daily quiz/practice sets yahin aate hain.</p></article>
          <article class="feature" data-reveal><div class="feature__icon ico--orange">2️⃣</div><h3>Step 2</h3><p>Discussion/quiz group join karo: doubts + regular quiz participation.</p></article>
          <article class="feature" data-reveal><div class="feature__icon ico--teal">3️⃣</div><h3>Step 3</h3><p>Wrong answers note karo + same topic ka short revision karo.</p></article>
          <article class="feature" data-reveal><div class="feature__icon ico--green">4️⃣</div><h3>Step 4</h3><p>Consistency: 15–30 min daily practice se score fast improve hota hai.</p></article>
        </div>

        <div class="tipBox mt16" data-reveal>
          <div class="tipBox__title">🖼 Notes ki quality dekhni hai?</div>
          <div class="tipBox__text">Homepage par notes samples gallery available hai: <a href="./#preview"><b>Open Notes Preview →</b></a></div>
        </div>

        <div class="ctaRow" data-reveal>
          <a class="btn btn--accent" href="https://t.me/deled_pathshala_discussion" target="_blank" rel="noopener">Start Quiz Practice</a>
          <a class="btn btn--primary" href="./deled-notes-pdf.html">📚 Notes PDF Page</a>
        </div>"""

CTET_BODY = """
        <div class="tipBox" data-reveal>
          <div class="tipBox__title">📝 CTET preparation ke liye ye useful</div>
          <div class="tipBox__text">
            • Notes PDFs + short revision points<br/>
            • Quizzes / practice sets for speed + accuracy<br/>
            • Doubts support via discussion group<br/>
            • Regular updates on Telegram
          </div>
        </div>

        <h2 class="h2 mt28">🔍 Quick tip (Telegram search)</h2>
        <p class="subLead">Telegram channel kholo kar search me ye type karo:</p>
        <div class="tipBox" data-reveal>
          <div class="tipBox__text"><b>ctet notes</b>, <b>ctet</b>, <b>pedagogy</b>, <b>quiz</b>, <b>mock</b></div>
        </div>

        <div class="ctaRow" data-reveal>
          <a class="btn btn--accent" href="https://t.me/Deled_Pathshala" target="_blank" rel="noopener">Get CTET Notes</a>
          <a class="btn btn--primary" href="./deled-series.html">Open DELED Quiz Series</a>
        </div>"""

SUPERTET_BODY = """
        <div class="tipBox" data-reveal>
          <div class="tipBox__title">✴️ Daily practice ka best routine (15–30 min)</div>
          <div class="tipBox__text">
            • Daily practice set attempt karo (channel)<br/>
            • गलत questions mark karo short revision karo<br/>
            • Group me participation + doubts clear karo<br/>
            • Weekly 1 mock-style session (speed + accuracy)
          </div>
        </div>

        <h2 class="h2 mt28">🔍 Quick search (Telegram)</h2>
        <p class="subLead">Channel search me ye type karke relevant posts jaldi milenge:</p>
        <div class="tipBox" data-reveal>
          <div class="tipBox__text"><b>supertet</b>, <b>mock</b>, <b>quiz</b>, <b>practice set</b>, <b>revision</b></div>
        </div>

        <div class="ctaRow" data-reveal>
          <a class="btn btn--accent" href="https://t.me/deled_pathshala_discussion" target="_blank" rel="noopener">Participate in Quizzes</a>
          <a class="btn btn--primary" href="./ctet-notes.html">CTET Notes</a>
          <a class="btn btn--ghost" href="./deled-series.html">DELED Series</a>
        </div>"""

PAGES = [
    {
        "file": "deled-series.html",
        "active": "Series",
        "title": "DELED Series (Quiz/Practice Sets) — DELED Pathshala | Daily Practice on Telegram",
        "desc": "DELED series: daily quizzes, practice sets, PYQ practice and mock-style preparation. 24×7 quiz participation in discussion group. Join DELED Pathshala Telegram channel + group.",
        "kicker": "✦ Quiz & Practice",
        "h1a": "DELED Series",
        "h1b": "(Quiz / Practice Sets)",
        "lead": "Agar aap <b>DELED / DLED</b> ke liye <b>practice</b> aur <b>quiz series</b> dhoondh rahe ho, toh <b>DELED Pathshala</b> par aapko daily practice sets, quizzes aur revision-friendly MCQs milte hain. Goal simple hai: <b>regular practice + better score</b>.",
        "cta_primary": ["https://t.me/Deled_Pathshala", "Join Telegram Channel"],
        "body": SERIES_BODY,
    },
    {
        "file": "ctet-notes.html",
        "active": "CTET",
        "title": "CTET Notes — PDFs, Practice Sets & Quizzes | DELED Pathshala (Telegram)",
        "desc": "CTET notes: pedagogy-focused notes PDFs, practice sets, quizzes and revision support. Join DELED Pathshala Telegram channel + group for regular updates and practice.",
        "kicker": "✦ CTET",
        "h1a": "CTET Notes",
        "h1b": "(PDF + Practice)",
        "lead": "Agar aap <b>CTET notes</b> aur <b>practice</b> dhoondh rahe ho, toh DELED Pathshala par aapko exam-oriented material milta hai — notes PDFs + quizzes/practice sets. CTET preparation me consistency aur practice sabse important hoti hai.",
        "cta_primary": ["https://t.me/Deled_Pathshala", "Join Telegram Channel"],
        "body": CTET_BODY,
    },
    {
        "file": "supertet-mock.html",
        "active": "SuperTET",
        "title": "SuperTET Mock Tests & Daily Quiz — DELED Pathshala | Practice Sets on Telegram",
        "desc": "SuperTET practice: daily practice set quiz, mock-style MCQ practice, revision and doubts support. Join DELED Pathshala Telegram channel + 24×7 quiz group.",
        "kicker": "✦ SuperTET",
        "h1a": "SuperTET Mock Tests",
        "h1b": "+ Daily Practice",
        "lead": "SuperTET preparation me <b>regular MCQ practice</b> aur <b>mock tests</b> ka bahut bada role hota hai. DELED Pathshala ke Telegram channel par aapko <b>daily SuperTET practice set quiz</b> milta hai, aur discussion group me aap practice + participation continue rakhte ho.",
        "cta_primary": ["https://t.me/Deled_Pathshala", "Join Telegram Channel"],
        "body": SUPERTET_BODY,
    },
]

SHELL = """<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#5a3df0" />
  <title>{{TITLE}}</title>
  <meta name="description" content="{{DESC}}" />
  <link rel="canonical" href="https://deledpathshala.github.io/{{FILE}}" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{{TITLE}}" />
  <meta property="og:description" content="{{DESC}}" />
  <meta property="og:url" content="https://deledpathshala.github.io/{{FILE}}" />
  <meta property="og:site_name" content="DELED Pathshala" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Inter:wght@400;600;700;800;900&family=Noto+Sans+Devanagari:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="./style.css" />
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
  <link rel="manifest" href="/site.webmanifest">
</head>

<body>
  <div class="bg-decor" aria-hidden="true"><div class="blob blob--1"></div><div class="blob blob--2"></div><div class="blob blob--3"></div></div>

  <header class="topbar">
    <div class="wrap topbar__inner">
      <a class="brand" href="./">
        <span class="brand__mark" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 4h6a4 4 0 0 1 4 4v13"/><path d="M22 4h-6a4 4 0 0 0-4 4v13"/><path d="M12 3v18"/></svg></span>
        DELED Pathshala
      </a>
      <nav class="nav">
        <a href="./">Home</a>
        <a href="./deled-notes-pdf.html">Notes PDF</a>
        <a href="./deled-series.html" {{ACTIVE_SERIES}}>Series</a>
        <a href="./ctet-notes.html" {{ACTIVE_CTET}}>CTET</a>
        <a href="./supertet-mock.html" {{ACTIVE_SUPERTET}}>SuperTET</a>
      </nav>
      <button class="menuBtn" id="menuBtn" aria-expanded="false" aria-controls="mobileMenu">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg> Menu
      </button>
      <div class="topbar__cta">
        <a class="btn btn--mini btn--ghost" href="https://www.youtube.com/@Deled_Pathshala" target="_blank" rel="noopener">YouTube</a>
        <a class="btn btn--mini btn--accent" href="https://t.me/Deled_Pathshala" target="_blank" rel="noopener">Join</a>
      </div>
    </div>
  </header>

  <div class="mobileMenu" id="mobileMenu" hidden>
    <div class="mobileMenu__inner wrap">
      <a href="./">🏠 Home</a>
      <a href="./deled-notes-pdf.html">📚 Notes PDF Library</a>
      <a href="./deled-series.html">🎯 DELED Series</a>
      <a href="./ctet-notes.html">📝 CTET Notes</a>
      <a href="./supertet-mock.html">✍ SuperTET Mock</a>
      <div class="mobileMenu__hr"></div>
      <a href="https://t.me/Deled_Pathshala" target="_blank" rel="noopener">✈ Join Telegram Channel</a>
      <a href="https://t.me/deled_pathshala_discussion" target="_blank" rel="noopener">👋 Doubts / Quiz Group</a>
      <a href="https://www.youtube.com/@Deled_Pathshala" target="_blank" rel="noopener">▶ YouTube Classes</a>
    </div>
  </div>

  <main>
    <section class="pageHero">
      <div class="wrap">
        <span class="kicker">{{KICKER}}</span>
        <h1>{{H1A}} <span class="grad-text">{{H1B}}</span></h1>
        <p class="lead">{{LEAD}}</p>
        <div class="ctaRow">
          <a class="btn btn--accent btn--lg" href="{{CTA_PRIMARY_URL}}" target="_blank" rel="noopener">{{CTA_PRIMARY_TEXT}}</a>
          <a class="btn btn--soft" href="https://t.me/deled_pathshala_discussion" target="_blank" rel="noopener">Join Doubts Group</a>
          <a class="btn btn--soft" href="https://t.me/s/Deled_Pathshala" target="_blank" rel="noopener">Latest Posts</a>
        </div>
      </div>
    </section>

    <section class="page">
      <div class="wrap page__inner">
{{BODY}}
        <div class="ctaRow" data-reveal style="margin-top:18px">
          <button class="copyChip" data-copy="@deled_pathshala">📋 Copy @deled_pathshala</button>
          <button class="copyChip" data-copy="@deled_pathshala_discussion">📋 Copy @deled_pathshala_discussion</button>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="wrap">
      <div class="footer__top">
        <div>
          <a class="brand" href="./"><span class="brand__mark" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 4h6a4 4 0 0 1 4 4v13"/><path d="M22 4h-6a4 4 0 0 0-4 4v13"/><path d="M12 3v18"/></svg></span> DELED Pathshala</a>
          <p class="footer__desc">UP DELED (BTC) notes PDFs, PYQ, quiz series और teaching exams की तैयारी — एक ही जगह विश्वसनीय सामग्री।</p>
        </div>
        <div>
          <h4>Study Material</h4>
          <ul>
            <li><a href="./deled-notes-pdf.html">Notes PDF Library</a></li>
            <li><a href="./semester-1.html">Semester 1</a></li>
            <li><a href="./semester-2.html">Semester 2</a></li>
            <li><a href="./semester-3.html">Semester 3</a></li>
            <li><a href="./semester-4.html">Semester 4</a></li>
          </ul>
        </div>
        <div>
          <h4>Practice & Exams</h4>
          <ul>
            <li><a href="./deled-series.html">DELED Series</a></li>
            <li><a href="./ctet-notes.html">CTET Notes</a></li>
            <li><a href="./supertet-mock.html">SuperTET Mock</a></li>
          </ul>
        </div>
        <div>
          <h4>Connect</h4>
          <div class="footer__social">
            <a href="https://t.me/Deled_Pathshala" target="_blank" rel="noopener">✈ Telegram</a>
            <a href="https://t.me/deled_pathshala_discussion" target="_blank" rel="noopener">👋 Group</a>
            <a href="https://www.youtube.com/@Deled_Pathshala" target="_blank" rel="noopener">▶ YouTube</a>
          </div>
        </div>
      </div>
      <div class="footer__bottom">
        <span>© <span id="year">2026</span> DELED Pathshala — UP D.El.Ed (BTC) Notes & Practice</span>
        <span>Made with ❤️ for DELED/BTC students</span>
      </div>
    </div>
  </footer>

  <script src="./app.js"></script>
</body>
</html>
"""


def render(p):
    out = SHELL
    out = out.replace("{{TITLE}}", p["title"])
    out = out.replace("{{DESC}}", p["desc"])
    out = out.replace("{{FILE}}", p["file"])
    out = out.replace("{{KICKER}}", p["kicker"])
    out = out.replace("{{H1A}}", p["h1a"])
    out = out.replace("{{H1B}}", p["h1b"])
    out = out.replace("{{LEAD}}", p["lead"])
    out = out.replace("{{CTA_PRIMARY_URL}}", p["cta_primary"][0])
    out = out.replace("{{CTA_PRIMARY_TEXT}}", p["cta_primary"][1])
    out = out.replace("{{BODY}}", p["body"])

    act = p["active"]
    out = out.replace("{{ACTIVE_SERIES}}", 'class="is-active"' if act == "Series" else "")
    out = out.replace("{{ACTIVE_CTET}}", 'class="is-active"' if act == "CTET" else "")
    out = out.replace("{{ACTIVE_SUPERTET}}", 'class="is-active"' if act == "SuperTET" else "")
    return out


if __name__ == "__main__":
    for p in PAGES:
        open(p["file"], "w", encoding="utf-8").write(render(p))
        print("wrote", p["file"])
