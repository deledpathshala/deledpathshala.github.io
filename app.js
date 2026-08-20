/* DELED Pathshala — interactions */
document.documentElement.classList.add("js");

/* ---------- Copy chips ---------- */
document.querySelectorAll("[data-copy]").forEach((btn) => {
  btn.addEventListener("click", async () => {
    const txt = btn.getAttribute("data-copy");
    const old = btn.textContent;
    try {
      await navigator.clipboard.writeText(txt);
      btn.textContent = "✓ Copied!";
      btn.style.color = "var(--green)";
    } catch {
      alert("Copy failed. Please copy manually: " + txt);
    }
    setTimeout(() => {
      btn.textContent = old;
      btn.style.color = "";
    }, 1100);
  });
});

/* ---------- Mobile menu ---------- */
const menuBtn = document.getElementById("menuBtn");
const mobileMenu = document.getElementById("mobileMenu");

if (menuBtn && mobileMenu) {
  menuBtn.addEventListener("click", () => {
    const isOpen = !mobileMenu.hasAttribute("hidden");
    if (isOpen) {
      mobileMenu.setAttribute("hidden", "");
      menuBtn.setAttribute("aria-expanded", "false");
    } else {
      mobileMenu.removeAttribute("hidden");
      menuBtn.setAttribute("aria-expanded", "true");
    }
  });

  mobileMenu.querySelectorAll("a").forEach((a) => {
    a.addEventListener("click", () => {
      mobileMenu.setAttribute("hidden", "");
      menuBtn.setAttribute("aria-expanded", "false");
    });
  });
}

/* ---------- Scroll reveal ---------- */
const revealEls = document.querySelectorAll("[data-reveal]");
if (revealEls.length && "IntersectionObserver" in window) {
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add("is-visible");
          io.unobserve(e.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
  );
  revealEls.forEach((el) => io.observe(el));
} else {
  revealEls.forEach((el) => el.classList.add("is-visible"));
}

/* ---------- PDF library: search + filters ---------- */
const libList = document.getElementById("libList");
if (libList) {
  const items = Array.from(libList.querySelectorAll(".pdfItem"));
  const sections = Array.from(libList.querySelectorAll(".libSection"));
  const searchInput = document.getElementById("libSearch");
  const semFilters = document.getElementById("semFilters");
  const typeFilters = document.getElementById("typeFilters");
  const countEl = document.getElementById("libCount");
  const emptyEl = document.getElementById("emptyState");

  let state = { q: "", sem: "all", type: "all" };

  function apply() {
    const q = state.q.trim().toLowerCase();
    let visible = 0;

    // 1) filter individual items by type + search
    items.forEach((item) => {
      const matchType = state.type === "all" || item.dataset.type === state.type;
      const matchQ = !q || item.dataset.search.includes(q);
      const show = matchType && matchQ;
      item.classList.toggle("is-hidden", !show);
      if (show) visible++;
    });

    // 2) show/hide semester sections + hide empty ones
    sections.forEach((sec) => {
      const matchSem = state.sem === "all" || sec.dataset.sem === state.sem;
      const hasVisibleItem = sec.querySelectorAll(".pdfItem:not(.is-hidden)").length > 0;
      sec.style.display = matchSem && hasVisibleItem ? "" : "none";
    });

    if (countEl) {
      countEl.innerHTML = "Showing <b>" + visible + "</b> of <b>" + items.length + "</b> PDFs";
    }
    if (emptyEl) emptyEl.style.display = visible === 0 ? "block" : "none";
  }

  if (searchInput) searchInput.addEventListener("input", (e) => {
    state.q = e.target.value;
    apply();
  });

  function bindTabs(container, key) {
    if (!container) return;
    container.addEventListener("click", (e) => {
      const tab = e.target.closest(".libTab");
      if (!tab) return;
      container.querySelectorAll(".libTab").forEach((t) => t.classList.remove("libTab--active"));
      tab.classList.add("libTab--active");
      state[key] = tab.dataset[key];
      apply();
    });
  }

  bindTabs(semFilters, "sem");
  bindTabs(typeFilters, "type");

  // Sync with #hash deep links (e.g. /deled-notes-pdf.html#sem2)
  function applyHash() {
    const h = location.hash.replace("#", "");
    if (["sem1", "sem2", "sem3", "sem4", "unknown"].includes(h)) {
      state.sem = h;
      const tab = semFilters && semFilters.querySelector('[data-sem="' + h + '"]');
      if (tab) {
        semFilters.querySelectorAll(".libTab").forEach((t) => t.classList.remove("libTab--active"));
        tab.classList.add("libTab--active");
      }
      apply();
      document.getElementById(h)?.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }
  applyHash();
  window.addEventListener("hashchange", applyHash);
}

/* ---------- Footer year ---------- */
const yearEl = document.getElementById("year");
if (yearEl) yearEl.textContent = new Date().getFullYear();
