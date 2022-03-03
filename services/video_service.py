import pyray as pr


class VideoService:
    def __init__(self, caption, width, height, cell_size, frame_rate, debug = False):
        self._caption = caption
        self._width = width
        self._height = height
        self._cell_size = cell_size
        self._frame_rate = frame_rate
        self._debug = debug


    def close_window(self):
        pr.close_window()

    def clear_buffer(self):
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
        if self._debug == True:
            self._draw_grid()

    def draw_actor(self, actor):
        text = actor.get_text()
        x = actor.get_position.get_x()
        y = actor.get_position.get_y()
        font_size = actor.get_font_size()
        color = actor.get_color.to_tuple()
        pr.draw_text(text, x, y, font_size, color)

    def draw_actors(self, actors):
        for actor in actors:
            self.draw_actor(actor)

    def flush_buffer(self):
        pr.end_drawing()

    def get_cell_size(self):
        return self._cell_size

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def is_window_open(self):
        pr.init_window(self._width, self._height, self._caption)
        pr.set_target_fps(self._frame_rate)

    def draw_grid(self):
        for y in range(0, self._height, self._cell_size):
            pr.draw_line(0, y, self._width, y, pr.GRAY)
        for x in range(0, self._width, self._cell_size):
            pr.draw_line(x, 0, x, self._height, pr.GRAY)






class VideoServiceRFK:

    def __init__(self, caption, width, height, cell_size, frame_rate, debug = False):
        # Constructs a new VideoService using the specified debug mode
        self._caption = caption
        self._width = width
        self._height = height
        self._cell_size = cell_size
        self._frame_rate = frame_rate
        self._debug = debug

    def close_window(self):
        # Closes the window and releases all computing resources
        pyray.close_window()


    def clear_buffer(self):
        # Clears the buffer in preparation for the next rendering. This method should be called at
        # the beginning of the game's output phase.
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()
    
    def draw_actor(self, actor):
        # Draws the given actor's text on the screen.         
        text = actor.get_text()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()
        pyray.draw_text(text, x, y, font_size, color)
        

    def draw_actors(self, actors):
        # Draws the text for the given list of actors on the screen.
        for actor in actors:
            self.draw_actor(actor)
    
    def flush_buffer(self):
        #Copies the buffer contents to the screen. 
        #This method should be called at the end of the game's output phase.
        pyray.end_drawing()


    def get_cell_size(self):
        # Gets the video screen's cell size.
        return self._cell_size


    def get_height(self):
        return self._height


    def get_width(self):
        return self._width


    def is_window_open(self):
        # Whether or not the window was closed by the user.
        return not pyray.window_should_close()


    def open_window(self):
        # Opens a new window with the provided title.
        pyray.init_window(self._width, self._height, self._caption)
        pyray.set_target_fps(self._frame_rate)


    def _draw_grid(self):
        """Draws a grid on the screen."""
        for y in range(0, self._height, self._cell_size):
            pyray.draw_line(0, y, self._width, y, pyray.GRAY)
        for x in range(0, self._width, self._cell_size):
            pyray.draw_line(x, 0, x, self._height, pyray.GRAY)