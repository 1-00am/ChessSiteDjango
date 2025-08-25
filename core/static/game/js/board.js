let board = null
let $board = $('#board')
let squareClass = 'square-55d63'
let legalSquares = null

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

async function getMoves(rq_type, source, piece) {
    const response = await fetch(`/game/${gameId}/move`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ 
                request_type: rq_type,
                from: source,
                board: board.fen(), 
                piece: piece
             })
        })
    return await response.json()
}

function onDragStart (source, piece, position, orientation) {
    if ((orientation === 'white' && piece.search(/^w/) === -1) ||
        (orientation === 'black' && piece.search(/^b/) === -1)) {
        return false
    }

    getMoves(rq_type="onDragStart",source, piece).then(data => {
        legalSquares = data['moves']
        highlightSquares(legalSquares)
    })
}

function onDrop (source, target, piece, newPos, oldPos, orientation) {
    removeHighlights('white')
    if (legalSquares === null) {
        return 'snapback'
    }
    if (!legalSquares.includes(target)) {
        legalSquares = null
        return 'snapback'
    }
    console.log(legalSquares, source, target)
    legalSquares = null
}

function onGameStart () {
    console.log(gameId)
    return fetch('/game/load', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ 
                gameId: gameId    
            })
        })
        .then(response => response.json())
}

async function initBoard() {
    const gameStartData = await onGameStart()

    let config = {
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

