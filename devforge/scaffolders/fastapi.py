"""
FastAPI framework scaffolder implementation.

This module provides scaffolding for FastAPI projects.
Creates a feature-based backend architecture.
"""

from pathlib import Path
from typing import Dict, List, Optional
import os
import click

from .base import FrameworkScaffolder, parse_features


class FastAPIScaffolder(FrameworkScaffolder):
    """
    Scaffolder for FastAPI projects.
    
    Creates a feature-based FastAPI project structure.
    Each feature contains: models, services, and routers.
    """
    
    def get_framework_name(self) -> str:
        return "FastAPI"
    
    def get_emoji(self) -> str:
        return "🐍"
    
    def get_required_command(self) -> Optional[str]:
        # FastAPI doesn't require external command for scaffolding
        return None
    
    def get_install_url(self) -> Optional[str]:
        return None
    
    def prompt_user(self) -> Dict[str, any]:
        """
        Prompt user for FastAPI project configuration.
        
        Returns:
            Dict with keys: project_name, features
        """
        project_name = click.prompt("🧱 Project name")
        features_input = click.prompt("Enter features (comma separated)", default="core")
        
        return {
            'project_name': project_name,
            'features': parse_features(features_input)
        }
    
    def create_base_project(self, config: Dict[str, any]) -> Optional[Path]:
        """
        Create base FastAPI project structure.
        
        Args:
            config: Must contain 'project_name'
        
        Returns:
            Path to created project
        """
        project_name = config['project_name']
        cwd = Path.cwd()
        project_path = cwd / project_name
        
        # Create main.py with basic FastAPI app
        main_file = project_path / "app" / "main.py"
        main_file.parent.mkdir(parents=True, exist_ok=True)
        main_file.write_text(
            "from fastapi import FastAPI\n\n"
            "app = FastAPI()\n\n"
            "@app.get('/')\n"
            "def root():\n"
            "    return {'message': 'Hello from DevForge FastAPI!'}\n"
        )
        
        # Create __init__.py for app package
        (project_path / "app" / "__init__.py").touch()
        
        # Create requirements.txt
        requirements_file = project_path / "requirements.txt"
        requirements_file.write_text(
            "fastapi>=0.104.0\n"
            "uvicorn[standard]>=0.24.0\n"
        )
        
        # Create README.md
        readme_file = project_path / "README.md"
        readme_file.write_text(
            f"# {project_name}\n\n"
            "FastAPI project created with DevForge.\n\n"
            "## Getting Started\n\n"
            "1. Install dependencies:\n"
            "   ```bash\n"
            "   pip install -r requirements.txt\n"
            "   ```\n\n"
            "2. Run the development server:\n"
            "   ```bash\n"
            "   uvicorn app.main:app --reload\n"
            "   ```\n\n"
            "3. Open http://127.0.0.1:8000 in your browser\n"
            "4. API documentation available at http://127.0.0.1:8000/docs\n"
        )
        
        return project_path
    
    def create_feature_structure(self, project_path: Path, features: List[str], config: Dict[str, any]) -> None:
        """
        Create feature-based folder structure in FastAPI project.
        
        Each feature gets: models, services, routers
        
        Args:
            project_path: Root path of the project
            features: List of feature names
            config: Project configuration (unused for FastAPI)
        """
        base = project_path / "app" / "features"
        
        for feature in features:
            feature_path = base / feature
            for subdir in ["models", "services", "routers"]:
                subdir_path = feature_path / subdir
                os.makedirs(subdir_path, exist_ok=True)
                # Create __init__.py in each directory
                (subdir_path / "__init__.py").touch()
            
            # Create __init__.py in feature directory
            (feature_path / "__init__.py").touch()
        
        # Create __init__.py in features directory
        (base / "__init__.py").touch()
    
    def get_next_steps(self, project_name: str, config: Dict[str, any]) -> List[str]:
        """Return commands to run the FastAPI project."""
        return [
            f"cd {project_name}",
            "pip install -r requirements.txt",
            "uvicorn app.main:app --reload"
        ]
