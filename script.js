
// Function to handle the submit of the form itself
async function handleSubmit() {
  const inputData = document.getElementById("inputData").value;
  console.log(inputData);

  try {
    const response = await fetch("/api/data", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ data: inputData }),
    });

    const result = await response.json();
    document.getElementById(
      "response"
    ).innerText = `Received: ${result.received.data}`;
  } catch (error) {
    document.getElementById("response").innerText = `Error: ${error.message}`;
  }
}
