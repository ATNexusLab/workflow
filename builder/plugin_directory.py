import shutil
from pathlib import Path, PurePosixPath


def replace(root: Path, harness: str, files: dict[PurePosixPath, bytes]) -> None:
    directory = root / "plugins" / harness
    if directory.exists():
        shutil.rmtree(directory)
    for path, content in files.items():
        target = directory / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)


def differences(root: Path, harness: str, files: dict[PurePosixPath, bytes]) -> list[str]:
    directory = root / "plugins" / harness
    committed = {
        PurePosixPath(path.relative_to(directory).as_posix())
        for path in directory.rglob("*")
        if path.is_file()
    }
    found: list[str] = []
    for path in sorted(files.keys() | committed):
        if path not in committed:
            found.append(f"plugins/{harness}/{path}: is missing")
        elif path not in files:
            found.append(f"plugins/{harness}/{path}: is not produced by the build")
        elif (directory / path).read_bytes() != files[path]:
            found.append(f"plugins/{harness}/{path}: differs from a fresh build")
    return found
