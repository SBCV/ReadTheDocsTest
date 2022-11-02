import subprocess
from subprocess import PIPE
import sys
import json

def print_command_line_sys_path():
    script_str = "import sys; import json; pickled_str = json.dumps(sys.path); print(pickled_str)"
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            script_str
        ],
        # capture_output=True,      # For Python 3.7 onwards
        # text=True                 # For Python 3.7 onwards
        stdout=PIPE,                # For Python 3.6 and earlier
        stderr=PIPE              # For Python 3.6 and earlier
    )
    print(result.stdout)

    deserialized_paths = json.loads(result.stdout)
    print(type(deserialized_paths))
    print(len(deserialized_paths))
    # print("deserialized_path\n", deserialized_paths)

    reference_paths = sys.path
    # print("reference_paths\n", reference_paths)
    # print(len(reference_paths))   


print_command_line_sys_path()