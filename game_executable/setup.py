#coding:utf-8
""" Fichier d'installation du script main.py"""

from cx_Freeze import setup, Executable

setup(
	name = "Mac Gyver", 
	version = "0.1",
	descrition = "Labyrinthe game",
	executables = [Executable("main.py")]
)

