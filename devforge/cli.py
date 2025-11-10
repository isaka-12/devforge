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
        click.secho("⚠️  Please specify a stack: --react, --fastapi, or --flutter", fg='yellow')
        click.echo()
        click.secho("Tip: ", fg='cyan', nl=False)
        click.echo("Run 'devforge list' to see all available frameworks")
        return
    
    # Get the appropriate scaffolder and run it
    try:
        scaffolder = get_scaffolder(selected_framework)
        scaffolder.forge()
    except KeyError as e:
        click.secho(f"❌ Error: {e}", fg='red')
    except Exception as e:
        click.secho(f"❌ Unexpected error: {e}", fg='red')


@cli.command()
def list():
    """
    List all available frameworks.
    
    Shows all frameworks that can be scaffolded with DevForge.
    """
    click.secho("\n🔥 Available frameworks in DevForge:\n", fg='cyan', bold=True)
    
    frameworks = list_available_frameworks()
    for framework_key in frameworks:
        try:
            scaffolder = get_scaffolder(framework_key)
            click.secho(f"  {scaffolder.emoji} ", nl=False, fg='yellow')
            click.secho(f"{scaffolder.framework_name.ljust(15)}", nl=False, fg='green', bold=True)
            click.secho(f" (--{framework_key})", fg='white')
        except Exception:
            click.echo(f"  • {framework_key.ljust(15)} (--{framework_key})")
    
    click.echo()
    click.secho(f"Total: {len(frameworks)} frameworks", fg='cyan')
    click.echo()
    click.secho("Usage: ", fg='yellow', nl=False)
    click.secho("devforge init --<framework>", fg='white', bold=True)


@cli.command()
def version():
    """Display the version of DevForge."""
    click.secho("🔥 DevForge v1.0.1", fg='cyan', bold=True)
    click.secho("Universal project scaffolder for React, FastAPI, and Flutter", fg='white')
    click.echo()
    click.secho("📦 Package: ", fg='yellow', nl=False)
    click.echo("devforge-cli")
    click.secho("🌐 Homepage: ", fg='yellow', nl=False)
    click.echo("https://github.com/isaka-12/devforge")
    click.secho("📚 Docs: ", fg='yellow', nl=False)
    click.echo("https://github.com/isaka-12/devforge#readme")
    click.echo()
    click.secho("💡 Tip: Run 'devforge list' to see available frameworks", fg='green')


if __name__ == "__main__":
    cli()
