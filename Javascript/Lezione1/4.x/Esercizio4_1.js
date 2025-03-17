let tabellinaForWhile = (numId, resultId) => {
    const tabellina = parseInt(document.getElementById(numId).value);
    if (tabellina < 1 || tabellina > 10 || isNaN(tabellina)) {
        throw new TypeError("Il numero deve essere fra 1 e 10.")
    }
    
    let tab_html = "<table><tr><th>Operazione</th><th>Risultato</th></tr>";
    let i = 1

    do {
        tab_html +=
        `<tr><td>${tabellina} x ${i}</td><td>${tabellina * i}</td></tr>`
        ++i;
    } while(i < 11)
    tab_html += "</table>";

    document.getElementById(resultId).innerHTML = tab_html;
}