# 🔥 DevForge

**Universal project scaffolder for modern frameworks**

DevForge is a powerful CLI tool that scaffolds production-ready projects with feature-based architecture for React, FastAPI, Flutter, and more. Built with extensibility in mind, adding new frameworks is as simple as creating a single file.

## ✨ Features

- 🎯 **Feature-Based Architecture**: Organizes code by features, not file types
- 🔌 **Highly Extensible**: Add new frameworks in minutes
- 🎨 **Best Practices**: Follows industry standards for each framework
- 🚀 **Zero Configuration**: Works out of the box
- 💡 **Interactive CLI**: Friendly prompts guide you through setup
- 📦 **Multiple Frameworks**: React, FastAPI, Flutter (and growing!)

## 🚀 Quick Start

### Installation

```bash
pip install -e .
```

### Create a New Project

```bash
# React project with TypeScript
devforge init --react

# FastAPI backend
devforge init --fastapi

# Flutter mobile app
devforge init --flutter
```

## 📋 Available Commands

### `devforge init --<framework>`
Create a new project for the specified framework

**Options:**
- `--react`: Create a React + Vite project
- `--fastapi`: Create a FastAPI backend project
- `--flutter`: Create a Flutter mobile app

### `devforge list`
Show all available frameworks

### `devforge version`
Display DevForge version

## 🎯 Supported Frameworks

| Framework | Command | Description |
|-----------|---------|-------------|
| ⚛️ React | `--react` | Vite + React with feature-based architecture |
| 🐍 FastAPI | `--fastapi` | FastAPI backend with modular features |
| 💙 Flutter | `--flutter` | Flutter with Clean Architecture |

## 🏗️ Project Structure

### React Projects
```
project-name/
├── src/
│   └── features/
│       ├── auth/
│       │   ├── components/
│       │   ├── hooks/
│       │   ├── pages/
│       │   ├── services/
│       │   ├── utils/
│       │   └── types/         # TypeScript only
│       └── [feature-name]/
│           └── ...
├── package.json
└── vite.config.js
```

### FastAPI Projects
```
project-name/
├── app/
│   ├── main.py
│   └── features/
│       ├── auth/
│       │   ├── models/
│       │   ├── services/
│       │   └── routers/
│       └── [feature-name]/
│           └── ...
└── requirements.txt
```

### Flutter Projects
```
project-name/
├── lib/
│   ├── main.dart
│   └── features/
│       ├── auth/
│       │   ├── domain/         # Business logic
│       │   ├── data/           # Data sources
│       │   └── presentation/   # UI components
│       │       ├── screens/
│       │       └── widgets/
│       └── [feature-name]/
│           └── ...
└── pubspec.yaml
```

## 🎨 Usage Examples

### Creating a React Project

```bash
$ devforge init --react
🧱 Project name: my-awesome-app
Use TypeScript? (y/n) [y]: y
Enter features (comma separated) [core]: auth,profile,dashboard

⚙️  Creating Vite project...
✅ React project 'my-awesome-app' forged successfully!

📦 Next steps:
   cd my-awesome-app
   npm install
   npm run dev
```

### Creating a FastAPI Project

```bash
$ devforge init --fastapi
🧱 Project name: my-api
Enter features (comma separated) [core]: auth,users,posts

✅ FastAPI project 'my-api' forged successfully!

📦 Next steps:
   cd my-api
   pip install -r requirements.txt
   uvicorn app.main:app --reload
```

### Creating a Flutter Project

```bash
$ devforge init --flutter
🧱 Project name: my_flutter_app
Enter features (comma separated) [core]: auth,profile,settings

⚙️  Creating Flutter project...
✅ Flutter project 'my_flutter_app' forged successfully!

📦 Next steps:
   cd my_flutter_app
   flutter pub get
   flutter run
```

## 🔧 Requirements

### For All Projects
- Python 3.8 or higher
- pip

### Framework-Specific Requirements

**React:**
- Node.js 18+ and npm
- Download from: https://nodejs.org

**FastAPI:**
- No additional requirements (Python only)

**Flutter:**
- Flutter SDK
- Download from: https://flutter.dev

## 🧩 Extending DevForge

DevForge is designed to be easily extensible. See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed documentation on adding new frameworks.

### Quick Overview:

1. **Create a scaffolder** in `devforge/scaffolders/your_framework.py`
2. **Extend `FrameworkScaffolder`** base class
3. **Register it** in `scaffolders/__init__.py`
4. **Add CLI option** in `cli.py`

That's it! Your new framework is ready to use.

Example minimal scaffolder:

```python
from .base import FrameworkScaffolder

class MyFrameworkScaffolder(FrameworkScaffolder):
    def get_framework_name(self) -> str:
        return "MyFramework"
    
    def get_emoji(self) -> str:
        return "🎯"
    
    def prompt_user(self) -> Dict[str, any]:
        # Prompt for configuration
        pass
    
    def create_base_project(self, config: Dict) -> Optional[Path]:
        # Create project structure
        pass
    
    def create_feature_structure(self, project_path: Path, 
                                features: List[str], 
                                config: Dict) -> None:
        # Create feature folders
        pass
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Add New Frameworks**: Create scaffolders for other popular frameworks
2. **Improve Existing Scaffolders**: Enhance templates and structure
3. **Fix Bugs**: Report and fix issues
4. **Documentation**: Improve docs and examples

## 📚 Documentation

- [Architecture Guide](ARCHITECTURE.md) - Detailed architecture documentation
- [Adding Frameworks](ARCHITECTURE.md#adding-a-new-framework) - Step-by-step guide

## 🐛 Troubleshooting

### Command Not Found

If you get "command not found" after installation, make sure Python's Scripts directory is in your PATH:

**Windows:**
```
C:\Users\<username>\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.x\LocalCache\local-packages\Python3xx\Scripts
```

**Linux/Mac:**
```bash
export PATH="$HOME/.local/bin:$PATH"
```

### npm/flutter Not Found

DevForge checks for required tools before scaffolding. If you see errors about missing tools:

1. Install the required tool (Node.js, Flutter, etc.)
2. Restart your terminal
3. Try the command again

## 📄 License

MIT License - feel free to use this in your own projects!

## 👨‍💻 Author

**Isaka Mtweve**
- Email: isakamtweve69@gmail.com

## 🌟 Show Your Support

If you find DevForge helpful, consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting new features
- 🤝 Contributing code

---

**Happy Forging! 🔥**
