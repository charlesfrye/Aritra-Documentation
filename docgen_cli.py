import os
import re
import subprocess
from typing import Tuple

#                      (             - Start of capture
#                       .*?          - 0 or more repitions of any character except a new line (non-greedy)
#                          \w        - Not a word character
#                            )       - End of capture
#                              +     - 1 or more repitions of space
#                               (    - Start of capture
#                                .*  - 0 of more repitions of any character except a new line
#                                  ) - End of group
PATTERN = re.compile(r"(.*?\w) +(.*)")
KEYWORDS = ["Options:", "Commands:"]
TEMPLATE = """
# {}

{}

{}

{}

{}
""".strip()


def run_help(command: str) -> str:
    """
    Runs `command --help` and gathers the output.

    Args:
        command: (str) The command eg. wandb in `wandb --help`

    Returns:
        str: The help page of the command.
    """
    help_page = subprocess.run(
        f"{command} --help", shell=True, capture_output=True, text=True
    ).stdout
    return help_page


def parse_help(command: str) -> Tuple[str, str, str]:
    """
    Gathers the help page of the command and then parses it.

    It is noted that the help page is structured in the following manner.
    ```bash
    Usage: ....

    <Summary>

    Options:
    ...

    Commands:
    ...
    ```
    This help page is parsed in Usage, Summary and a Parsed Dict
    that contains Options and Commands.

    Args:
        command (str): The command eg. wandb in `wandb --help`

    Returns:
        str, str, str: usage, summary and the parsed document
    """
    help_page = run_help(command)
    summary = []
    keyword = None  # initializing keyword with None
    parsed_dict = {}  # will hold Options and Commands

    for line in help_page.split("\n"):
        line = line.strip()
        if line in KEYWORDS:  # Keywords contains [Options, Commands]
            parsed_dict[line] = []
            keyword = line
            continue
        if keyword is None:
            summary.append(line)
        else:
            # PATTERN help with option and value
            # eg --version Show the version
            # [("--version","Show the version")]
            extract = PATTERN.findall(line)
            if extract:
                parsed_dict[keyword].append([extract[0][0], extract[0][1]])

    if len(summary) == 0:
        return "", "", parsed_dict
    elif len(summary) == 1:
        return summary[0], "", parsed_dict
    else:
        usage = summary[0]
        summary = "\n".join(summary[1:])
        return usage, summary, parsed_dict


def markdown_render(command: str, output_dir: str, output_file: str) -> str:
    """
    Renders the markdown and also provides
    the commands nested in it.

    Args:
        command (str): The command that is executed `wandb command --help`
        output_file (str): The file in which the markdown is written.

    Returns:
        str: The output directory
    """
    usage, summary, parsed_dict = parse_help(command)
    if usage:
        # Document usage
        usage = usage.split(":")
        usage = f"**Usage**\n\n`{usage[1]}`"
    if summary:
        # Document summary
        summary = f"**Summary**\n{summary}"
    options = ""
    if "Options:" in parsed_dict.keys():
        # Document options
        for element in parsed_dict.get("Options:"):
            des = (
                " ".join(list(filter(lambda x: x, element[1].split(" ")[1:])))
                if element[1]
                .split(" ")[0]
                .isupper()  # to check for types in help page eg. --version INTEGER the version
                else element[1]
            )
            # concatenate all the options
            options += f"""|{element[0]}|{des}|\n"""
        options = (
            """**Options**\n| **Options** | **Description** |\n|:--|:--|:--|\n"""
            + options
        )

    commands = ""
    command_list = []
    if "Commands:" in parsed_dict.keys():
        # Document commands
        for element in parsed_dict.get("Commands:"):
            command_list.append(
                f"{command} {element[0]}"
            )  # Keeping a list of all the nested counts
            des = (
                " ".join(list(filter(lambda x: x, element[1].split(" ")[1:])))
                if element[1]
                .split(" ")[0]
                .isupper()  # to check for types in help page eg. --version INTEGER the version
                else element[1]
            )
            # concatenate all the options
            commands += f"""|{element[0]}|{des}|\n"""
        commands = (
            """**Commands**\n| **Commands** | **Description** |\n|:--|:--|:--|\n"""
            + commands
        )

    # Write to the output file
    if usage or summary or options or commands:
        with open(output_file, "w") as fp:
            fp.write(
                TEMPLATE.format(
                    command,  # Heading
                    usage,  # Usage
                    summary,  # Summary
                    options,  # Options
                    commands,  # Commands
                )
            )

    if len(command_list) > 0:
        for command in command_list:
            # For `command --help`
            command_file_name = "-".join(command.split(" "))
            output_dir = os.path.join(output_dir, f"{command_file_name}")
            os.mkdir(path=output_dir)
            output_file = os.path.join(output_dir, "README.md")
            output_dir = markdown_render(
                command=command, output_dir=output_dir, output_file=output_file
            )

    else:
        # BASE CONDITION TO STOP RECURSION
        parent_path = os.path.dirname(output_dir)
        return parent_path
    # Return the parent directory
    parent_path = os.path.dirname(output_dir)
    return parent_path


def build(output_dir: str = None):
    """
    Entry point for docgen_cli.
    Builds the entire documentation for `wandb` CLI.

    Args:
        output_dir: (str) The output directory for the generated CLI docs.
    """
    if output_dir is None:
        output_dir = os.getcwd()

    # For `wandb --help`
    output_dir = os.path.join(output_dir, "cli")
    os.mkdir(path=output_dir)
    output_file = os.path.join(output_dir, "README.md")
    output_dir = markdown_render(
        command="wandb", output_dir=output_dir, output_file=output_file
    )
