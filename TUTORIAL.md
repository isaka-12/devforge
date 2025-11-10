# 🎓 Tutorial: Adding a New Framework to DevForge

This tutorial walks you through adding support for a new framework to DevForge. We'll use **Next.js** as an example.

## 📋 Prerequisites

- Basic Python knowledge
- Understanding of the framework you're adding
- DevForge codebase cloned locally

## 🎯 Overview

Adding a new framework involves 4 simple steps:
1. Create a scaffolder class
2. Register it
3. Add CLI option
4. Test it

**Time required:** ~30 minutes for a basic scaffolder

## 📝 Step-by-Step Guide

### Step 1: Create the Scaffolder Class

Create a new file: `devforge/scaffolders/nextjs.py`

```python
"""
Next.js framework scaffolder implementation.

This module provides scaffolding for Next.js projects.
"""

from pathlib import Path
from typing import Dict, List, Optional
import subprocess
import os
import click

from .base import FrameworkScaffolder, parse_features


class NextJSScaffolder(FrameworkScaffolder):
    """
    Scaffolder for Next.js projects.
    
    Creates a Next.js project with App Router and feature-based structure.
    """
    
    def get_framework_name(self) -> str:
        """Return 'Next.js'"""
        return "Next.js"
    
    def get_emoji(self) -> str:
        """Return Next.js emoji"""
        return "▲"  # Next.js triangle logo
    
    def get_required_command(self) -> str:
        """Next.js uses npm/npx"""
        return "npm"
    
    def get_install_url(self) -> str:
        """URL to install Node.js"""
        return "https://nodejs.org"
    
    def prompt_user(self) -> Dict[str, any]:
        """
        Prompt user for Next.js configuration.
        
        Returns:
            Dict with project_name, use_typescript, use_tailwind, features
        """
        project_name = click.prompt("🧱 Project name")
        ts_choice = click.prompt("Use TypeScript? (y/n)", default="y")
        tailwind_choice = click.prompt("Use Tailwind CSS? (y/n)", default="y")
        features_input = click.prompt(
            "Enter features (comma separated)", 
            default="core"
        )
        
        return {
            'project_name': project_name,
            'use_typescript': ts_choice.lower() == 'y',
            'use_tailwind': tailwind_choice.lower() == 'y',
            'features': parse_features(features_input)
        }
    
    def create_base_project(self, config: Dict[str, any]) -> Optional[Path]:
        """
        Create base Next.js project using create-next-app.
        """
        project_name = config['project_name']
        use_typescript = config['use_typescript']
        use_tailwind = config['use_tailwind']
        
        cwd = Path.cwd()
        project_path = cwd / project_name
        
        # Build command
        cmd = f'npx create-next-app@latest {project_name}'
        
        # Add flags for non-interactive mode
        cmd += ' --yes'  # Skip confirmation prompts
        
        if use_typescript:
            cmd += ' --typescript'
        else:
            cmd += ' --javascript'
        
        if use_tailwind:
            cmd += ' --tailwind'
        else:
            cmd += ' --no-tailwind'
        
        cmd += ' --app'  # Use App Router (recommended)
        cmd += ' --no-src-dir'  # Don't use src/ directory
        cmd += ' --import-alias "@/*"'  # Set import alias
        
        try:
            subprocess.run(
                cmd,
                shell=True,
                check=True,
                capture_output=False,
                text=True
            )
            return project_path
        except subprocess.CalledProcessError as e:
            click.echo(f"❌ Error creating Next.js project: {e}")
            return None
        except FileNotFoundError:
            click.echo(f"❌ Error: npm command not found")
            return None
    
    def create_feature_structure(self, project_path: Path, 
                                features: List[str], 
                                config: Dict[str, any]) -> None:
        """
        Create feature-based folder structure in Next.js project.
        
        Each feature gets:
        - components: React components
        - hooks: Custom React hooks
        - actions: Server actions
        - api: API routes
        - types: TypeScript types (if using TS)
        """
        use_typescript = config.get('use_typescript', False)
        
        # Next.js App Router uses /app directory
        features_path = project_path / "app" / "features"
        os.makedirs(features_path, exist_ok=True)
        
        # Define subdirectories
        subdirs = ["components", "hooks", "actions", "api"]
        if use_typescript:
            subdirs.append("types")
        
        for feature in features:
            feature_path = features_path / feature
            for subdir in subdirs:
                os.makedirs(feature_path / subdir, exist_ok=True)
                
                # Create index file for easier imports
                if use_typescript:
                    (feature_path / subdir / "index.ts").touch()
                else:
                    (feature_path / subdir / "index.js").touch()
    
    def get_next_steps(self, project_name: str, 
                      config: Dict[str, any]) -> List[str]:
        """Return commands to run the Next.js project."""
        return [
            f"cd {project_name}",
            "npm run dev",
            "# Open http://localhost:3000 in your browser"
        ]
```

### Step 2: Register the Scaffolder

Edit `devforge/scaffolders/__init__.py`:

```python
from .base import FrameworkScaffolder
from .react import ReactScaffolder
from .fastapi import FastAPIScaffolder
from .flutter import FlutterScaffolder
from .nextjs import NextJSScaffolder  # ← Add this import

SCAFFOLDERS: Dict[str, Type[FrameworkScaffolder]] = {
    'react': ReactScaffolder,
    'fastapi': FastAPIScaffolder,
    'flutter': FlutterScaffolder,
    'nextjs': NextJSScaffolder,  # ← Add this line
}
```

### Step 3: Add CLI Option

Edit `devforge/cli.py`:

```python
@cli.command()
@click.option('--react', is_flag=True, help="Forge a new React project")
@click.option('--fastapi', is_flag=True, help="Forge a new FastAPI project")
@click.option('--flutter', is_flag=True, help="Forge a new Flutter project")
@click.option('--nextjs', is_flag=True, help="Forge a new Next.js project")  # ← Add this
def init(react, fastapi, flutter, nextjs):  # ← Add nextjs parameter
    """Initialize a new project in your current directory."""
    
    framework_map = {
        'react': react,
        'fastapi': fastapi,
        'flutter': flutter,
        'nextjs': nextjs,  # ← Add this line
    }
    
    # ... rest of the function remains the same
```

### Step 4: Test Your Scaffolder

```bash
# Reinstall the package
pip install -e .

# Test listing frameworks
devforge list

# Test creating a project
devforge init --nextjs
```

## ✅ Checklist

Before submitting your scaffolder, verify:

- [ ] Scaffolder extends `FrameworkScaffolder`
- [ ] All abstract methods are implemented
- [ ] Error handling for missing prerequisites
- [ ] Helpful error messages
- [ ] Feature structure is created correctly
- [ ] Next steps are provided
- [ ] Documentation strings are clear
- [ ] Tested with actual framework CLI
- [ ] Registered in `__init__.py`
- [ ] CLI option added
- [ ] Framework appears in `devforge list`

## 🎨 Best Practices

### 1. Error Handling

Always handle potential errors gracefully:

```python
try:
    subprocess.run(command, check=True, shell=True)
except subprocess.CalledProcessError as e:
    click.echo(f"❌ Error: {e}")
    return None
except FileNotFoundError:
    click.echo(f"❌ Command not found")
    return None
```

### 2. User-Friendly Messages

Use emojis and clear language:

```python
click.echo("⚙️  Creating project...")
click.echo("✅ Project created successfully!")
click.echo("❌ Error: Something went wrong")
```

### 3. Sensible Defaults

Provide good defaults for prompts:

```python
ts_choice = click.prompt("Use TypeScript? (y/n)", default="y")
```

### 4. Feature-Based Architecture

Organize by features, not file types:

```
✅ Good:
features/
  auth/
    components/
    hooks/
    services/

❌ Bad:
components/
  auth/
hooks/
  auth/
```

### 5. Documentation

Document what each method does:

```python
def create_base_project(self, config: Dict[str, any]) -> Optional[Path]:
    """
    Create base project using framework CLI.
    
    Args:
        config: Dictionary with project_name and other options
    
    Returns:
        Path to created project, or None if failed
    """
```

## 🐛 Debugging Tips

### Import Errors

```python
# Test imports
python -c "from devforge.scaffolders.nextjs import NextJSScaffolder; print('OK')"
```

### Test Individual Methods

```python
from devforge.scaffolders import get_scaffolder

scaffolder = get_scaffolder('nextjs')
print(scaffolder.framework_name)  # Should print "Next.js"
print(scaffolder.check_prerequisites())  # Test prerequisite checking
```

### Verbose Testing

Add print statements during development:

```python
def create_base_project(self, config):
    print(f"DEBUG: Config = {config}")
    print(f"DEBUG: Running command: {cmd}")
    # ... rest of method
```

## 📚 More Examples

### Django Scaffolder Outline

```python
class DjangoScaffolder(FrameworkScaffolder):
    def get_framework_name(self) -> str:
        return "Django"
    
    def get_emoji(self) -> str:
        return "🎸"
    
    def get_required_command(self) -> Optional[str]:
        return None  # Django is pure Python
    
    def create_base_project(self, config):
        # Use django-admin startproject
        subprocess.run([
            "django-admin", "startproject", 
            config['project_name']
        ])
        # ...
```

### Vue Scaffolder Outline

```python
class VueScaffolder(FrameworkScaffolder):
    def get_framework_name(self) -> str:
        return "Vue"
    
    def get_emoji(self) -> str:
        return "💚"
    
    def get_required_command(self) -> str:
        return "npm"
    
    def create_base_project(self, config):
        # Use npm create vue@latest
        subprocess.run([
            "npm", "create", "vue@latest",
            config['project_name']
        ])
        # ...
```

## 🎓 Learning Resources

- **DevForge Architecture**: See `ARCHITECTURE.md` for design patterns
- **Click Documentation**: https://click.palletsprojects.com
- **subprocess Module**: https://docs.python.org/3/library/subprocess.html
- **pathlib Module**: https://docs.python.org/3/library/pathlib.html

## 🚀 Next Steps

After adding your scaffolder:

1. **Test thoroughly** with various configurations
2. **Add to README** in the "Supported Frameworks" section
3. **Update version** in `setup.py`
4. **Write tests** (optional but recommended)
5. **Submit PR** or use internally

## 💡 Tips for Success

- Start simple, add features incrementally
- Test early and often
- Look at existing scaffolders for reference
- Keep user experience in mind
- Handle edge cases gracefully

## ❓ Common Issues

**Q: My scaffolder isn't showing up in `devforge list`**  
A: Make sure you registered it in `scaffolders/__init__.py` and reinstalled the package

**Q: Getting import errors**  
A: Check that all imports use relative imports (`.base`, `.fastapi`, etc.)

**Q: Subprocess command fails**  
A: Use `shell=True` for complex commands with pipes or redirects

**Q: Features not created in right location**  
A: Use `pathlib.Path` for cross-platform path handling

---

**Happy Scaffolding! 🔥**
