from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json
from .chess.chess_game import *
from .models import Game

# Create your views here.

def home(request):
    return render(request, 'home.html')

def game(request, id):
    context = {'game_id': id}
    return render(request, 'game.html', context)

def new_game(request):
    game = Game()
    game.save()
    return redirect(f'/game/{game.id}')

def load_game(request): # loads game of given id
    if request.method == 'POST':
        data = json.loads(request.body)
        game_id = data['gameId']
        game = get_object_or_404(Game, pk=game_id)
        print(game.fen())
        return JsonResponse({
            'game_id': game.id,
            'board': game.fen()
        })

def move(request, id): # handles all game-logic
    if request.method == 'POST':
        data = json.loads(request.body)
        
        if data['requestType'] == 'onDragStart':      
            where_from = data['from']
            piece = data['piece']
            game = get_object_or_404(Game, pk=id)
            return JsonResponse({
                'moves': get_moves(where_from, game.board, piece)
            })
        elif data['requestType'] == 'onDrop':
            game = get_object_or_404(Game, pk=id)
            game.board = fen_to_64bit(data['board'])
            print(game.board)
            game.save()
            return JsonResponse({
                'winner': None,
                'board': game.fen()
            })
        else:
            pass
    else:
        return JsonResponse({
            'player': 'white'
        })

