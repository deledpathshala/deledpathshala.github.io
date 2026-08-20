document.documentElement.classList.add("js");

(() => {
  const topbar = document.querySelector(".topbar");
  const menuBtn = document.getElementById("menuBtn");
  const siteNav = document.getElementById("siteNav");

  const updateTopbar = () => topbar?.classList.toggle("is-scrolled", window.scrollY > 10);
  updateTopbar();
  window.addEventListener("scroll", updateTopbar, { passive: true });

  const closeMenu = () => {
    if (!menuBtn || !siteNav) return;
    menuBtn.setAttribute("aria-expanded", "false");
    siteNav.classList.remove("is-open");
  };

  if (menuBtn && siteNav) {
    menuBtn.addEventListener("click", () => {
      const opening = menuBtn.getAttribute("aria-expanded") !== "true";
      menuBtn.setAttribute("aria-expanded", String(opening));
      siteNav.classList.toggle("is-open", opening);
    });
    siteNav.querySelectorAll("a").forEach((link) => link.addEventListener("click", closeMenu));
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") closeMenu();
    });
    document.addEventListener("click", (event) => {
      if (!topbar?.contains(event.target)) closeMenu();
    });
  }

  document.querySelectorAll("[data-copy]").forEach((button) => {
    button.addEventListener("click", async () => {
      const text = button.getAttribute("data-copy") || "";
      const original = button.textContent;
      try {
        await navigator.clipboard.writeText(text);
        button.textContent = "✓ Copied";
      } catch {
        window.prompt("Copy this:", text);
      }
      window.setTimeout(() => { button.textContent = original; }, 1200);
    });
  });

  document.querySelectorAll("[data-year]").forEach((el) => {
    el.textContent = new Date().getFullYear();
  });

  const revealItems = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        obs.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -8%", threshold: 0.08 });
    revealItems.forEach((item) => observer.observe(item));
  } else {
    revealItems.forEach((item) => item.classList.add("is-visible"));
  }

  const library = document.getElementById("pdfLibrary");
  if (!library) return;

  const list = document.getElementById("pdfList");
  const count = document.getElementById("pdfCount");
  const search = document.getElementById("pdfSearch");
  const semesterTabs = [...document.querySelectorAll("[data-semester]")];
  const typeTabs = [...document.querySelectorAll("[data-type]")];
  const state = { semester: "all", type: "all", query: "", items: [] };
  const semesterNames = {
    sem1: "Semester 1",
    sem2: "Semester 2",
    sem3: "Semester 3",
    sem4: "Semester 4",
    unknown: "Other"
  };

  const icon = (name) => {
    const paths = {
      open: '<path d="M15 3h6v6M10 14 21 3M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>',
      download: '<path d="M12 3v12m0 0 5-5m-5 5-5-5M5 21h14"/>'
    };
    return `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${paths[name]}</svg>`;
  };

  const makeItem = (item) => {
    const article = document.createElement("article");
    article.className = "pdfItem";

    const fileIcon = document.createElement("div");
    fileIcon.className = "pdfItem__icon";
    fileIcon.textContent = "PDF";

    const copy = document.createElement("div");
    copy.className = "pdfItem__left";
    const title = document.createElement("div");
    title.className = "pdfItem__title";
    title.textContent = item.title;
    title.title = item.title;
    const meta = document.createElement("div");
    meta.className = "pdfItem__meta";
    const type = document.createElement("span");
    type.className = "type-pill";
    type.textContent = item.type;
    const sem = document.createElement("span");
    sem.textContent = semesterNames[item.semester] || "Other";
    const size = document.createElement("span");
    size.textContent = `${item.sizeMB} MB`;
    meta.append(type, document.createTextNode("•"), sem, document.createTextNode("•"), size);
    copy.append(title, meta);

    const actions = document.createElement("div");
    actions.className = "pdfItem__right";
    const open = document.createElement("a");
    open.className = "pdf-action";
    open.href = item.url;
    open.target = "_blank";
    open.rel = "noopener";
    open.setAttribute("aria-label", `Open ${item.title}`);
    open.title = "Open PDF";
    open.innerHTML = icon("open");
    const download = document.createElement("a");
    download.className = "pdf-action pdf-action--download";
    download.href = item.url;
    download.download = `${item.title}.pdf`;
    download.setAttribute("aria-label", `Download ${item.title}`);
    download.title = "Download PDF";
    download.innerHTML = icon("download");
    actions.append(open, download);
    article.append(fileIcon, copy, actions);
    return article;
  };

  const setActiveTabs = () => {
    semesterTabs.forEach((tab) => {
      const active = tab.dataset.semester === state.semester;
      tab.classList.toggle("libTab--active", active);
      tab.setAttribute("aria-pressed", String(active));
    });
    typeTabs.forEach((tab) => {
      const active = tab.dataset.type === state.type;
      tab.classList.toggle("libTab--active", active);
      tab.setAttribute("aria-pressed", String(active));
    });
  };

  const render = () => {
    const query = state.query.trim().toLocaleLowerCase("hi");
    const filtered = state.items.filter((item) => {
      const semesterMatch = state.semester === "all" || item.semester === state.semester;
      const typeMatch = state.type === "all" || item.type === state.type;
      const searchMatch = !query || `${item.title} ${item.type} ${semesterNames[item.semester] || ""}`.toLocaleLowerCase("hi").includes(query);
      return semesterMatch && typeMatch && searchMatch;
    });

    list.replaceChildren();
    count.textContent = `${filtered.length} ${filtered.length === 1 ? "PDF" : "PDFs"}`;
    if (!filtered.length) {
      const empty = document.createElement("div");
      empty.className = "libEmpty";
      empty.innerHTML = "<strong>Koi PDF nahi mili</strong>Search ya filters ko change karke dekhiye.";
      list.append(empty);
      return;
    }
    const fragment = document.createDocumentFragment();
    filtered.forEach((item) => fragment.append(makeItem(item)));
    list.append(fragment);
  };

  semesterTabs.forEach((tab) => tab.addEventListener("click", () => {
    state.semester = tab.dataset.semester;
    setActiveTabs();
    render();
    const hash = state.semester === "all" ? "" : `#${state.semester}`;
    history.replaceState(null, "", `${location.pathname}${location.search}${hash}`);
  }));

  typeTabs.forEach((tab) => tab.addEventListener("click", () => {
    state.type = tab.dataset.type;
    setActiveTabs();
    render();
  }));

  let searchTimer;
  search?.addEventListener("input", () => {
    window.clearTimeout(searchTimer);
    searchTimer = window.setTimeout(() => {
      state.query = search.value;
      render();
    }, 120);
  });

  const initialSemester = location.hash.slice(1);
  if (["sem1", "sem2", "sem3", "sem4", "unknown"].includes(initialSemester)) {
    state.semester = initialSemester;
  }
  setActiveTabs();

  fetch("./pdf-index.json")
    .then((response) => {
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return response.json();
    })
    .then((items) => {
      state.items = Array.isArray(items) ? items : [];
      render();
    })
    .catch(() => {
      list.innerHTML = '<div class="libError"><strong>Library load nahi ho paayi</strong>Page refresh karein ya thodi der baad dobara try karein.</div>';
      count.textContent = "Unavailable";
    });
})();
