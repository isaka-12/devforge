"""
DevForge CLI - Universal project scaffolder.

This is the main entry point for the DevForge CLI tool.
It provides a command-line interface for scaffolding projects
across multiple frameworks (React, FastAPI, Flutter, etc.).

Usage:
    devforge init --react      # Create a React project
    devforge init --fastapi    # Create a FastAPI project
    devforge init --flutter    # Create a Flutter project
    devforge list              # List all available frameworks

To add a new framework:
    1. Create a new scaffolder in devforge/scaffolders/
    2. Extend the FrameworkScaffolder base class
    3. Register it in devforge/scaffolders/__init__.py
    4. Add a new option in the init() command below
"""

import click
from .scaffolders import get_scaffolder, list_available_frameworks


@click.group()
def cli():
    """🔥 DevForge — Universal project scaffolder for React, FastAPI, and Flutter."""
    pass


@cli.command()
@click.option('--react', is_flag=True, help="Forge a new React project")
@click.option('--fastapi', is_flag=True, help="Forge a new FastAPI project")
@click.option('--flutter', is_flag=True, help="Forge a new Flutter project")
def init(react, fastapi, flutter):
    """
    Initialize a new project in your current directory.
    
    Choose one framework option to scaffold a project with
    a feature-based architecture and best practices.
    
    Examples:
        devforge init --react      # Create React + Vite project
        devforge init --fastapi    # Create FastAPI project
        devforge init --flutter    # Create Flutter project
    """
    # Map CLI flags to scaffolder keys
    framework_map = {
        'react': react,
        'fastapi': fastapi,
        'flutter': flutter,
    }
    
    # Find which framework was selected
    selected_framework = None
    for framework_key, flag_value in framework_map.items():
        if flag_value:
            selected_framework = framework_key
            break
    
    if not selected_framework:
        click.echo("⚠️  Please specify a stack: --react, --fastapi, or --flutter")
        click.echo("\nTip: Run 'devforge list' to see all available frameworks")
        return
    
    # Get the appropriate scaffolder and run it
    try:
        scaffolder = get_scaffolder(selected_framework)
        scaffolder.forge()
    except KeyError as e:
        click.echo(f"❌ Error: {e}")
    except Exception as e:
        click.echo(f"❌ Unexpected error: {e}")


@cli.command()
def list():
    """
    List all available frameworks.
    
    Shows all frameworks that can be scaffolded with DevForge.
    """
    click.echo("� Available frameworks in DevForge:\n")
    
    frameworks = list_available_frameworks()
    for framework_key in frameworks:
        try:
            scaffolder = get_scaffolder(framework_key)
            click.echo(f"  {scaffolder.emoji} {scaffolder.framework_name.ljust(15)} (--{framework_key})")
        except Exception:
            click.echo(f"  • {framework_key.ljust(15)} (--{framework_key})")
    
    click.echo(f"\nTotal: {len(frameworks)} frameworks")
    click.echo("\nUsage: devforge init --<framework>")


@cli.command()
def version():
    """Display the version of DevForge."""
    click.echo("DevForge v1.0.0")
    click.echo("Universal project scaffolder")


if __name__ == "__main__":
    cli()
