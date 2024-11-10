from player_utilities import PlayerReader, PlayerStats
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

def main():
    console = Console()
    nationality = Prompt.ask("Enter nationality (e.g., 'FIN' for Finland):", default="FIN").upper()
    season = Prompt.ask("Enter season (e.g., 2023-24):", default="2023-24")
    reader = PlayerReader(season)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    display_players(console, players, nationality, season)

def display_players(console, players, nationality, season):
    table = Table(title=f"Top Scorers for {nationality} in {season}", title_style="bold magenta")
    table.add_column("Rank", justify="center", style="cyan", no_wrap=True)
    table.add_column("Name", style="green", no_wrap=True)
    table.add_column("Team", style="yellow", no_wrap=True)
    table.add_column("Goals", style="blue", no_wrap=True)
    table.add_column("Assists", style="blue", no_wrap=True)
    table.add_column("Points", style="magenta", no_wrap=True)


    for idx, player in enumerate(players, 1):
        table.add_row(
            str(idx),                    
            player.name,                 
            player.team,                 
            str(player.goals),           
            str(player.assists),         
            str(player.points),          
        )
    console.print(table)

if __name__ == "__main__":
    main()
