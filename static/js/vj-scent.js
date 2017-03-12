SCENT_STATUS_URL = "/status";

console.log("Start");
var socket = io.connect('http://' + document.domain + ':' + location.port + '/scent');

socket.on('connect', function(msg) {
    console.log('[INFO] Socket connected.');
    fetchState();
});

socket.on('disconnect', function (msg) {
    console.log('[INFO] Socket disconnected');
    $.each(scentModel.availableScents, function (_, val) {
        var cb =$('#scentCheckboxes').find('#' + val);
        cb.prop('disabled', true);
    })
});

socket.on('status_changed', function(data) {
    console.log('[INFO] Status changed to');
    console.log(data);
    applyState(data);
});

function activate(scent) {
    console.log('Activating scent: ' + scent);
    socket.emit('activate', scent);
}

function deactivate(scent) {
    console.log('Deactivating scent: ' + scent);
    socket.emit('deactivate', scent);
}

function stopAll() {
    console.log('Deactivating all scents');
    socket.emit('deactivateAll');
    fetchState();
}

function handleClick(cb) {
    if (cb.checked)
        activate(cb.id);
    else
        deactivate(cb.id);
}

function applyState(data) {
    $.each(data, function(key, val) {
        var cb =$('#scentCheckboxes').find('#' + key);
        cb.prop('checked', val);
        cb.prop('disabled', false);
    });
}

function fetchState() {
    $.ajax({
        url: SCENT_STATUS_URL,
        success: applyState
    });
}

var scentModel = {
    availableScents: [0, 1, 2, 3, 4, 5]
};
ko.applyBindings(scentModel);
