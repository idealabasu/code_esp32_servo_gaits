function myformsubmit(event) {
    event.preventDefault();

    var elements = form.elements;

    var data = {};
    // for (var i = 0, ii = form.length; i < ii; ++i) {
        // var input = form[i];
    for (var i = 0, element; element = elements[i++];) {        
        // var input = element;
        if (element.name) {
            // console.log("input.id: " + input.id);
            // console.log("input.value: " + input.value);
            data[element.name] = element.value;
        }
    }

    const message = JSON.stringify(data);
    console.log("message: " + message);

    ws.send(message);
    document.getElementById('amplitude').value = ''
    document.getElementById('frequency').value = ''
    // log.textContent = `Form Submitted! Timestamp: ${event.timeStamp}`;
    log.textContent = JSON.stringify(data);
}

const ws = new WebSocket(`ws://${location.host}/ws`);
console.log("ws opening");
ws.binaryType = "blob";
// Log socket opening and closing
ws.addEventListener("open", event => {console.log("Websocket connection opened");});
ws.addEventListener("close", event => {console.log("Websocket connection closed");});
ws.onmessage = function (message) {
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('msgCtn');
    if (message.data instanceof Blob) {
        reader = new FileReader();
        reader.onload = () => {
            msgDiv.innerHTML = reader.result;
            document.getElementById('messages').appendChild(msgDiv);
        };
    } else {
        console.log("message: " + message.data);
        msgDiv.innerHTML = message.data;
        document.getElementById('messages').appendChild(msgDiv);
    }
}

const ws2 = new WebSocket(`ws://${location.host}/sensordata`);
console.log("ws2 opening");
ws2.binaryType = "blob";
// Log socket opening and closing
ws2.addEventListener("open", event => {console.log("Websocket connection opened");});
ws2.addEventListener("close", event => {console.log("Websocket connection closed");});
ws2.onmessage = function (message) {
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('msgCtn');
    if (message.data instanceof Blob) {
        reader = new FileReader();
        reader.onload = () => {
            msgDiv.innerHTML = reader.result;
            document.getElementById('messages').appendChild(msgDiv);
        };
    } else {
        console.log("message: " + message.data);
        msgDiv.innerHTML = message.data;
        document.getElementById('messages').appendChild(msgDiv);
    }
}

const form = document.getElementById('msgForm');
form.addEventListener("submit", myformsubmit);