import re
import sys
from argparse import ArgumentParser
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Directory:
    name: str
    files: list['File'] = field(default_factory=list)


@dataclass
class File:
    name: str
    substitute: list['Substitution'] = field(default_factory=list)
    remove_content: list[str] = field(default_factory=list)


@dataclass
class Substitution:
    regex: re.Pattern
    replacement: str


def main():
    cli = parse_program_arguments()
    print(f"a| {cli.name} |a")
    root = Directory('..', [
        File('CMakeLists.txt',
             substitute=[
                 Substitution(re.compile(r'EigenSample'), cli.name)],
             remove_content=['comments']),
        File('conanfile.txt',
             remove_content=[op_label for (condition, op_label) in (
                 (cli.rm_tests, 'tests'),
                 (cli.rm_benchmarks, 'benchmarks'),
                 (cli.rm_windows, 'windows')
             ) if condition])
    ])
    process_directory(root)


def parse_program_arguments():
    parser = ArgumentParser(description='''This program will remove components
        from the host project to simplify it for use in another project by
        another name. It is carving a new project from a template project.
    ''')
    parser.add_argument('name', metavar='project_name', nargs='?', help='Name of the new project')
    parser.add_argument('lib', metavar='library_name', nargs='?', help='Name of the source library, none if omitted')
    parser.add_argument('-a', '--all', action='store_true',
                        help='Change only the project name. Supersedes all other options.')
    parser.add_argument('-b', '--benchmarks', dest='rm_benchmarks', action='store_false')
    parser.add_argument('-p', '--package', dest='rm_package', action='store_false')
    parser.add_argument('-s', '--scripts', dest='rm_scripts', action='store_false')
    parser.add_argument('-t', '--tests', dest='rm_tests', action='store_false')
    parser.add_argument('-w', '--windows', dest='rm_windows', action='store_false')

    if len(sys.argv) <= 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    return parser.parse_args()


def process_directory(dir_: Directory):
    dir_path = Path(dir_.name)
    assert dir_path.exists()

    for file in dir_.files:
        file_path = dir_path / file.name
        assert file_path.exists()
        process_file(file)


def process_file(file: File):
    substitute(file)
    remove_content(file)


def substitute(file: File):
    for sub in file.substitute:
        print(f'in {file.name} replace {sub.regex.pattern} with {sub.replacement}')


def remove_content(file: File):
    for operation in file.remove_content:
        # TODO: All of this stuff
        if operation == 'comments':
            pass


if __name__ == '__main__':
    main()
