# DevForge Architecture Documentation

## 📚 Overview

DevForge is a modular, extensible CLI tool for scaffolding projects across multiple frameworks. The architecture is designed to make adding new frameworks as simple as creating a single new file.

## 🏗️ Project Structure

```
devforge/
├── __init__.py                 # Package initialization
├── cli.py                      # CLI entry point and command definitions
└── scaffolders/                # Framework scaffolder modules
    ├── __init__.py            # Scaffolder registry
    ├── base.py                # Abstract base class
    ├── react.py               # React/Vite scaffolder
    ├── fastapi.py             # FastAPI scaffolder
    └── flutter.py             # Flutter scaffolder
```

## 🎯 Core Concepts

### 1. Base Scaffolder (`scaffolders/base.py`)

The `FrameworkScaffolder` abstract base class defines the contract that all framework scaffolders must implement:

```python
class FrameworkScaffolder(ABC):
    @abstractmethod
    def get_framework_name(self) -> str:
        """Return display name (e.g., 'React', 'FastAPI')"""
    
    @abstractmethod
    def get_emoji(self) -> str:
        """Return emoji icon (e.g., '⚛️', '🐍')"""
    
    @abstractmethod
    def prompt_user(self) -> Dict[str, any]:
        """Prompt user for project configuration"""
    
    @abstractmethod
    def create_base_project(self, config: Dict) -> Optional[Path]:
        """Create the base project structure"""
    
    @abstractmethod
    def create_feature_structure(self, project_path: Path, features: List[str], config: Dict):
        """Create custom feature folders"""
    
    def forge(self):
        """Main orchestration method (implemented in base class)"""
```

### 2. Framework Scaffolders

Each framework has its own scaffolder that extends `FrameworkScaffolder`:

- **`ReactScaffolder`**: Creates Vite + React projects with feature-based architecture
- **`FastAPIScaffolder`**: Creates FastAPI projects with backend feature structure
- **`FlutterScaffolder`**: Creates Flutter projects with Clean Architecture

### 3. Registry System (`scaffolders/__init__.py`)

The registry maintains a dictionary of all available scaffolders:

```python
SCAFFOLDERS = {
    'react': ReactScaffolder,
    'fastapi': FastAPIScaffolder,
    'flutter': FlutterScaffolder,
}
```

## 🔌 Adding a New Framework

Adding support for a new framework is a 4-step process:

### Step 1: Create Scaffolder File

Create `devforge/scaffolders/your_framework.py`:

```python
from pathlib import Path
from typing import Dict, List, Optional
import click
from .base import FrameworkScaffolder, parse_features

class YourFrameworkScaffolder(FrameworkScaffolder):
    def get_framework_name(self) -> str:
        return "YourFramework"
    
    def get_emoji(self) -> str:
        return "🎯"  # Choose an appropriate emoji
    
    def get_required_command(self) -> Optional[str]:
        return "your-cli-tool"  # Or None if no external tool needed
    
    def get_install_url(self) -> Optional[str]:
        return "https://your-framework.dev"
    
    def prompt_user(self) -> Dict[str, any]:
        project_name = click.prompt("🧱 Project name")
        # Add your custom prompts here
        return {
            'project_name': project_name,
            # ... other config
        }
    
    def create_base_project(self, config: Dict[str, any]) -> Optional[Path]:
        # Create base project structure
        # Return project path or None on failure
        pass
    
    def create_feature_structure(self, project_path: Path, 
                                features: List[str], 
                                config: Dict[str, any]) -> None:
        # Create custom feature folders
        pass
    
    def get_next_steps(self, project_name: str, 
                      config: Dict[str, any]) -> List[str]:
        return [
            f"cd {project_name}",
            "your-install-command",
            "your-run-command"
        ]
```

### Step 2: Register in `scaffolders/__init__.py`

```python
from .your_framework import YourFrameworkScaffolder

SCAFFOLDERS = {
    'react': ReactScaffolder,
    'fastapi': FastAPIScaffolder,
    'flutter': FlutterScaffolder,
    'yourframework': YourFrameworkScaffolder,  # Add this line
}
```

### Step 3: Add CLI Option in `cli.py`

```python
@cli.command()
@click.option('--react', is_flag=True, help="Forge a new React project")
@click.option('--fastapi', is_flag=True, help="Forge a new FastAPI project")
@click.option('--flutter', is_flag=True, help="Forge a new Flutter project")
@click.option('--yourframework', is_flag=True, help="Forge a new YourFramework project")
def init(react, fastapi, flutter, yourframework):
    framework_map = {
        'react': react,
        'fastapi': fastapi,
        'flutter': flutter,
        'yourframework': yourframework,  # Add this line
    }
    # ... rest of function
```

### Step 4: Test

```bash
devforge init --yourframework
```

## 🎨 Design Patterns Used

### 1. **Template Method Pattern**
The `forge()` method in `FrameworkScaffolder` defines the skeleton of the scaffolding algorithm:
1. Check prerequisites
2. Prompt user
3. Create base project
4. Create features
5. Show next steps

Each scaffolder implements the specific steps.

### 2. **Registry Pattern**
The `SCAFFOLDERS` dictionary acts as a registry, allowing dynamic lookup of scaffolders without tight coupling.

### 3. **Strategy Pattern**
Each scaffolder is a strategy for creating a specific type of project. The CLI selects the appropriate strategy at runtime.

## 📦 Feature-Based Architecture

All scaffolders create a **feature-based architecture** where related code is grouped by feature rather than by type:

### React Structure
```
src/features/
├── auth/
│   ├── components/
│   ├── hooks/
│   ├── pages/
│   ├── services/
│   ├── utils/
│   └── types/         # TypeScript only
└── profile/
    └── ...
```

### FastAPI Structure
```
app/features/
├── auth/
│   ├── models/
│   ├── services/
│   └── routers/
└── profile/
    └── ...
```

### Flutter Structure (Clean Architecture)
```
lib/features/
├── auth/
│   ├── domain/
│   ├── data/
│   └── presentation/
│       ├── screens/
│       └── widgets/
└── profile/
    └── ...
```

## 🔧 Utilities

### `parse_features()`
Helper function to parse comma-separated feature strings:
```python
features = parse_features("auth, profile, dashboard")
# Returns: ['auth', 'profile', 'dashboard']
```

### `check_prerequisites()`
Automatically checks if required CLI tools (npm, flutter, etc.) are installed and provides helpful error messages.

## 🚀 CLI Commands

### `devforge init --<framework>`
Create a new project for the specified framework.

### `devforge list`
Show all available frameworks with their emojis and CLI flags.

### `devforge version`
Display the current version of DevForge.

## 🧪 Testing New Scaffolders

When developing a new scaffolder, test each method independently:

```python
# Test prerequisite checking
scaffolder = YourFrameworkScaffolder()
assert scaffolder.check_prerequisites() == True

# Test user prompting
config = scaffolder.prompt_user()
assert 'project_name' in config

# Test project creation
project_path = scaffolder.create_base_project(config)
assert project_path.exists()

# Test feature creation
scaffolder.create_feature_structure(project_path, ['auth'], config)
assert (project_path / "expected/feature/path").exists()
```

## 📝 Best Practices

1. **Comprehensive Error Handling**: Always handle `subprocess` failures and provide helpful error messages
2. **Clear Documentation**: Document what each method does and what it expects
3. **Emoji Consistency**: Use emojis to make CLI output more engaging
4. **Feature Independence**: Keep scaffolders independent - no cross-dependencies
5. **Validation**: Validate user input where appropriate
6. **Idempotency**: Make sure running a scaffolder twice doesn't cause issues

## 🎯 Future Enhancements

- Add configuration file support (`.devforge.yml`)
- Add template customization
- Add plugin system for community scaffolders
- Add interactive mode with arrow key navigation
- Add project migration/upgrade commands
- Add telemetry for popular frameworks

## 📄 License

This architecture documentation is part of the DevForge project.
