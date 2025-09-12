document.addEventListener("DOMContentLoaded", function () {
  const page = document.body.dataset.page;
  const footerContent = document.getElementById("footer-content");

  console.log("✅ Footer JS loaded. Current page:", page);
  console.log("Footer container found:", !!footerContent);

  if (!footerContent) {
    console.warn("No footer container found!");
    return;
  }

  if (page === "future" || page === "opened") {
    footerContent.innerHTML = `
      <nav class="mb-3">
        <a href="/" class="me-3 text-success text-decoration-none">Home</a>
        <a href="/future/" class="me-3 text-success text-decoration-none">Future</a>
        <a href="/opened/" class="text-success text-decoration-none">Opened</a>
      </nav>
      <p class="text-muted">&copy; ${new Date().getFullYear()} TimeCapsule</p>
    `;
  } else {
    footerContent.innerHTML = `
      <h2>Ready to Begin?</h2>
      <p>Start creating your first time capsule today and give your future self the gift of remembering this beautiful moment.</p>
      <a href="#" class="cta-btn">Create Your First Time Capsule</a>
    `;
  }
});