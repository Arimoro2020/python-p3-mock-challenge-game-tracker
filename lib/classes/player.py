class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
        Player.all.append(self)


    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if (type(value) == str and 2 <= len(value)<= 16):
            self._username = value
        else:
            raise ValueError("Exception")
        
    def results(self, new_result=None):
        from classes.result import Result
        if isinstance(new_result, Result):
            self._results.append(new_result)
        return [result for result in Result.all if result.player ==self] 
        
        

    
    def games_played(self, new_game=None):
        from classes.game import Game
        from classes.result import Result
        if isinstance(new_game, Game):
            self._games_played.append(new_game)
        return [result.game for result in Result.all if result.player == self] 

        
    
    def played_game(self, game):
        from classes.result import Result
        return len([result.game for result in Result.all if result.player == self and result.game == game]) >0
    
    def num_times_played(self, game):
        from classes.result import Result
        return len([result.game for result in Result.all if result.player == self and result.game == game])
       
     
    
    @classmethod
    def highest_scored(cls, game):
        pass
        
