const checkBtn = document.getElementById("check-btn");
const palindromeInput = document.getElementById("text-input");

function checkPalindrome() {
    let rawInput = palindromeInput.value;
    let cleanedInput = cleanInput(rawInput);

    if (cleanedInput === "") {
        alert("Please input a value");
        return;
    }

    let reversed = cleanedInput.split("").reverse().join("");
    let resultMsg = (cleanedInput === reversed) 
        ? `"${rawInput}" is a palindrome!` 
        : `"${rawInput}" is not a palindrome.`;

    document.getElementById("result").textContent = resultMsg; // Display result
}

function cleanInput(input) {
    return input.toLowerCase().replace(/[^a-z0-9]/g, ""); 
}

checkBtn.addEventListener("click", checkPalindrome);

// need to unhide the result 