"""Entrypoint of the CLI"""
import click

from .commands import create as create_commands
from .commands import delete as delete_commands


@click.group()
def framework():
    """Framework commands."""


@click.group()
def create():
    """Create commands."""


@click.group()
def delete():
    """Delete commands."""


create.add_command(create_commands.create_resource)
delete.add_command(delete_commands.delete_resource)

framework.add_command(create)
framework.add_command(delete)
