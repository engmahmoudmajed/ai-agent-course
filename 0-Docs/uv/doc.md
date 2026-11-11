# UV
**uv is An extremely fast Python package and project manager, written in Rust.**

## how to use it 

### init
#### new project 
to init project in new folder  
```bash
uv init hello-world
cd hello-world
```
to init project in current folder
```bash
uv init .
```

```bash
# This will create 
├── .git/
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
└── src
    └── hello_world
        └── __init__.py
```

### run the project
```bash
uv run hello-world
```
or you can edit 
pyproject.toml

**from**

```toml
[project.scripts]
start-work-with-agent = "hello-world:main"
```

**to** 

```toml
[project.scripts]
# start-work-with-agent = "start_work_with_agent:main"
dev = "hello-world:main"
```

```bash
uv run dev
```

### install packeges 
```bash
uv add requests
```

### remove packege 
```bash
uv remove requests
```

### install and update all packeges 
```bash
uv sync
```


### build dist
```bash
uv build
ls dist/
```
