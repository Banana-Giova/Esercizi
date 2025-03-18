let jobP1 = (resultId) => {
    return new Promise((resolve, reject) => {
        
        setTimeout(() => {
            resolve(document.getElementById(resultId).innerHTML= 
            `<div class="box"> Ciao Mondo</div>`)
        }, 2000);
    });
}