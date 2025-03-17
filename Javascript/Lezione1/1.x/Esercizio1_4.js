let bebes = `50`;

let showBebes = (id) => {
    console.log
        (`Valore della variabile: ${bebes}, è un valore numerico? ${!isNaN(bebes)}`);
    document.getElementById(id).innerText = 
        `Valore della variabile: ${bebes}, è un valore numerico? ${!isNaN(bebes)}`;
}

let convertBebes = (id) => {
    bebes = Number(bebes);
    showBebes(id);
}