const checkBtn = document.getElementById("check-btn");
const palindromeInput = document.getElementById("text-input");
const resultDiv = document.getElementById("result"); // Get result div

function checkPalindrome() {
  let rawInput = palindromeInput.value;
  let cleanedInput = cleanInput(rawInput);

  if (cleanedInput === "") {
    alert("Please input a value");
    return;
  }

  let reversed = cleanedInput.split("").reverse().join("");
  let resultMsg =
    cleanedInput === reversed
      ? `${rawInput} is a palindrome`
      : `${rawInput} is not a palindrome`;

  resultDiv.textContent = resultMsg; // Set result message
  resultDiv.style.display = "block"; // Unhide the result div
}

function cleanInput(input) {
  return input.toLowerCase().replace(/[^a-z0-9]/g, "");
}

checkBtn.addEventListener("click", checkPalindrome);
