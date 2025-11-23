import os
import yaml # pip install pyyaml
from pathlib import Path

def generate_scaffold(phase_file):
    with open(phase_file, 'r') as f:
        blueprint = yaml.safe_load(f)

    phase_id = blueprint['phase_id']
    phase_name = blueprint['name']
    output_root = Path(f"output/phase_{phase_id:02d}_{phase_name.lower().replace(' ', '_')}")
    
    print(f"🏗️  Scaffolding Phase {phase_id}: {phase_name}...")

    # 1. Create Directories
    for folder in blueprint.get('structure', []):
        path = output_root / folder
        path.mkdir(parents=True, exist_ok=True)
        # Create a .gitkeep to ensure git tracks it
        (path / ".gitkeep").touch()

    # 2. Create Key Files with Descriptions
    for file_def in blueprint.get('files', []):
        path = output_root / file_def['path']
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w') as f:
            f.write(f"# {Path(file_def['path']).name}\n")
            f.write(f"## Purpose\n{file_def['description']}\n\n")
            if 'content' in file_def:
                f.write(file_def['content'])

    # 3. Generate Architecture README
    with open(output_root / "ARCHITECTURE.md", 'w') as f:
        f.write(f"# Phase {phase_id}: {phase_name}\n\n")
        f.write(f"**Goal:** {blueprint['goal']}\n")
        f.write(f"**Stack:** {blueprint['stack']}\n\n")
        f.write("## Database Schema Changes\n")
        for model in blueprint.get('data_models', []):
            f.write(f"### {model['name']}\n")
            for field in model['fields']:
                f.write(f"- {field}\n")
            f.write("\n")

if __name__ == "__main__":
    # Process all YAMLs in blueprints/ folder
    blueprints_dir = Path("blueprints")
    for yaml_file in sorted(blueprints_dir.glob("phase_*.yaml")):
        generate_scaffold(yaml_file)
