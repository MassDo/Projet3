from cx_Freeze import setup, Executable

setup(
	name = "Mac Gyver",
	version = "0.1",
	description = "Labyrinthe game",
	executables = [Executable("main.py")]
)