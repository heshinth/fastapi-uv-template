# FastAPI uv Template

A  FastAPI project template powered by [Copier](https://copier.readthedocs.io/) and [uv](https://github.com/astral-sh/uv).


## Requirements

To use this Copier template, you will need:

- **Git v2**
- **Python 3**
- **Copier**

To install Git version 2, follow the [official instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

To install Python 3, download and install it from the [official website](https://www.python.org/downloads/), or install it with uv:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install 3.12
```

To install Copier, use uv or pipx:

```sh
uv tool install copier --with copier-templates-extensions
```

Or with pipx:

```sh
pipx install copier
pipx inject copier copier-templates-extensions
```

## Usage

### 1. Generate a New Project

To generate a project, run one of the following commands:

```sh
copier copy --trust "https://github.com/pawamoy/copier-uv.git" /path/to/your/new/project
```

Or with a shorter command:

```sh
copier copy --trust "gh:pawamoy/copier-uv" /path/to/your/new/project
```

You can even generate a project without installing Copier, using uv:

```sh
uvx --with copier-templates-extensions copier copy --trust "gh:pawamoy/copier-uv" /path/to/your/new/project
```

Replace `/path/to/your/new/project` with the desired path for your project.

### 2. Navigate to Your Project Directory

```sh
cd /path/to/your/new/project
```

### 3. Install Dependencies

Install the project dependencies using uv:

```sh
uv sync
```

### 4. Run the Development Server

```sh
uv run fastapi dev ./app/main.py
```

Your FastAPI application will be running at `http://127.0.0.1:8000`.