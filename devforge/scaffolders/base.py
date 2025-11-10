"""
Base classes and utilities for framework scaffolders.

This module provides the abstract base class and common utilities
for implementing framework-specific project scaffolders.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, List, Optional
import shutil
import click


class FrameworkScaffolder(ABC):
    """
    Abstract base class for framework scaffolders.
    
    Each framework (React, FastAPI, Flutter, etc.) should implement
    this interface to provide consistent scaffolding behavior.
    
    Attributes:
        framework_name (str): Display name of the framework
        emoji (str): Emoji icon for the framework
        required_command (str): Command to check if framework tools are installed
        install_url (str): URL where users can install the framework tools
    """
    
    def __init__(self):
        self.framework_name: str = self.get_framework_name()
        self.emoji: str = self.get_emoji()
        self.required_command: Optional[str] = self.get_required_command()
        self.install_url: Optional[str] = self.get_install_url()
    
    @abstractmethod
    def get_framework_name(self) -> str:
        """Return the display name of the framework."""
        pass
    
    @abstractmethod
    def get_emoji(self) -> str:
        """Return the emoji icon for the framework."""
        pass
    
    def get_required_command(self) -> Optional[str]:
        """
        Return the command required to scaffold projects (e.g., 'npm', 'flutter').
        Return None if no external command is required.
        """
        return None
    
    def get_install_url(self) -> Optional[str]:
        """Return the URL where users can install the framework tools."""
        return None
    
    def check_prerequisites(self) -> bool:
        """
        Check if required tools are installed.
        
        Returns:
            bool: True if prerequisites are met, False otherwise
        """
        if not self.required_command:
            return True
        
        cmd_path = shutil.which(self.required_command)
        if not cmd_path:
            click.echo(f"❌ Error: {self.required_command} is not installed or not in PATH")
            if self.install_url:
                click.echo(f"{self.emoji} Please install from {self.install_url}")
            click.echo("   Then restart your terminal and try again.")
            return False
        
        return True
    
    @abstractmethod
    def prompt_user(self) -> Dict[str, any]:
        """
        Prompt user for project configuration.
        
        Returns:
            Dict[str, any]: Dictionary containing user's choices
        """
        pass
    
    @abstractmethod
    def create_base_project(self, config: Dict[str, any]) -> Optional[Path]:
        """
        Create the base project structure.
        
        Args:
            config (Dict[str, any]): Configuration from prompt_user()
        
        Returns:
            Optional[Path]: Path to the created project, or None if failed
        """
        pass
    
    @abstractmethod
    def create_feature_structure(self, project_path: Path, features: List[str], config: Dict[str, any]) -> None:
        """
        Create custom feature folders within the project.
        
        Args:
            project_path (Path): Path to the project root
            features (List[str]): List of feature names to create
            config (Dict[str, any]): Additional configuration options
        """
        pass
    
    def get_next_steps(self, project_name: str, config: Dict[str, any]) -> List[str]:
        """
        Return list of next steps for the user after scaffolding.
        
        Args:
            project_name (str): Name of the created project
            config (Dict[str, any]): Project configuration
        
        Returns:
            List[str]: List of command strings to show user
        """
        return []
    
    def forge(self) -> None:
        """
        Main entry point to scaffold a project.
        
        This orchestrates the entire scaffolding process:
        1. Check prerequisites
        2. Prompt user for configuration
        3. Create base project
        4. Create feature structure
        5. Display next steps
        """
        # Step 1: Check prerequisites
        if not self.check_prerequisites():
            return
        
        # Step 2: Prompt user
        config = self.prompt_user()
        if not config:
            return
        
        project_name = config.get('project_name')
        features = config.get('features', ['core'])
        
        # Step 3: Create base project
        click.echo(f"⚙️  Creating {self.framework_name} project...")
        project_path = self.create_base_project(config)
        
        if not project_path:
            return
        
        # Step 4: Create feature structure
        self.create_feature_structure(project_path, features, config)
        
        # Step 5: Display success and next steps
        click.echo(f"\n✅ {self.framework_name} project '{project_name}' forged successfully at {project_path}")
        
        next_steps = self.get_next_steps(project_name, config)
        if next_steps:
            click.echo(f"\n📦 Next steps:")
            for step in next_steps:
                click.echo(f"   {step}")


def parse_features(features_input: str) -> List[str]:
    """
    Parse comma-separated feature string into list.
    
    Args:
        features_input (str): Comma-separated feature names
    
    Returns:
        List[str]: List of trimmed feature names
    """
    return [f.strip() for f in features_input.split(",") if f.strip()]
