"""Delete module"""

import shutil
from pathlib import Path

import click


@click.command(name="res")
@click.argument("resource_name")
def delete_resource(resource_name: str):
    """Delete an existing resource from app/resources."""
    resource_path = Path("app/resources") / resource_name

    # Check if the resource exists
    if not resource_path.exists():
        click.echo(f"Resource '{resource_name}' does not exist.")
        return

    # Delete the resource folder
    shutil.rmtree(resource_path)

    click.echo(f"Resource '{resource_name}' deleted successfully.")
