# Copyright: (c) 2018, Toshio Kuratomi <tkuratomi@ansible.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

"""
Context of the running Ansible.

In the future we *may* create Context objects to allow running multiple Ansible plays in parallel
with different contexts but that is currently out of scope as the Ansible library is just for
running the ansible command line tools.

These APIs are still in flux so do not use them unless you are willing to update them with every Ansible release
"""

from ansible.arguments.context_objects import CLIArgs, GlobalCLIArgs


# Note: this is not the singleton version.  The Singleton is only created once the program has
# actually parsed the args
CLIARGS = CLIArgs({})


def _init_global_context(cli_args):
    """Initialize the global context objects"""
    global CLIARGS
    CLIARGS = GlobalCLIArgs.from_options(cli_args)
