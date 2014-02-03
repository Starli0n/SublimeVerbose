Verbose
=======

Sublime Text plugin which logs messages in `Console` when activated


Description
===========

**Verbose** is used by other plugins to write log messages.
When it is activated, it enables plugins to log verbose messages, especially useful in development step, for debugging.

It enables also to show or hide `Commands` and `Input` in the `Console`.


Package Installation
====================

Bring up a command line in the Packages/ folder of your Sublime user folder, and execute the following:
> git clone https://github.com/Starli0n/verbose.git Verbose


Menu Setting
============

Add entries `Menu` in `View`:

- `Log Verbose` show or hide verbose logs in `Console`
- `Log Commands` show or hide `Commands` in `Console`
- `Log Input` show or hide `Input` in `Console`


Usage
=====

- Log a simple message

> sublime.run_command("verbose", {"log": "Hello World"})


- Log a message prefixed by the name of the plugin

> sublime.run_command("verbose", {"plugin_name": PluginName, "log": "Hello World"})


Version
=======

- **v1.0**

First Release
