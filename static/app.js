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
   CLEAR
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


    if (!text) {

      showError(
        "Please enter a movie review before analyzing it."
      );

      review.focus();

      return;
    }


    /* Loading */

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
                "application/json",

              "Accept":
                "application/json"
            },

            body:
              JSON.stringify({
                review: text
              })
          }
        );


      /*
       * IMPORTANT:
       * Don't directly call response.json().
       *
       * First read the response as text.
       */

      const rawResponse =
        await response.text();


      console.log(
        "HTTP Status:",
        response.status
      );

      console.log(
        "Server Response:",
        rawResponse
      );


      /*
       * Empty response
       */

      if (!rawResponse.trim()) {

        throw new Error(
          `Server returned an empty response (HTTP ${response.status}). Check the Render logs for the /predict error.`
        );
      }


      /*
       * Convert response to JSON
       */

      let data;

      try {

        data =
          JSON.parse(
            rawResponse
          );

      }

      catch (jsonError) {

        console.error(
          "Invalid JSON:",
          rawResponse
        );

        throw new Error(
          `Server returned a non-JSON response (HTTP ${response.status}). Check the Render logs.`
        );
      }


      /*
       * Flask returned an error
       */

      if (!response.ok) {

        throw new Error(
          data.error ||
          "Prediction failed on the server."
        );
      }


      /*
       * Validate prediction
       */

      if (
        !data.sentiment ||
        data.confidence === undefined
      ) {

        throw new Error(
          "Invalid prediction response from Flask."
        );
      }


      /* =================================
         SHOW RESULT
      ================================= */

      const isPositive =
        data.sentiment === "Positive";


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

      const confidenceValue =
        Number(
          data.confidence
        );


      confidence.textContent =
        `${confidenceValue.toFixed(2)}%`;


      /* Progress */

      meterFill.style.width =
        `${Math.min(
          confidenceValue,
          100
        )}%`;


      /* Icon */

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

      analyzeBtn.disabled =
        false;

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
   THEME
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
   LOAD THEME
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