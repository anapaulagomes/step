import typer


app = typer.Typer()


@app.command()
def main(package_name: str, markdown_checklist: str, dry_run: bool = False):
    print(f"Package name: {package_name}")


if __name__ == "__main__":
    app()
