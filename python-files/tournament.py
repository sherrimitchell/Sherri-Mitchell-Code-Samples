# Simulate a sports tournament

import csv
import sys
import random
from sys import argv

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    filename = argv[1]

    # convert rating to an int
    teams = []
    # TODO: Read teams into memory from file
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        next(reader)
        for team in reader:
            team["rating"] = int(team["rating"])

            teams.append(team)

    # print teams
    for team in teams:
        print(team)

    counts = {}
    # TODO: Simulate N tournaments and keep track of win counts
    for i in range(N):
        # returns the winning team of the tournament
        winner = simulate_tournament(teams)
        # increment counts based on wins
        if winner in counts:
            counts[winner] += 1
        else:
            counts[winner] = 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO
    # for all the teams in the list
    #   simulate round for each pair of teams
    #       until the number of teams = 1
    # return the name of the winning team

    while len(teams) < 1:
        teams = simulate_round(team)

    return teams[0]["team"]


if __name__ == "__main__":
    main()
