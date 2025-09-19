from django.db import models

# Create your models here.

class GamePvsAI(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    board = models.CharField(max_length=64, default='rnbqkbnrppppppppxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxPPPPPPPPRNBQKBNR')
    player_color = models.CharField(max_length=5, default='white')
    move_count = models.IntegerField(default=1) #counts white move + black response as 2 separate moves
    last_move_from = models.CharField(max_length=2, null=True, blank=True, default=None)
    last_move_to = models.CharField(max_length=2, null=True, blank=True, default=None)
    castle_lw = models.BooleanField(default=True) # information about castling availability 
    castle_sw = models.BooleanField(default=True) # l/s means long/short
    castle_lb = models.BooleanField(default=True) # w/b means white/black
    castle_sb = models.BooleanField(default=True)
    king_w = models.IntegerField(default=60)
    king_b = models.IntegerField(default=4)

    def fen(self): # return board in short-fen format
        brd = self.board
        fen = ''
        for i in range(64):
            if brd[i] == 'x':
                if fen and fen[-1].isdigit():
                    fen = fen[:-1] + str(int(fen[-1])+1)
                else:
                    fen += '1'
            else:
                fen += brd[i]
            if (i+1)%8 == 0 and i != 63:
                fen += '/'
        return fen