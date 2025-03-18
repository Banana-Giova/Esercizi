let conteggio;
let rng;
let local_id;
let bigSmall;

let checkIfWin = (numId) => {
    let num = parseInt(document.getElementById(numId).value);

    if (num == rng) {
        theGame('win');
    } else if (isNaN(num)) {
        theGame('error');
    } else {
        ++conteggio;
        if (num < rng) {
            bigSmall = `Riprova! Il numero da indovinare è più grande del tuo!`;
        } else {
            bigSmall = `Riprova! Il numero da indovinare è più piccolo del tuo!`;
        }
        theGame('fail');
    }
}

let theGame = (status) => {
    if (status == 'new') {
        conteggio = 0;
        rng = Math.floor(Math.random() * 101);
        
        document.getElementById(local_id).innerHTML = 
        `
        <h4>Prova ad indovinare a quale numero sto pensando!</h4>
        <h5>Indizio: E' un numero intero fra 0 e 100!</h5>
        <form id="frm3" action="/action_page.php">
            <div class="form-group">
                <label for="tentativo"></label>
                <input type="number" id="tentativo" name="tentativo" min="0" max="100" placeholder="Prova ad indovinare!">
            </div>
            <div class="counter">
                <h4>Tentativi:</h4><p id="count">${conteggio}</p>
            </div>
            <br>
            <input type="button" onclick="checkIfWin('tentativo')" value="Controlla">
        </form>
        <hr><button type="button" onclick="theGame('new', ${local_id})">Nuovo gioco</button>
        `;
    } else if (status == 'fail') {
        console.log(bigSmall);
        document.getElementById(local_id).innerHTML = 
        `
        <h4>${bigSmall}</h4>
        <h5>Indizio: E' un numero intero fra 0 e 100!</h5>
        <form id="frm3" action="/action_page.php">
            <div class="form-group">
                <label for="tentativo"></label>
                <input type="number" id="tentativo" name="tentativo" min="0" max="100" placeholder="Ritenta!">
            </div>
            <div class="counter">
                <h4>Tentativi:</h4><p id="count">${conteggio}</p>
            </div>
            <br>
            <input type="button" onclick="checkIfWin('tentativo')" value="Controlla">
        </form>
        <hr><button type="button" onclick="theGame('new', ${local_id})">Nuovo gioco</button>
        `;
    } else if (status == 'win') {
        console.log(`Bravo! Il numero era proprio ${rng}!`);
        document.getElementById(local_id).innerHTML = 
        `
        <h3>Bravo! Il numero era proprio ${rng}!</h3>
        <h4>Lo hai azzeccato in ${conteggio} tentativi! Vuoi giocare ancora?</h4>
        <hr><button type="button" onclick="theGame('new', ${local_id})">Nuovo gioco</button>
        `;
    } else if (status == 'error') {
        document.getElementById(local_id).innerHTML = 
        `
        <h4>Quello che hai inserito non è un numero valido! Riprova!</h4>
        <h5>Indizio: E' un numero intero fra 0 e 100!</h5>
        <form id="frm3" action="/action_page.php">
            <div class="form-group">
                <label for="tentativo"></label>
                <input type="number" id="tentativo" name="tentativo" min="0" max="100" placeholder="Inserisci un numero intero valido!">
            </div>
            <div class="counter">
                <h4>Tentativi:</h4><p id="count">${conteggio}</p>
            </div>
            <br>
            <input type="button" onclick="checkIfWin('tentativo')" value="Controlla">
        </form>
        <hr><button type="button" onclick="theGame('new', ${local_id})">Nuovo gioco</button>
        `;
    }
}

let newGame = (resultId) => {
    local_id = resultId;
    theGame('new');
}