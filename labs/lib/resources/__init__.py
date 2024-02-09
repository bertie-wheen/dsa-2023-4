from pathlib import Path

labs_dir = Path.cwd()
if labs_dir.name != "labs":
    labs_dir /= "labs"

resources_dir = labs_dir / "lib" / "resources"
