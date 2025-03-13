let numero = 100;

let mostraNumero = () => {
    console.log(numero);
    document.getElementById("Esercizio_2").innerText = `Valore del numero: ${numero}`;
};

let cambiaNumero = (numero) => {
    numero = numero - 70;
    mostraNumero(numero);
};