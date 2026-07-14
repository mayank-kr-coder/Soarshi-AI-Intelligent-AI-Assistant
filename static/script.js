
const sidebar = document.getElementById("sidebar");
const menuBtn = document.getElementById("menu-btn");

const sendBtn = document.getElementById("send-btn");
const inputBox = document.getElementById("message-input");

const chatContainer = document.getElementById("chat-container");

console.log("JS Loaded");

// Sidebar toggle
menuBtn.onclick = () => {

    sidebar.classList.add("active");

};
const closeBtn = document.getElementById("close-sidebar");

closeBtn.onclick = () => {

    sidebar.classList.remove("active");

};

// clear chat button 
const clearBtn = document.getElementById("clearBtn");

clearBtn.onclick = async () => {

    chatContainer.innerHTML = "";

    await fetch("/clear_chat",{
        method:"POST"
    });

}


// Add message to screen
function addMessage(text, sender){

    const messageDiv = document.createElement("div");

    messageDiv.classList.add("message");
    messageDiv.classList.add(sender);


    const bubble = document.createElement("div");

    bubble.classList.add("bubble");


    if(sender === "user"){

        bubble.innerHTML = "👤 " + text;

    }

    else{

        bubble.innerHTML = "🤖 " + text;

    }


    messageDiv.appendChild(bubble);

    chatContainer.appendChild(messageDiv);


    chatContainer.scrollTop = chatContainer.scrollHeight;

}



// Send message to Flask

async function sendMessage(){

    let message = inputBox.value.trim();

    if(message === "")
        return;

    addMessage(message,"user");

    inputBox.value = "";

    // Disable send button while processing
    sendBtn.disabled = true;

    // Loading message
    const loadingId = "loading-" + Date.now();

    const loadingDiv = document.createElement("div");

    loadingDiv.classList.add("message","bot");
    loadingDiv.id = loadingId;

    loadingDiv.innerHTML =
   `<div class="bubble">⚡ Soarshi AI is thinking...</div>`;

    chatContainer.appendChild(loadingDiv);

    chatContainer.scrollTop = chatContainer.scrollHeight;

    // Render cold-start warning
    const wakeupTimer = setTimeout(() => {

        const loading = document.getElementById(loadingId);

        if(loading){

            loading.querySelector(".bubble").innerHTML =
            "⚡ Jarvis is waking up on Render. This may take up to 60 seconds.";

        }

    },10000);

    try{

        const response = await fetch("/chat",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({

                message:message

            })

        });
        

        const data = await response.json();

        // Remove loading message
        document.getElementById(loadingId)?.remove();

        clearTimeout(wakeupTimer);

        addMessage(data.response,"bot");

        if (data.action === "open_url") {
            window.open(data.url, "_blank");
        }

        if(data.audio_file){

            let audio = new Audio("/static/" + data.audio_file);

            audio.play();
        }

    }

    catch(error){

        document.getElementById(loadingId)?.remove();

        clearTimeout(wakeupTimer);

        addMessage("Something went wrong.","bot");

        console.log(error);

    }

    finally{

        sendBtn.disabled = false;

    }

}



// Send button
sendBtn.onclick = sendMessage;



// Enter key
inputBox.addEventListener("keypress",function(event){

    if(event.key==="Enter"){

        sendMessage();

    }

});

    // voice button

const voiceBtn = document.getElementById("voice-btn");

const statusText = document.getElementById("listening-status");
const statusDiv = document.getElementById("jarvis-status");

const SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();

recognition.lang = "en-IN";
recognition.interimResults = false;
recognition.maxAlternatives = 1;
// recognition.onstart = () => {
//     statusDiv.innerHTML = "🎤 Listening...";
// };


voiceBtn.onclick = () => {

    voiceBtn.classList.add("recording");
    statusText.style.display = "block";

    recognition.start();

};


recognition.onresult = function(event){

    voiceBtn.classList.remove("recording");
    statusText.style.display = "none";

    const transcript = event.results[0][0].transcript;

    inputBox.value = transcript;

    sendMessage();

};


recognition.onerror = function(event){

    voiceBtn.classList.remove("recording");
    statusText.style.display = "none";

    console.log(event.error);

};


// Voice Deletion

async function clearChat(){

    await fetch("/clear_chat",{
        method:"POST"
    });

    chatContainer.innerHTML = "";
}

window.addEventListener("beforeunload", () => {
    navigator.sendBeacon("/clear_chat");
});
