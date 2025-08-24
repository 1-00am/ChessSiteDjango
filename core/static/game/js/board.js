var board = null
var $board = $('#board')
var squareClass = 'square-55d63'

function highlightSquares (squares) {
    for (let i = 0; i < squares.length; i++) {
        const square = squares[i];
        $board.find('.square-' + square).addClass('highlight-white')
    }
}

function removeHighlights (color) {
  $board.find('.' + squareClass)
    .removeClass('highlight-' + color)
}

async function getMoves(source) {
    const response = await fetch('game/move', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ from: source, board: board.fen() })
        })
    return await response.json()
}

function onDragStart (source, piece, position, orientation) {
    if ((orientation === 'white' && piece.search(/^w/) === -1) ||
        (orientation === 'black' && piece.search(/^b/) === -1)) {
        return false
    }

    getMoves(source).then(data => {
        highlightSquares(data['moves'])
    })
}

function onDrop (source, target, piece, newPos, oldPos, orientation) {
    removeHighlights("white")
}

function onGameStart () {
    return fetch('game/move', {
            method: 'GET'
        })
        .then(response => response.json())
}

async function initBoard() {
    const gameStartData = await onGameStart()

    var config = {
        draggable: true,
        position: 'start',
        orientation: gameStartData['player'],
        onDrop: onDrop,
        onDragStart: onDragStart,
        pieceTheme: '/static/img/chesspieces/wikipedia/{piece}.png'
    }

    board = Chessboard('board', config)
}

initBoard()

