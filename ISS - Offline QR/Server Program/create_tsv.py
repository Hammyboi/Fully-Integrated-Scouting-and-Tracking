import tomllib

header = "Scouter Initials|Match Number|Robot|Team Number|No Show|Starting Location|Mobility|Auto Upper Cone|Auto Middle Cone|Auto Lower Cone|Auto Upper Cube|Auto Middle Cube|Auto Lower Cube|Auto Pickup|Auto Dock Engage|Teleop Upper Cone|Teleop Middle Cone|Teleop Lower Cone|Teleop Upper Cube|Teleop Middle Cube|Teleop Lower Cube|Teleop Pickup|Links|Early Endgame|Endgame Location|Number Of Docked Robots|Skill|Defense|Died|Tipped|Red/Yellow Card|Damaged|Comments"

with open("config.toml", "rb") as f:
    config = tomllib.load(f)
with open(config["output_file"], "w") as file:
    file.write(header)