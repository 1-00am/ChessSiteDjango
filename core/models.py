from django.db import models

# Create your models here.

class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    board = models.CharField(max_length=64, default='rnbqkbnrppppppppxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxPPPPPPPPRNBQKBNR')

    def fen(self): # return board in short-fen format
        brd = self.board
        fen = ""
        for i in range(64):
            if brd[i] == "x":
                if fen[-1].isdigit():
                    fen = fen[:-1] + str(int(fen[-1])+1)
                else:
                    fen += "1"
            else:
                fen += brd[i]
            if (i+1)%8 == 0 and i != 63:
                fen += "/"
        return fen