let tabellineMultiple = (tabId, resultId) => {
    let tab_html = "<table>";

    switch(Number(tabId)) {
        case 42: 
        {
            tab_html += "<tr><th>Numero</th></tr>";
            let i = 0;
            do {
                tab_html +=
                `<tr><td>${i++}</td></tr>`
            } while(i < 11)
        }
        break;
        
        case 43:
        {
            tab_html += "<tr><th>Numero</th></tr>";
            let i = 5;
            do {
                tab_html +=
                `<tr><td>${i++}</td></tr>`
            } while(i < 16)
        }
        break;
        
        case 44:
        {
            tab_html += "<tr><th>Numero</th></tr>";
            let i = 0;
            do {
                tab_html +=
                `<tr><td>${i}</td></tr>`
                i += 2;
            } while(i < 21)
        }
        break;

        case 45:
        {
            tab_html += "<tr><th>Numero</th></tr>";
            let i = 0;
            do {
                tab_html +=
                `<tr><td>${i}</td></tr>`
                i += 4;
            } while(i < 41)
        }
        break;

        default:
            throw new ReferenceError("No such operation. Valid operations: 42, 43, 44, 45.");
    }
    tab_html += "</table>";
    document.getElementById(resultId).innerHTML = tab_html;
}