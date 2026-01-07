# Taskli

taskli or `task-li` is a simple python cli app to maintain a simple no bs todo list for a [project from roadmap.sh](https://roadmap.sh/projects/task-tracker)

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

---

**Usage**:

```console
$ taskli [OPTIONS] COMMAND [ARGS]...
```

**Options**:

- `--install-completion`: Install completion for the current shell.
- `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
- `--help`: Show this message and exit.

**Commands**:

- `add`: ADD a new task
- `delete`: DELETE a task using its id
- `update`: update/chanfe a task&#x27;s descritption
- `mark`: Update/Change a task&#x27;s status...
- `list`: show a table of tasks

---

### `taskli add`

---

ADD a new task

**Usage**:

```console
$ taskli add [OPTIONS] TASKDESC
```

**Arguments**:

- `TASKDESC`: the task description [required]

**Options**:

- `--help`: Show this message and exit.

---

### `taskli delete`

---

DELETE a task using its id

**Usage**:

```console
$ taskli delete [OPTIONS] TASKID
```

**Arguments**:

- `TASKID`: Enter the task&#x27;s id [required]

**Options**:

- `--help`: Show this message and exit.

---

### `taskli update`

---

update/chanfe a task&#x27;s descritption

**Usage**:

```console
$ taskli update [OPTIONS] TASKID TASKDESC
```

**Arguments**:

- `TASKID`: Enter the Task&#x27;s id [required]
- `TASKDESC`: new DESCRIPTION for the task [required]

**Options**:

- `--help`: Show this message and exit.

---

### `taskli mark`

---

Update/Change a task&#x27;s status

**Usage**:

```console
$ taskli mark [OPTIONS] TASKID STATUS:{todo|in-progress|done}
```

**Arguments**:

- `TASKID`: Enter the task&#x27;s id [required]
- `STATUS:{todo|in-progress|done}`: change the status of a given task [required]

**Options**:

- `--help`: Show this message and exit.

---

### `taskli list`

---

show a table of tasks

**Usage**:

```console
$ taskli list [OPTIONS] [STATUS]:[todo|in-progress|done]
```

**Arguments**:

- `[STATUS]:[todo|in-progress|done]`: filter tasks by status

**Options**:

- `--help`: Show this message and exit.
