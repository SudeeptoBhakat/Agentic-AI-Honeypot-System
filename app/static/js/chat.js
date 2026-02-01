function appendMessage(sender, text){

    let div = document.createElement("div");

    div.classList.add("msg");

    if(sender === "You"){
        div.classList.add("user");
    }else{
        div.classList.add("agent");
    }

    div.innerHTML = `<b>${sender}:</b> ${text}`;

    document.getElementById("messages").appendChild(div);
}


function sendMessage(){

    let input = document.getElementById("msg");
    let message = input.value;

    if(!message) return;

    appendMessage("You", message);

    input.value="";

    fetch("http://127.0.0.1:8000/chat",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            message:message
        })
    })
    .then(res => res.json())
    .then(data=>{

        // Fake typing delay for realism
        setTimeout(()=>{
            appendMessage("Rahul Sharma", data.reply);
        },1500);

    });
}
