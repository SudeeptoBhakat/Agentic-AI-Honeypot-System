function handoff(){

    fetch("http://127.0.0.1:8000/handoff",{
        method:"POST"
    })
    .then(res => res.json())
    .then(data=>{
        console.log(data);
        window.location.href="chat.html";
    })
    .catch(err=>{
        alert("Backend not running!");
    });
}
