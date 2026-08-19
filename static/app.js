/* =========================================
   ELEMENTS
========================================= */

const review =
  document.getElementById("review");

const counter =
  document.getElementById("counter");

const analyzeBtn =
  document.getElementById("analyzeBtn");

const clearBtn =
  document.getElementById("clearBtn");

const emptyState =
  document.getElementById("emptyState");

const resultContent =
  document.getElementById("resultContent");

const errorBox =
  document.getElementById("errorBox");

const resultTitle =
  document.getElementById("resultTitle");

const statusDot =
  document.getElementById("statusDot");

const sentiment =
  document.getElementById("sentiment");

const sentimentIcon =
  document.getElementById("sentimentIcon");

const confidence =
  document.getElementById("confidence");

const meterFill =
  document.getElementById("meterFill");

const themeToggle =
  document.getElementById("themeToggle");


/* =========================================
   CHARACTER COUNTER
========================================= */

function updateCounter() {

  const currentLength =
    review.value.length;

  counter.textContent =
    `${currentLength.toLocaleString()} / 12,000`;
}


/*
   IMPORTANT:
   Update counter whenever the user
   types, pastes, cuts, or edits text.
*/

review.addEventListener(
  "input",
  updateCounter
);


/* =========================================
   ERROR
========================================= */

function showError(message) {

  errorBox.textContent =
    message;

  errorBox.classList.remove(
    "hidden"
  );

  resultContent.classList.add(
    "hidden"
  );

  emptyState.classList.add(
    "hidden"
  );

  resultTitle.textContent =
    "Something went wrong";

  statusDot.classList.remove(
    "active"
  );
}


/* =========================================
   RESET RESULT
========================================= */

function resetResult() {

  errorBox.classList.add(
    "hidden"
  );

  resultContent.classList.add(
    "hidden"
  );

  emptyState.classList.remove(
    "hidden"
  );

  resultTitle.textContent =
    "Ready when you are";

  statusDot.classList.remove(
    "active"
  );
}


/* =========================================
   EXAMPLE REVIEWS
========================================= */

document
  .querySelectorAll(".example")
  .forEach(button => {

    button.addEventListener(
      "click",
      () => {

        review.value =
          button.dataset.review;

        updateCounter();

        resetResult();

        review.focus();
      }
    );

  });


/* =========================================
   CLEAR BUTTON
========================================= */

clearBtn.addEventListener(
  "click",
  () => {

    review.value = "";

    updateCounter();

    resetResult();

    review.focus();
  }
);


/* =========================================
   ANALYZE SENTIMENT
========================================= */

analyzeBtn.addEventListener(
  "click",
  async () => {

    const text =
      review.value.trim();


    /* Check empty review */

    if (!text) {

      showError(
        "Please enter a movie review before analyzing it."
      );

      review.focus();

      return;
    }


    /* Loading state */

    analyzeBtn.disabled = true;

    analyzeBtn.classList.add(
      "loading"
    );

    errorBox.classList.add(
      "hidden"
    );

    resultTitle.textContent =
      "Analyzing review…";

    statusDot.classList.add(
      "active"
    );


    try {

      const response =
        await fetch(
          "/predict",
          {
            method: "POST",

            headers: {
              "Content-Type":
                "application/json"
            },

            body:
              JSON.stringify({
                review: text
              })
          }
        );


      const data =
        await response.json();


      /* Check Flask response */

      if (!response.ok) {

        throw new Error(
          data.error ||
          "Prediction failed."
        );
      }


      /* Determine sentiment */

      const isPositive =
        data.sentiment === "Positive";


      /* Show result */

      emptyState.classList.add(
        "hidden"
      );

      resultContent.classList.remove(
        "hidden"
      );


      resultTitle.textContent =
        "Analysis complete";


      /* Sentiment */

      sentiment.textContent =
        data.sentiment;


      /* Confidence */

      confidence.textContent =
        `${data.confidence.toFixed(2)}%`;


      /* Confidence progress bar */

      meterFill.style.width =
        `${Math.min(
          data.confidence,
          100
        )}%`;


      /* Sentiment icon */

      sentimentIcon.textContent =
        isPositive
          ? "✓"
          : "×";


      sentimentIcon.classList.toggle(
        "negative",
        !isPositive
      );

    }


    catch (error) {

      console.error(
        "Prediction error:",
        error
      );

      showError(
        error.message
      );
    }


    finally {

      analyzeBtn.disabled = false;

      analyzeBtn.classList.remove(
        "loading"
      );
    }

  }
);


/* =========================================
   CTRL + ENTER
========================================= */

review.addEventListener(
  "keydown",
  event => {

    if (
      (event.ctrlKey ||
        event.metaKey) &&
      event.key === "Enter"
    ) {

      analyzeBtn.click();
    }

  }
);


/* =========================================
   DARK / BRIGHT MODE
========================================= */

function setTheme(theme) {

  if (theme === "light") {

    document.body.classList.add(
      "light-mode"
    );

    themeToggle.title =
      "Switch to dark mode";

    localStorage.setItem(
      "movieMindTheme",
      "light"
    );

  }

  else {

    document.body.classList.remove(
      "light-mode"
    );

    themeToggle.title =
      "Switch to bright mode";

    localStorage.setItem(
      "movieMindTheme",
      "dark"
    );
  }
}


/* =========================================
   THEME TOGGLE
========================================= */

themeToggle.addEventListener(
  "click",
  () => {

    const isLight =
      document.body.classList.contains(
        "light-mode"
      );


    setTheme(
      isLight
        ? "dark"
        : "light"
    );
  }
);


/* =========================================
   LOAD SAVED THEME
========================================= */

const savedTheme =
  localStorage.getItem(
    "movieMindTheme"
  );


if (savedTheme === "light") {

  setTheme("light");

}

else {

  setTheme("dark");
}


/* =========================================
   INITIALIZE
========================================= */

updateCounter();