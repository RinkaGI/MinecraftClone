import pyglet

pyglet.options["shadow_windows"] = False
pyglet.options["debug_gl"] = False

import pyglet.gl as gl

class Window(pyglet.window.Window):
	def __init__(self, **args):
		super().__init__(**args)
	
	def on_draw(self):
		gl.glClearColor(1.0, 0.5, 1.0, 1.0)
		self.clear()
	
	def on_resize(self, width, height):
		print(f"Resize {width} * {height}")
class Game:
    def __init__(self) -> None:
        self.config = gl.Config(
            double_buffer = True,
            major_version = 3,
            minor_version = 3
        )

        self.window = Window(
            config = self.config,
            width = 800,
            height = 600,
            caption = "Minecraft clone",
            resizable = True,
            vsync = False
        )

    def run(self):
        pyglet.app.run()

if __name__ == '__main__':
    game = Game()
    game.run()