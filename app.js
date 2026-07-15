document.querySelectorAll("[data-copy]").forEach(btn => {
  btn.addEventListener("click", async () => {
    const txt = btn.getAttribute("data-copy");
    try {
      await navigator.clipboard.writeText(txt);
      const old = btn.textContent;
      btn.textContent = "Copied!";
      setTimeout(() => (btn.textContent = old), 900);
    } catch {
      alert("Copy failed. Please copy manually: " + txt);
    }
  });
});
