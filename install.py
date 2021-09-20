import sys
import subprocess
import pkg_resources

required = {'selenium','pywin32'} 
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed


if missing:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',*missing])