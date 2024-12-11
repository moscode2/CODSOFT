// script.js
const display = document.getElementById('display');
const buttons = document.querySelectorAll('.btn');

let currentInput = '';
let previousInput = '';
let operator = null;

// Update display
function updateDisplay(value) {
  display.textContent = value || '0';
}

// Handle button clicks
buttons.forEach(button => {
  button.addEventListener('click', () => {
    const value = button.dataset.value;

    if (button.id === 'clear') {
      currentInput = '';
      previousInput = '';
      operator = null;
      updateDisplay('0');
    } else if (button.id === 'equals') {
      if (previousInput && currentInput && operator) {
        currentInput = eval(`${previousInput} ${operator} ${currentInput}`);
        previousInput = '';
        operator = null;
        updateDisplay(currentInput);
      }
    } else if (button.classList.contains('operator')) {
      if (currentInput) {
        operator = value;
        previousInput = currentInput;
        currentInput = '';
      }
    } else {
      currentInput += value;
      updateDisplay(currentInput);
    }
  });
});
