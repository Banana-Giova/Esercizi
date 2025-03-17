let a2 = 2;
let x2 = 1 + (a2 *= 2);

let showAXResults = (id) => {
    console.log
        (`a = ${a2}, x = ${x2}; Spiegazione:\n
         'a' viene dichiarato con il valore di 2\n
         quando viene dichiarato 'x' il valore di 'a' è modificato,\n
         dunque, modificato tale valore, viene assegnata 'x',\n
         che ritiene le modifiche al valore di 'a'!`);
    document.getElementById(id).innerText = 
        `a = ${a2}, x = ${x2}; Spiegazione:\n
         'a' viene dichiarato con il valore di 2\n
         quando viene dichiarato 'x' il valore di 'a' è modificato,\n
         dunque, modificato tale valore, viene assegnata 'x',\n
         che ritiene le modifiche al valore di 'a'!`;
};