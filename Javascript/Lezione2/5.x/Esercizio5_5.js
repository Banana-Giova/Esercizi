let asteriskStorm = (resultId) => {
    let aster_count = 10;
    let result_html = `<br>
    ★
    `;

    do {
        result_html +=
        `
        <p>${"*".repeat(aster_count)}</p>

        `;
        ++aster_count;
    } while (aster_count < 31);
    document.getElementById(resultId).innerHTML = result_html;
}