from django.shortcuts import render
from django.http import JsonResponse
import json
from .chess.chess_game import is_legal_move, start_pose, get_moves

# Create your views here.

def home(request):
    return render(request, 'home.html')

def play(request):
    return render(request, 'game.html')

def move(request): # handles all game-logic
    if request.method == 'POST':
        data = json.loads(request.body)
        
        if 'from' in data.keys():      
            where_from = data['from']
            board = data['board']
            return JsonResponse({
                'moves': get_moves(where_from, board)
            })
        
        else:
            where_to = data['to']
            #board = data['board']
            board = start_pose()
            
            valid = is_legal_move(where_from, where_to, board)

            return JsonResponse({
                'valid': valid,
                'winner': None,
                'board': board
            })
    else:
        return JsonResponse({
            'player': 'white'
        })

