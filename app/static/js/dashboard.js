fetch("http://127.0.0.1:8000/evidence")
.then(res => res.json())
.then(data=>{

    let body = document.getElementById("tableBody");

    data.forEach(item=>{

        body.innerHTML += `
        <tr>
            <td>${item.phone}</td>
            <td>${item.upi}</td>
            <td>${item.link}</td>
            <td>${item.risk}%</td>
        </tr>
        `;
    });

});
