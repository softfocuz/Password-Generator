const button = document.querySelector("#generate-btn");
const resultScreen = document.querySelector(".result_screen");

button.addEventListener("click", async () => {
    try {
        const response = await fetch("/password");
        const data = await response.json();
        resultScreen.innerText = data.result;
    } catch (error) {
        console.error("Error:", error);
        resultScreen.innerText = "Failed to fetch password!";
    }
});
