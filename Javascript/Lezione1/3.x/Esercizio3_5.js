let a1 = 1, b = 1;
let c = ++a1; // 2
let d = b++; // 1
/*
  c = 2, perché prima incrementa il valore e poi lo assegna
  d = 1, perché prima assegna il valore poi lo incrementa
*/

let showCDResults = (id) => {
    console.log
        (`c = ${c}, d = ${d}; Spiegazione:\n
          c = 2, perché prima incrementa il valore e poi lo assegna\n
          d = 1, perché prima assegna il valore poi lo incrementa`);
    document.getElementById(id).innerText = 
        `c = ${c}, d = ${d}; Spiegazione:\n
         c = 2, perché prima incrementa il valore e poi lo assegna\n
         d = 1, perché prima assegna il valore poi lo incrementa`;
};