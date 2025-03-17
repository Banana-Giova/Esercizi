let calcSumError = (resultId) => {

    var a = prompt("Inserisci il primo numero");
    var b = prompt("Inserisci il secondo numero");
    /*
      I numeri mandati in input col prompt non hanno problemi,
      tuttavia fare "a+b" concatena due stringhe, anziché sommare
      due numeri. Per sommare i due numeri mandati in input
      è necessario usare Number() per castare il tipo numerico
      sulla variabile.
    */

    console.log(Number(a)+Number(b));
    document.getElementById(resultId).innerText = Number(a)+Number(b);
}