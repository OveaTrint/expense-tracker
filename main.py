from commands.add import add
from commands.list import list
from commands.delete import delete
from commands.summary import summary

from argparse import ArgumentParser

parser = ArgumentParser(prog="expense-tracker", description="A cli app that helps users manage their expenses")
