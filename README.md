# Taskli
taskli or `task-li` is a simple python cli app to maintain a simple no bs todo list

## Installation
1. Using pip and a virtual environment
```bash
#clone this repo
git clone https://github.com/Sagetrash/taskli.git
cd taskli

#create a python virtual environment, this protects your universal python environment from package corruption
python -m venv .venv #or python3 for some users
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

#install the package using pip
pip install . 
```
2. using uv (universal install without cloning repo)
```bash
#use uv to install taskli globally without having to clone the repo
uv tool install git+https://github.com/Sagetrash/taskli.git
```

## Commands
### `taskli`
___

**Usage**:

```console
$ taskli [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `add`: adds a new task to the json file
* `mark`: change the status of any task
* `lst`: displays a table for the tasks in the...
* `update`: Update a task, i.e change it&#x27;s description...
* `delete`: delete a specific task using its tid

#### `taskli add`
___
adds a new task to the json file

**Usage**:

```console
$ taskli add [OPTIONS] DESC
```

**Arguments**:

* `DESC`: [required]

**Options**:

* `--help`: Show this message and exit.

#### `taskli mark`
___
change the status of any task

**Usage**:

```console
$ taskli mark [OPTIONS] STATE:{todo|done|in-progress} TID
```

**Arguments**:

* `STATE:{todo|done|in-progress}`: [required]
* `TID`: [required]

**Options**:

* `--help`: Show this message and exit.

#### `taskli lst`
___
displays a table for the tasks in the database

**Usage**:

```console
$ taskli lst [OPTIONS] [STATE]:[todo|done|in-progress]
```

**Arguments**:

* `[STATE]:[todo|done|in-progress]`

**Options**:

* `--help`: Show this message and exit.

#### `taskli update`
___
Update a task, i.e change it&#x27;s description essentially.

**Usage**:

```console
$ taskli update [OPTIONS] TID DESC
```

**Arguments**:

* `TID`: [required]
* `DESC`: [required]

**Options**:

* `--help`: Show this message and exit.

#### `taskli delete`
___
delete a specific task using its tid

**Usage**:

```console
$ taskli delete [OPTIONS] TID
```

**Arguments**:

* `TID`: [required]

**Options**:

* `--help`: Show this message and exit.
