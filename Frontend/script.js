fetch('data/tennis-odds.json')
  .then(res => res.json())
  .then(data => {
    const tbody = document.querySelector('tbody');
    data.forEach(row => {
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td>${row.match}</td>
        <td>${row.player1}</td>
        <td>${row.player2}</td>
        <td>${row.book}</td>
        <td>${row.odds_p1}</td>
        <td>${row.odds_p2}</td>
      `;
      tbody.appendChild(tr);
    });
  });