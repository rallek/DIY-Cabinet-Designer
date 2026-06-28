import adsk.core
import traceback


COMMAND_ID = "diy_cabinet_designer_prototype_command"
COMMAND_NAME = "DIY Cabinet Designer"
COMMAND_DESCRIPTION = "Starts the DIY Cabinet Designer prototype command."
WORKSPACE_ID = "FusionSolidEnvironment"
PANEL_ID = "SolidScriptsAddinsPanel"

_handlers = []


class CommandCreatedHandler(adsk.core.CommandCreatedEventHandler):
    def notify(self, args):
        try:
            command = args.command
            execute_handler = CommandExecuteHandler()
            command.execute.add(execute_handler)
            _handlers.append(execute_handler)
        except Exception:
            _show_error()


class CommandExecuteHandler(adsk.core.CommandEventHandler):
    def notify(self, args):
        try:
            app = adsk.core.Application.get()
            ui = app.userInterface
            ui.messageBox("DIY Cabinet Designer prototype command started.")
        except Exception:
            _show_error()


def run(context):
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        command_definition = ui.commandDefinitions.itemById(COMMAND_ID)
        if not command_definition:
            command_definition = ui.commandDefinitions.addButtonDefinition(
                COMMAND_ID,
                COMMAND_NAME,
                COMMAND_DESCRIPTION,
            )

        created_handler = CommandCreatedHandler()
        command_definition.commandCreated.add(created_handler)
        _handlers.append(created_handler)

        panel = _get_target_panel(ui)
        control = panel.controls.itemById(COMMAND_ID)
        if not control:
            panel.controls.addCommand(command_definition)
    except Exception:
        _show_error()


def stop(context):
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        panel = _get_target_panel(ui)
        control = panel.controls.itemById(COMMAND_ID)
        if control:
            control.deleteMe()

        command_definition = ui.commandDefinitions.itemById(COMMAND_ID)
        if command_definition:
            command_definition.deleteMe()
    except Exception:
        _show_error()


def _get_target_panel(ui):
    workspace = ui.workspaces.itemById(WORKSPACE_ID)
    return workspace.toolbarPanels.itemById(PANEL_ID)


def _show_error():
    app = adsk.core.Application.get()
    if app and app.userInterface:
        app.userInterface.messageBox("DIY Cabinet Designer add-in error:\n{}".format(traceback.format_exc()))
