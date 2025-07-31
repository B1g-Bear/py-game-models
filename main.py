from db.management.commands.import_players import import_players


def run() -> None:
    import_players()


if __name__ == "__main__":
    run()
