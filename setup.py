import cx_Freeze

executables_12 = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name = "SpaceWars",
    options = {"build_exe": {"packages": ["pygame"],
    "include_files": ["background.png", "background.wav", "bullet.png", "explosion.wav", "laser.wav", "rocket-32.png", "rocket-64.png",
    "skull.png"]}},
    executables = executables_12
)



