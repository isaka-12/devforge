"""
Flutter framework scaffolder implementation.

This module provides scaffolding for Flutter projects.
Creates a clean architecture structure.
"""

from pathlib import Path
from typing import Dict, List, Optional
import subprocess
import os
import click

from .base import FrameworkScaffolder, parse_features


class FlutterScaffolder(FrameworkScaffolder):
    """
    Scaffolder for Flutter projects.
    
    Creates a Flutter project with Clean Architecture structure.
    Each feature contains: domain, data, and presentation layers.
    """
    
    def get_framework_name(self) -> str:
        return "Flutter"
    
    def get_emoji(self) -> str:
        return "💙"
    
    def get_required_command(self) -> str:
        return "flutter"
    
    def get_install_url(self) -> str:
        return "https://flutter.dev"
    
    def prompt_user(self) -> Dict[str, any]:
        """
        Prompt user for Flutter project configuration.
        
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
        Create base Flutter project.
        
        Args:
            config: Must contain 'project_name'
        
        Returns:
            Path to created project or None on failure
        """
        project_name = config['project_name']
        cwd = Path.cwd()
        
        try:
            subprocess.run(
                ["flutter", "create", project_name],
                check=True,
                shell=True
            )
            return cwd / project_name
        except subprocess.CalledProcessError as e:
            click.echo(f"❌ Error creating Flutter project: {e}")
            return None
        except FileNotFoundError:
            click.echo(f"❌ Error: flutter command not found")
            return None
    
    def create_feature_structure(self, project_path: Path, features: List[str], config: Dict[str, any]) -> None:
        """
        Create Clean Architecture folder structure in Flutter project.
        
        Each feature gets:
        - domain: Business logic and entities
        - data: Data sources and repositories
        - presentation: UI (widgets and screens)
        
        Args:
            project_path: Root path of the project
            features: List of feature names
            config: Project configuration (unused for Flutter)
        """
        base = project_path / "lib" / "features"
        
        for feature in features:
            feature_path = base / feature
            
            # Create domain layer
            os.makedirs(feature_path / "domain", exist_ok=True)
            
            # Create data layer
            os.makedirs(feature_path / "data", exist_ok=True)
            
            # Create presentation layer with subdirectories
            os.makedirs(feature_path / "presentation" / "widgets", exist_ok=True)
            os.makedirs(feature_path / "presentation" / "screens", exist_ok=True)
    
    def get_next_steps(self, project_name: str, config: Dict[str, any]) -> List[str]:
        """Return commands to run the Flutter project."""
        return [
            f"cd {project_name}",
            "flutter pub get",
            "flutter run"
        ]
