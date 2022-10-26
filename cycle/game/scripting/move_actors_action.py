from game.scripting.action import Action

class MoveActorsAction(Action):
    """ Moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the game actors.
    """

    def execute(self, cast, script):
        """Executes the move actors method.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()



    
