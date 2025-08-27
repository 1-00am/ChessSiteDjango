from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json
from .chess.chess_game import *
from .chess.board_operations import fen_to_64bit
from .models import GamePvsAI

# Create your views here.

def home(request):
    return render(request, 'home.html')

def game(request, id):
    context = {'game_id': id}
    return render(request, 'game.html', context)

def new_game(request):
    if request.method == 'POST':
        color = request.POST.get('color')
    game = GamePvsAI()
    game.player_color = color
    game.save()
    return redirect(f'/game/{game.id}')

def load_game(request): # loads game of id given in request
    if request.method == 'POST':
        data = json.loads(request.body)
        game_id = data['gameId']
        game = get_object_or_404(GamePvsAI, pk=game_id)
        return JsonResponse({
            'game_id': game.id,
            'board': game.fen(),
            'player_color': game.player_color,
        })

def move(request, id): # handles all game-logic
    if request.method == 'POST':
        data = json.loads(request.body)
        game = get_object_or_404(GamePvsAI, pk=id)
        
        if data['requestType'] == 'onDragStart':      
            where_from = data['from']
            piece = data['piece']
            last_move = (game.last_move_from, game.last_move_to) if game.last_move_from else None
            moves, sp_moves = get_moves(where_from, game.board, piece, last_move)
            return JsonResponse({
                'moves': moves,
                'sp_moves': sp_moves
            })
        elif data['requestType'] == 'onDrop':           
            game.board = fen_to_64bit(data['board'])
            game.last_move_from = data['from']
            game.last_move_to = data['to']
            game.save()
            return JsonResponse({
                'winner': None,
            })
        else:
            # should not go here for now
            pass
    else:
        # should not go here for now
        return JsonResponse({
        })

