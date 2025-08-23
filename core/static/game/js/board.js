function onDrop (source, target, piece, newPos, oldPos, orientation) {
    fetch('game/move', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ from: source, to: target })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            if (!data.valid) {
                return 'snapback';
            }
        });
    return 'snapback'
}

var config = {
    draggable: true,
    position: 'start',
    onDrop: onDrop,
    pieceTheme: '/static/img/chesspieces/wikipedia/{piece}.png'
}

var board = Chessboard('board', config)

