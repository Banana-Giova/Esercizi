const curr_anno = 2025;

let calcAging = (intId, resultId) => {

    const anno_nascita = parseFloat(document.getElementById(intId).value);
    
    const curr_age = curr_anno - anno_nascita;
    const hundred = 100 - curr_age;

    console.log
        (`Se non hai compiuto gli anni, ne hai ${curr_age-1},\nSennò hai ${curr_age} anni!\nE fra ${hundred} anni ne farai 100!`);
    document.getElementById(resultId).innerText = 
        `Se non hai compiuto gli anni, ne hai ${curr_age-1},\nSennò hai ${curr_age} anni!\nE fra ${hundred} anni ne farai 100!`;
}