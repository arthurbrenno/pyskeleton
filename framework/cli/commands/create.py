"""Create module"""

import shutil
from pathlib import Path

import click


@click.command(name="res")
@click.argument("resource_name")
def create_resource(resource_name: str):
    """Creates a new resource under app/resources"""
    resource_path = Path("app/resources") / resource_name

    # Check if the resource already exists
    if resource_path.exists():
        click.echo(f"Resource '{resource_name}' already exists.")
        return

    # Correct the template path
    template_path = Path("framework/templates/resources")

    # Copy template content to the new resource folder
    shutil.copytree(template_path, resource_path)

    click.echo(f"Resource '{resource_name}' created successfully.")
