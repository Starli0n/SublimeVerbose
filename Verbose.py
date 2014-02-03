import sublime, sublime_plugin

PluginName = 'Verbose'

g_bVerbose = False
g_bCommands = False
g_bInput = False


class Initialize:
    @staticmethod
    def run():
        global g_bVerbose
        global g_bCommands
        global g_bInput
        g_bVerbose = False
        g_bCommands = False
        g_bInput = False
        sublime.log_commands(g_bCommands)
        sublime.log_input(g_bInput)

Initialize.run()


def ToggleVerbose():
    global g_bVerbose
    g_bVerbose = not g_bVerbose


def ToggleCommands():
    global g_bCommands
    g_bCommands = not g_bCommands
    sublime.log_commands(g_bCommands)


def ToggleInput():
    global g_bInput
    g_bInput = not g_bInput
    sublime.log_input(g_bInput)


class VerboseCommand(sublime_plugin.ApplicationCommand):
    def run(self, log, plugin_name = None):
        if plugin_name:
            print plugin_name + ": " + log
        else:
            print log

    def is_enabled(self):
        return g_bVerbose


class VerboseToggleCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        ToggleVerbose()

    def is_checked(self):
        return g_bVerbose


class VerboseCommandsToggleCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        ToggleCommands()

    def is_checked(self):
        return g_bCommands


class VerboseInputToggleCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        ToggleInput()

    def is_checked(self):
        return g_bInput
