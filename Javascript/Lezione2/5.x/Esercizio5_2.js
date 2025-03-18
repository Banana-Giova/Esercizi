let weekChecker = (boolNum, resultId) => {
    let output;
    switch(boolNum) {
        case 0:
            output = "Peccato, non posso indovinare questo giorno.";
            break;
        case 1:
            output = "Lunedì"
            break;
        case 2:
            output = "Martedì"
            break;
        case 3:
            output = "Mercoledì"
            break;
        case 4:
            output = "Giovedì"
            break;
        case 5:
            output = "Venerdì"
            break;
        case 6:
            output = "Sabato"
            break;
        case 7:
            output = "Domenica"
            break;
        default:
            output = "Errore interno."
            break;
    }
    console.log(output);
    document.getElementById(resultId).innerText =
        output
}

let rangeChecker = (numId, resultId) => {

    let num = parseInt(document.getElementById(numId).value);
    if (num > 0 && num < 8) {
        weekChecker(num, resultId)
    } else {
        weekChecker(0, resultId)
    }
}