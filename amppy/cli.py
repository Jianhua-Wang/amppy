"""Console script for amppy."""

import typer

app = typer.Typer()

def main():
    """Main entrypoint."""
    typer.echo("amppy")
    typer.echo("=" * len("amppy"))
    typer.echo("A QC tool for amplicon sequencing")


if __name__ == "__main__":
   app(main)