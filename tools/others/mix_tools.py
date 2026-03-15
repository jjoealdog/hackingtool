# coding=utf-8
from core import HackingTool
from core import HackingToolsCollection

from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich import box

_theme = Theme({"purple": "#7B61FF"})
console = Console(theme=_theme)


class TerminalMultiplexer(HackingTool):
    TITLE = "Terminal Multiplexer"
    DESCRIPTION = (
        "Terminal Multiplexer (tilix) is a tiling terminal emulator that "
        "allows opening several terminal sessions inside one window."
    )
    # Bug 19 fix: tilix is a Debian/Ubuntu package only — mark Linux-only
    INSTALL_COMMANDS = ["sudo apt-get install -y tilix"]
    SUPPORTED_OS = ["linux"]

    def __init__(self):
        # Py3-4 fix: super(TerminalMultiplexer, self) → super()
        super().__init__(runnable=False)


class Crivo(HackingTool):
    TITLE = "Crivo"
    DESCRIPTION = (
        "A tool for extracting and filtering URLs, IPs, domains, and subdomains\n"
        "from web pages or text, with built-in web scraping capabilities.\n"
        "See: python3 crivo_cli.py -h"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/GMDSantana/crivo.git",
        # Bug 18 verify: this is correct — cd and pip in same string works
        "cd crivo && pip install --user -r requirements.txt",
    ]
    PROJECT_URL = "https://github.com/GMDSantana/crivo"

    def __init__(self):
        # Py3-4 fix: super(Crivo, self) → super()
        super().__init__(runnable=False)


class MixTools(HackingToolsCollection):
    TITLE = "Mix tools"
    TOOLS = [
        TerminalMultiplexer(),
        Crivo()
    ]

    def pretty_print(self):
        table = Table(title="Mix Tools", show_lines=True, expand=True)
        table.add_column("Title", style="purple", no_wrap=True)
        table.add_column("Description", style="purple")
        table.add_column("Project URL", style="purple", no_wrap=True)

        for t in self.TOOLS:
            desc = getattr(t, "DESCRIPTION", "") or ""
            url = getattr(t, "PROJECT_URL", "") or ""
            table.add_row(t.TITLE, desc.strip().replace("\n", " "), url)

        panel = Panel(table, title="[purple]Available Tools[/purple]", border_style="purple")
        console.print(panel)

    def show_options(self, parent=None):
        console.print("\n")
        panel = Panel.fit("[bold magenta]Mix Tools Collection[/bold magenta]\n"
                          "Select a tool to view details or run it.",
                          border_style="purple")
        console.print(panel)

        table = Table(title="[bold cyan]Available Tools[/bold cyan]", show_lines=True, expand=True)
        table.add_column("Index", justify="center", style="bold yellow")
        table.add_column("Tool Name", justify="left", style="bold green")
        table.add_column("Description", justify="left", style="white")

        for i, tool in enumerate(self.TOOLS):
            title = getattr(tool, "TITLE", tool.__class__.__name__)
            desc = getattr(tool, "DESCRIPTION", "—")
            table.add_row(str(i + 1), title, desc or "—")

        table.add_row("[red]99[/red]", "[bold red]Exit[/bold red]", "Return to previous menu")
        console.print(table)

        try:
            choice = Prompt.ask("[bold cyan]Select a tool to view/run[/bold cyan]", default="99")
            choice = int(choice)
            if 1 <= choice <= len(self.TOOLS):
                selected = self.TOOLS[choice - 1]
                if hasattr(selected, "show_options"):
                    selected.show_options(parent=self)
                elif hasattr(selected, "run"):
                    selected.run()
                elif hasattr(selected, "show_info"):
                    selected.show_info()
                else:
                    console.print("[bold yellow]Selected tool has no runnable interface.[/bold yellow]")
            elif choice == 99:
                return 99
        except Exception:
            console.print("[bold red]Invalid choice. Try again.[/bold red]")
        return self.show_options(parent=parent)


if __name__ == "__main__":
    tools = MixTools()
    tools.pretty_print()
    tools.show_options()