"""
React framework scaffolder implementation.

This module provides scaffolding for React projects using Vite.
Supports both JavaScript and TypeScript templates.
"""

from pathlib import Path
from typing import Dict, List, Optional
import subprocess
import os
import click

from .base import FrameworkScaffolder, parse_features


class ReactScaffolder(FrameworkScaffolder):
    """
    Scaffolder for React projects using Vite.
    
    Creates a Vite-based React project with feature-based architecture.
    Each feature contains: components, hooks, pages, services, utils, and types (if TypeScript).
    """
    
    def get_framework_name(self) -> str:
        return "React"
    
    def get_emoji(self) -> str:
        return "⚛️"
    
    def get_required_command(self) -> str:
        return "npm"
    
    def get_install_url(self) -> str:
        return "https://nodejs.org"
    
    def prompt_user(self) -> Dict[str, any]:
        """
        Prompt user for React project configuration.
        
        Returns:
            Dict with keys: project_name, use_typescript, features
        """
        project_name = click.prompt("🧱 Project name")
        ts_choice = click.prompt("Use TypeScript? (y/n)", default="y")
        features_input = click.prompt("Enter features (comma separated)", default="core")
        
        return {
            'project_name': project_name,
            'use_typescript': ts_choice.lower() == 'y',
            'features': parse_features(features_input)
        }
    
    def create_base_project(self, config: Dict[str, any]) -> Optional[Path]:
        """
        Create base Vite + React project.
        
        Args:
            config: Must contain 'project_name' and 'use_typescript'
        
        Returns:
            Path to created project or None on failure
        """
        project_name = config['project_name']
        use_typescript = config['use_typescript']
        
        cwd = Path.cwd()
        project_path = cwd / project_name
        template = "react-ts" if use_typescript else "react"
        
        try:
            subprocess.run(
                f'npm create vite@latest {project_name} -- --template {template}',
                shell=True,
                check=True,
                capture_output=False,
                text=True
            )
            return project_path
        except subprocess.CalledProcessError as e:
            click.echo(f"❌ Error creating Vite project: {e}")
            return None
        except FileNotFoundError:
            click.echo(f"❌ Error: npm command not found")
            return None
    
    def create_feature_structure(self, project_path: Path, features: List[str], config: Dict[str, any]) -> None:
        """
        Create feature-based folder structure in React project.
        
        Each feature gets: components, hooks, pages, services, utils
        TypeScript projects also get a types folder.
        
        Args:
            project_path: Root path of the project
            features: List of feature names
            config: Project configuration (checks 'use_typescript')
        """
        use_typescript = config.get('use_typescript', False)
        src_path = project_path / "src" / "features"
        os.makedirs(src_path, exist_ok=True)
        
        # Define subdirectories for each feature
        subdirs = ["components", "hooks", "pages", "services", "utils"]
        if use_typescript:
            subdirs.append("types")
        
        for feature in features:
            feature_path = src_path / feature
            for subdir in subdirs:
                os.makedirs(feature_path / subdir, exist_ok=True)
    
    def get_next_steps(self, project_name: str, config: Dict[str, any]) -> List[str]:
        """Return commands to run the React project."""
        return [
            f"cd {project_name}",
            "npm install",
            "npm run dev"
        ]
