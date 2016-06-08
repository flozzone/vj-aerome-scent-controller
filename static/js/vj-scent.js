console.log("Start");
var socket = io.connect('http://' + document.domain + ':' + location.port + '/scent');

socket.on('connect', function(msg) {
    console.log('[INFO] Socket connected.');
});

function activate() {
    scent = $('#scent').val();
    console.log('Activating scent: ' + scent);
    socket.emit('activate', scent);
}

function deactivate() {
    scent = $('#scent').val();
    console.log('Deactivating scent: ' + scent);
    socket.emit('deactivate', scent);
}