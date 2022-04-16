import os
import subprocess

from typing import List

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile import hook


mod = "mod4"
terminal = "kitty"

color = "#458588"
color_light = "#83a598"
color_light2 = "#83a598"
back = "#282828"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus to down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move windows to other windows"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move windows to left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.shrink(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow(),
        desc="Grow window to the right"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    Key([mod], "f", lazy.window.toggle_floating()),

    #  Rofi
    Key([mod], "r", lazy.spawn("rofi -show drun")),
    Key([mod, "shift"], "r", lazy.spawn("rofi -show run")),
    Key([mod], "g", lazy.spawn("rofi -show filebrowser")),
]

__groups = {
    1: Group("TER 🤖"),
    2: Group("WWW 🌐", matches=[Match(wm_class=["firefox"]), Match(wm_class=["google-chrome-stable"])]),
    3: Group("DEV 🌇"),
    4: Group("MUS 💻"),
}
groups = [__groups[i] for i in __groups]


def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]


for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(get_group_key(i.name)), lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1+shift+letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(get_group_key(i.name)),
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.MonadTall(
        border_normal="#222222",
        border_focus="#458587",
        border_width=3,
        single_border_width=3,
        margin=6,
        single_margin=6,
    ),
    layout.Max(),
        # Try more layouts by unleashing below layouts.
    #  layout.Stack(num_stacks=2),
    #  layout.Bsp(),
    #  layout.Matrix(),
    #  layout.MonadWide(),
    #  layout.RatioTile(),
    #  layout.Tile(),
    #  layout.TreeTab(),
    #  layout.VerticalTile(),
    #  layout.Zoomy(),
]

widget_defaults = dict(
    font="SF Pro Display Bold",
    fontsize=12,
    padding=1,
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(
                    highlight_color=[color],
                    highlight_method="line",
                    spacing=0,
                    inactive=color_light2,
                    active=color,
                    block_highlight_text_color="#ffffff",
                    borderwidth=0,
                    padding=10
                ),
                widget.Prompt(),
                widget.WindowName(foreground="#999999"),
                widget.Memory(foreground="#928374"),
                widget.Spacer(length=5),
                widget.CPUGraph(border_color="#504945",fill_color="#504945", graph_color="#928374"),
                    widget.KeyboardLayout(configured_keyboards=["es", "us"],foreground="#a89984", padding=6),
                widget.TextBox(text="", background="#3c3836",
                               foreground="#504945", fontsize=28, padding=0),
                widget.Systray(background="#504945"),
                widget.Spacer(length=10, background="#504945"),

                widget.TextBox(text="", background="#504945",
                               foreground="#a89984", fontsize=28, padding=0),
                widget.Volume(
                    background="#a89984",
                    theme_path="/usr/share/icons/ePapirus/24x24/panel/",
                    padding=0,
                ),
                widget.BatteryIcon(
                    theme_path="/usr/share/icons/ePapirus/24x24/panel/",
                    update_interval=5, background="#a89984", padding=0),
                widget.TextBox(text="", background="#a89984",
                               foreground="#fe8019", fontsize=28, padding=0),

                widget.CheckUpdates(
                    custom_command="checkupdates", 
                    update_interval=1800,
                    background="#fe8019",
                    colour_have_updates="#232323",
                    colour_no_updates="#ff5500",
                    display_format='Actualizaciones: {updates}',
                    padding=10,
                    execute="kitty -e sudo pacman -Suy",
                ),
                widget.TextBox(text="", background="#fe8019",
                               foreground="#fb4934", fontsize=28, padding=0),

                widget.Clock(format='%H:%M', fontsize=16,
                             background="#fb4934", foreground="#232323", padding=10),
            ],
            30,
            background="#3c3836",
            opacity=0.8
        ),
    ),

    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(
                    highlight_color=[color],
                    highlight_method="line",
                    spacing=0,
                    inactive=color_light2,
                    active=color,
                    block_highlight_text_color="#ffffff",
                    borderwidth=0,
                    padding=10
                ),
            ],
            34,
            background="#222222",
            opacity=1
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.fish")
    subprocess.call([home])
