let hrBall = (resultId) => {
    let hr_count = 1;
    let result_html = `
    <h3>Prisma di Mazinga</h3>
    <hr style="width: 1%; height: 2px; background-color: white;">

    `;
    let anti_html = `

    <hr style="width: 1%; height: 2px; background-color: white;">        
    `;

    do {
        result_html +=
        `
        <hr style="width: ${hr_count*5}%; height: 2px; background-color: white;">

        `;
        anti_html =
        `

        <hr style="width: ${hr_count*5}%; height: 2px; background-color: white;">        
        ` + anti_html;
        ++hr_count;
    } while (hr_count < 19);
    result_html +=
    `
    <hr style="width: ${hr_count*5}%; height: 2px; background-color: white;">

    `;
    result_html += anti_html;
    document.getElementById(resultId).innerHTML = result_html;
}