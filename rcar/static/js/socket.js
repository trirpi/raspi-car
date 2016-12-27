/**
 * Created by Tristan Trouwen on 27/12/16.
 */

$(document).ready(function() {

    var socket = io.connect('http://192.168.1.83');
    socket.on('connect', function () {
        socket.emit('my event', {data: 'I\'m connected!'});
    });

    $("#left").click(function () {
       socket.emit('message', {data: 'left'});
    });
    $("#right").click(function () {
        socket.emit('message', {data: 'right'});
    });
    $("#up").click(function () {
        socket.emit('message', {data: 'forward'});
    });
    $("#down").click(function () {
        socket.emit('message', {data: 'backward'});
    });
    $("#stop").click(function () {
        socket.emit('message', {data: 'stop'});
    });
});