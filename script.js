const form = document.getElementById("feedbackForm");
const successMessage = document.getElementById("successMessage");

const subjects = {
  "Matemaatika": [18, 4.3],
  "Vene keel": [15, 4.6],
  "Andmebaasid": [20, 3.9],
  "Programmeerimine": [12, 4.5],
  "Inglise keel": [16, 4.2]
};

function renderSummary() {
  const body = document.getElementById("summaryBody");
  body.innerHTML = "";

  Object.entries(subjects).forEach(([subject, data]) => {
    const row = document.createElement("tr");

    row.innerHTML = `
      <td>${subject}</td>
      <td>${data[0]}</td>
      <td>${data[1]}</td>
    `;

    body.appendChild(row);
  });
}

function clearErrors() {
  document.querySelectorAll(".error").forEach((element) => {
    element.textContent = "";
  });
}

form.addEventListener("submit", function (event) {
  event.preventDefault();

  clearErrors();
  successMessage.textContent = "";

  const name = document.getElementById("name").value.trim();
  const className = document.getElementById("className").value.trim();
  const subject = document.getElementById("subject").value;
  const rating = document.querySelector(
    'input[name="rating"]:checked'
  );
  const comment = document.getElementById("comment").value.trim();

  let valid = true;

  if (!name) {
    document.getElementById("nameError").textContent =
      "Nimi on kohustuslik.";

    valid = false;
  }

  if (!className) {
    document.getElementById("classError").textContent =
      "Klass on kohustuslik.";

    valid = false;
  }

  if (!subject) {
    document.getElementById("subjectError").textContent =
      "Vali õppeaine.";

    valid = false;
  }

  if (!rating) {
    document.getElementById("ratingError").textContent =
      "Vali hinne 1–5.";

    valid = false;
  }

  if (comment.length > 500) {
    valid = false;
  }

  if (!valid) {
    return;
  }

  const value = Number(rating.value);

  if (subjects[subject]) {
    const [count, average] = subjects[subject];

    const newAverage =
      ((average * count) + value) / (count + 1);

    subjects[subject] = [
      count + 1,
      Number(newAverage.toFixed(1))
    ];
  }

  renderSummary();

  successMessage.textContent =
    "Tagasiside on edukalt salvestatud!";

  form.reset();
});

renderSummary();