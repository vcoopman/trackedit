logo = """
  __                        __              .___.__  __   
_/  |_____________    ____ |  | __ ____   __| _/|__|/  |_ 
\   __\_  __ \__  \ _/ ___\|  |/ // __ \ / __ | |  \   __\
 |  |  |  | \// __ \\  \___|    <\  ___// /_/ | |  ||  |  
 |__|  |__|  (____  /\___  >__|_ \\___  >____ | |__||__|  
                  \/     \/     \/    \/     \/           

"""

import os
from optparse import OptionParser
import sys

usage = f"""
trackedit [ FILE(S) ] [-v/--verbose] [--deploy] <ENV>

Track file changes. Receive automatic updates on deployed files. Deploy files to new hosts. 

Examples:
=========
    trackedit /etc/dhcpd/host.conf
    trackedit /etc/dhcpd/host.conf --editor nano
    trackedit --push <ENV>
    trackedit --pull <ENV>
    trackedit --deploy <ENV> 

"""
parser = OptionParser(usage)
parser.add_option("--push", dest="push", metavar="PUSH",
                  default=False, action="store_true", help="Push enviroment to repository.")
parser.add_option("--pull", dest="pull", metavar="PULL",
                  default=False, action="store_true", help="Push enviroment from repository.")
parser.add_option("--deploy", dest="deploy", metavar="DEPLOY",
                  default=False, action="store_true", help="Deploys enviroment from repository to host.")
parser.add_option("-v", "--verbose", dest="verbose", metavar="VERBOSE",
                  default=False, action="store_true", help="If more verbose output.")

(options, args) = parser.parse_args()

# What do I need to implement: edit
# ---------------
#
# Enviroment deployed [  ]
#   - Location to store repo in host [  ]
#   - Files deployed in right location in host [  ] 
# 

PATH_HOST_REPOSITORY_HOME = "/tmp"
DEFAULT_TRACKEDIT_CONFIG_PATH = "/tmp"

def execute_cmd(cmd):
    #TODO
    pass

def environment_is_deployed(environment_name):
    #TODO
    pass

def get_trackedit_configuration(conf_path):
    """
    Reads trackedit configuration from conf_path.
    conf_path points to a .json file.
    """
    config = {}

    # TODO

    return config

def clone_environment_repository(configuration, environment_name):
    """
    Clones enviroment repository from remote source to host.
    """
    url_repo = configuration['ENVIRONMENT'][environment_name]['REPOSITORY'][['URL']]
    repository_host_location = configuration['ENVIRONMENT'][environment_name]['REPOSITORY']['HOST_LOCATION']
    execute_cmd(f"git clone {url_repo} --to {repository_host_location}")

def install_environment_from_repository(configuration, environment_name)
    """
    Installs files from the repository of the enviroment to the host.
    """
    # TODO: Improve this names, it could get a bit confusing.
    # A clear difference must be show between where the file is located in the current host (in the repo).
    # And where the file must be located by the installation.
    for file in get_environment_files_path(configuration, environment_name):
        execute_cmd("mv file /tmp/file")
        file_path = get_path_in_enviroment(file)
        execute_cmd("ln -s repository_host_location/file  file_path")

def deploy_environment(configuration, environment_name):
    """
    Deploys enviroment from repository to host.
    It pulls from the repository the files from the environment
    and deploys them in the host.

    "Deployed Files" are files present in the repostiory of the enviroment
    and that have been installed in the host. Installing a file consist of
    saving the original file and creating a symbolic link from the file in
    the repository of the enviroment located in host to the place where this
    file should go in the host.

    Location of files.
        Files are located in the host by copying the structure of the environment.

    """
    clone_environment_repository(configuration, environment_name)
    install_environment_from_repository(configuration, environment_name)


def pull_environment_repository(configuration, enviroment_name)
    """
    Pulls changes into the enviroment repository from its remote source.
    """
    execute_cmd(f"git pull")

def pull_environment(configuration, environment_name):
    """
    Pull changes from remote repository to repository in host.
    Changes in the environment are reflected in the host inmediatly due to
    the installation of files.

    If pulled repository not present, it will be cloned.

    """
    if not environment_is_deployed(environment_name):
        deploy_environment(configuration, environment_name)

    pull_environment_repository(configuration, environment_name)

def main():
    environment_name = "TEST_ENV1"
    configuration = get_trackedit_configuration(DEFAULT_TRACKEDIT_CONFIG_PATH)
    deploy_environment(configuration, environment_name)
