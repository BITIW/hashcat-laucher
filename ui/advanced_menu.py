import flet as ft

def AdvancedMenu():
    return ft.Column([
        ft.Text("General"),
        ft.Checkbox(label="Quiet", value=True),
        ft.Checkbox(label="Disable Pot File", value=True),
        ft.Checkbox(label="Disable Log File", value=True),
        ft.Checkbox(label="Enable Optimized Kernel", value=True),
        ft.Checkbox(label="Enable Slower Candidate Generators"),
        ft.Checkbox(label="Remove Found Hashes"),
        ft.Checkbox(label="Ignore Usernames"),
        ft.Checkbox(label="Disable Self-Test (Not Recommended)"),
        ft.Checkbox(label="Ignore Warnings (Not Recommended)"),

        ft.Text("Devices"),
        ft.TextField(label="Devices IDs", hint_text="Select Devices IDs"),
        ft.TextField(label="Devices Types", hint_text="Select Devices Types"),
        ft.TextField(label="Workload Profile", hint_text="Select Workload Profile"),

        ft.Text("Markov"),
        ft.Checkbox(label="Disable markov-chains, emulates classic brute-force"),
        ft.Checkbox(label="Enable classic markov-chains, no per-position"),
        ft.TextField(label="Threshold X when to stop accepting new markov-chains", hint_text="0"),

        ft.Text("Monitor"),
        ft.Checkbox(label="Disable Monitor"),
        ft.TextField(label="Temp Abort (°C)", hint_text="Select Temp Abort (°C)"),

        ft.Text("Extra Arguments"),
        ft.TextField(label="Extra Arguments", hint_text="Set Extra Arguments"),

        ft.Text("Misc"),
        ft.TextField(label="Status Timer", hint_text="20 Seconds")
    ])
