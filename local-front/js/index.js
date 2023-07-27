// index.html

function logout() {
  document.cookie = `loginToken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
}

function askQuestion() {
  const questionInput = document.getElementById("question");
  const question = questionInput.value;
  if (question) {
    fetch("http://127.0.0.1:8000/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ prompt: question }),
    })
      .then((response) => response.json())
      .then((data) => {
        // Display AI's response on the page
        const responseDiv = document.getElementById("response");
        responseDiv.innerText += `AI's Response: ${data[0]["response"]}\n`;
        //   console.log(data);
        //   console.log(data[0]["response"]);
        //   alert(data[0]["response"]);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
}
