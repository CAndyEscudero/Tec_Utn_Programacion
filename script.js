let tamañoSeleccionado = null;

const cards = document.querySelectorAll('.perro-card');
const resultado = document.getElementById('resultado');
const pesoInput = document.getElementById('peso');

cards.forEach(card => {
  card.addEventListener('click', () => {
    cards.forEach(c => c.classList.remove('selected'));
    card.classList.add('selected');
    tamañoSeleccionado = card.dataset.tamaño;
  });
});

document.getElementById('calcularBtn').addEventListener('click', () => {
  const peso = parseFloat(pesoInput.value);

  if (!tamañoSeleccionado || isNaN(peso)) {
    resultado.innerHTML = "<p style='color:red;'>Selecciona un tamaño y coloca el peso.</p>";
    return;
  }

  let gramosPorKg;
  let vacunas = [];

  switch (tamañoSeleccionado) {
    case 'pequeño':
      gramosPorKg = 30;
      vacunas = ['Rabia', 'Parvovirus', 'Moquillo'];
      break;
    case 'mediano':
      gramosPorKg = 25;
      vacunas = ['Rabia', 'Hepatitis', 'Parvovirus'];
      break;
    case 'grande':
      gramosPorKg = 20;
      vacunas = ['Rabia', 'Moquillo', 'Leptospirosis'];
      break;
  }

  const totalAlimento = gramosPorKg * peso;

  resultado.innerHTML = `
    <h3>Resultado</h3>
    <table>
      <tr>
        <th>Peso</th>
        <td>${peso} kg</td>
      </tr>
      <tr>
        <th>Alimento diario</th>
        <td>${totalAlimento} gramos</td>
      </tr>
      <tr>
        <th>Vacunas sugeridas</th>
        <td>${vacunas.join(', ')}</td>
      </tr>
    </table>
  `;
});
