import json
from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for username, pdata in data.items():
        race_data = pdata["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description")},
        )

        guild_data = pdata.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")},
            )

        player = Player.objects.create(
            nickname=username,
            email=pdata["email"],
            bio=pdata.get("bio"),
            race=race,
            guild=guild,
        )

        for skill_data in race_data.get("skills", []):
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data.get("bonus"), "race": race},
            )
            player.skills.add(skill)

        player.save()


if __name__ == "__main__":
    main()
