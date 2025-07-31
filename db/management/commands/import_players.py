import json
from pathlib import Path

from django.core.management.base import BaseCommand
from db.models import Race, Skill, Guild, Player


def import_players() -> None:
    file_path = Path("players.json")

    with file_path.open(encoding="utf-8") as file:
        players_data = json.load(file)

    for player_data in players_data:
        race, _ = Race.objects.get_or_create(name=player_data["race"])
        guild = None

        if guild_name := player_data.get("guild"):
            guild, _ = Guild.objects.get_or_create(name=guild_name)

        player, _ = Player.objects.get_or_create(
            nickname=player_data["nickname"],
            defaults={
                "race": race,
                "guild": guild,
                "level": player_data["level"],
            },
        )

        for skill_name in player_data["skills"]:
            skill, _ = Skill.objects.get_or_create(name=skill_name)
            player.skills.add(skill)


class Command(BaseCommand):
    def handle(self, *args, **options) -> None:
        import_players()
