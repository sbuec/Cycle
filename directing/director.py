

class Director:
    def __init__(self, keyboard_service, vido_service):
        self._keyboard_service = keyboard_service
        self._video_service = vido_service



class DirectorRFK:
    # A person who directs the game. 


    def __init__(self, keyboard_service, video_service):
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        # Starts the game using the given cast. Runs the main game loop.
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        # Gets directional input from the keyboard and applies it to the robot.
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        #Updates the robot's position and resolves any collisions with artifacts.
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()):
                message = artifact.get_message()
                banner.set_text(message)    
        
    def _do_outputs(self, cast):
        #Draws the actors on the screen.
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()