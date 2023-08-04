import os
from contextlib import contextmanager
from pathlib import Path
import subprocess
from typing import Optional, List

@contextmanager
def set_directory(path: Path):
    """Sets the current working path within the context.
    Parameters
    ----------
    path : Path
        The path to the cwd
    Yields
    ------
    None
    
    Examples
    --------
    >>> with set_directory("some_path"):
    ...    do_something()
    """
    cwd = Path().absolute()
    path.mkdir(exist_ok=True, parents=True)
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(cwd)


def run_command(
        cmd: List, 
        stdin: Optional[str] = None,
        shell: Optional[bool] = None,
        print_to_terminal: bool = True
    ):
    
    if print_to_terminal:
        stdout = None
    else:
        stdout = subprocess.PIPE
    
    stderr = subprocess.STDOUT
    
    with subprocess.Popen(
        args=cmd,
        stdin=subprocess.PIPE,
        stdout=stdout,
        stderr=stderr,
        encoding="utf-8",
        shell=shell
    ) as subp:
        out, err = subp.communicate(input=stdin)
        return_code = subp.poll()
    return return_code, out, err


def set_tag(name):
    with open(name, 'w') as _:
        pass


def print_list(alist, by=","):
    string = []
    for aa in alist:
        string.append(str(aa))
    return by.join(string)