// Yoruba words and their English translations
const wordData = [
    { yoruba: "wara", english: "milk" },
    { yoruba: "bọọlu afẹsẹgba", english: "football" },
    { yoruba: "ọmọ", english: "child" },
    { yoruba: "Ogogo melo ni o lu?", english: "What time is it?" },
    { yoruba: "O re mi", english: "I'm tired" },
    { yoruba: "Omo odun melo ni e?", english: "How old are you?" },
    { yoruba: "Ki 'ni oruko re?", english: "What is your name?" },
    { yoruba: "ebi n pa mi", english: "I'm hungry" },
    { yoruba: "Ti o ni ki awon!", english: "That's so interesting!" },
    { yoruba: "Kú isé", english: "Well done" },
    // Add more word pairs as needed
];

// Function to generate and display a random word
function generateWord() {
    const randomIndex = Math.floor(Math.random() * wordData.length);
    const randomWord = wordData[randomIndex];

    const wordElement = document.getElementById("word");
    const translationElement = document.getElementById("translation");


    wordElement.textContent = randomWord.yoruba;
    translationElement.textContent = randomWord.english;
}

// Call the function to display the initial word
generateWord();
