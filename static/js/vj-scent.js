console.log("Start");
var socket = io.connect('http://' + document.domain + ':' + location.port + '/scent');

socket.on('connect', function(msg) {
    console.log('[INFO] Socket connected.');
});

function activate(scent) {
    console.log('Activating scent: ' + scent);
    socket.emit('activate', scent);
}

function deactivate(scent) {
    console.log('Deactivating scent: ' + scent);
    socket.emit('deactivate', scent);
}

function handleClick(cb) {
    if (cb.checked)
        activate(cb.id);
    else
        deactivate(cb.id);
}

var scentModel = {
    availableScents: [0, 1, 2, 3, 4, 5]
};
ko.applyBindings(scentModel);
