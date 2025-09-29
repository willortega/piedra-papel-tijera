let userScore = 0;
let cpuScore = 0;

const userChoiceDiv = document.getElementById('userChoice');
const cpuChoiceDiv = document.getElementById('cpuChoice');
const messageP = document.getElementById('message');
const userScoreSpan = document.getElementById('userScore');
const cpuScoreSpan = document.getElementById('cpuScore');

function play(userChoice) {
  // Animación CPU
  const icons = [
    '<i class="fa-solid fa-hand-fist"></i>',
    '<i class="fa-solid fa-hand"></i>',
    '<i class="fa-solid fa-hand-scissors"></i>'
  ];
  let i = 0;
  const interval = setInterval(() => {
    cpuChoiceDiv.innerHTML = icons[i];
    i = (i + 1) % icons.length;
  }, 100);

  setTimeout(() => {
    clearInterval(interval);
    const cpuChoice = ['piedra', 'papel', 'tijera'][Math.floor(Math.random()*3)];

    showResult(userChoice, cpuChoice);
  }, 1000);

  // Mostrar jugada del usuario
  if(userChoice === 'piedra') userChoiceDiv.innerHTML = '<i class="fa-solid fa-hand-fist"></i>';
  if(userChoice === 'papel') userChoiceDiv.innerHTML = '<i class="fa-solid fa-hand"></i>';
  if(userChoice === 'tijera') userChoiceDiv.innerHTML = '<i class="fa-solid fa-hand-scissors"></i>';
}

function showResult(userChoice, cpuChoice) {
  if(cpuChoice === 'piedra') cpuChoiceDiv.innerHTML = '<i class="fa-solid fa-hand-fist"></i>';
  if(cpuChoice === 'papel') cpuChoiceDiv.innerHTML = '<i class="fa-solid fa-hand"></i>';
  if(cpuChoice === 'tijera') cpuChoiceDiv.innerHTML = '<i class="fa-solid fa-hand-scissors"></i>';

  if(userChoice === cpuChoice){
    messageP.textContent = '¡Empate!';
  } else if(
    (userChoice === 'piedra' && cpuChoice === 'tijera') ||
    (userChoice === 'papel' && cpuChoice === 'piedra') ||
    (userChoice === 'tijera' && cpuChoice === 'papel')
  ){
    messageP.textContent = '¡Ganaste! 🎉';
    userScore++;
  } else {
    messageP.textContent = 'Perdiste 😢';
    cpuScore++;
  }
  userScoreSpan.textContent = userScore;
  cpuScoreSpan.textContent = cpuScore;
}

function resetGame() {
  userScore = 0;
  cpuScore = 0;
  userScoreSpan.textContent = 0;
  cpuScoreSpan.textContent = 0;
  userChoiceDiv.innerHTML = '';
  cpuChoiceDiv.innerHTML = '';
  messageP.textContent = '';
}
