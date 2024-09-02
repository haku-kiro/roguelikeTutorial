import tcod


from actions import EscapeAction, MovementAction
from entity import Entity
from input_handlers import EventHandler


def main():
    screen_width = 80
    screen_height = 50

    player_x = screen_width // 2
    player_y = screen_height // 2

    npc_x = screen_width // 2 - 5
    npc_y = screen_height // 2

    tileset = tcod.tileset.load_tilesheet(
        "./dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(player_x, player_y, "@", (255, 255, 255))
    npc = Entity(npc_x, npc_y, "@", (255, 255, 0))

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(
            screen_width, screen_height, order="F"
        )

        while True:
            root_console.print(
                x=player.x,
                y=player.y,
                string=player.char,
                fg=player.colour
            )

            context.present(root_console)

            root_console.clear()

            for event in tcod.event.wait():
                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player.move(dx=action.dx, dy=action.dy)

                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()
