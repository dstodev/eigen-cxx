import re
from dataclasses import dataclass, field
from pathlib import Path
from argparse import ArgumentParser


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

    root = Directory('..', [
        File('CMakeLists.txt',
             substitute=[
                 Substitution(re.compile(r'EigenSample'), cli.name)],
             remove_content=['comments']),
        File('conanfile.txt',
             remove_content=[op_label for (condition, op_label) in (
                 (cli.rm_tests, 'tests'),
                 (cli.rm_benchmarks, 'benchmarks'),
                 (cli.rm_dependencies, 'dependencies')
             ) if condition])
    ])
    process_directory(root)


def parse_program_arguments():
    parser = ArgumentParser(description='''This program will remove components
        from the host project to simplify it for use in another project by
        another name. It is carving a new project from a template project.
    ''')

    parser.add_argument('name', metavar='project_name', help='Name of the new project')

    parser.add_argument('-b', '--no-benchmarks', dest='rm_benchmarks', action='store_true')
    parser.add_argument('-d', '--no-dependencies', dest='rm_dependencies', action='store_true')
    parser.add_argument('-e', '--no-eigen-lib', dest='rm_entrypoint', action='store_true')
    parser.add_argument('-p', '--no-packaging', dest='rm_packaging', action='store_true')
    parser.add_argument('-s', '--no-scripts', dest='rm_scripts', action='store_true')
    parser.add_argument('-t', '--no-tests', dest='rm_scripts', action='store_true')
    parser.add_argument('-w', '--no-windows', dest='rm_windows', action='store_true')

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
