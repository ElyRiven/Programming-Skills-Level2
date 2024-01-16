TEAMS = [{"manchester united": 0}, {"liverpool": 0}, {"arsenal": 0}, {"chelsea": 0}, {"manchester city": 0}, {"tottenham hotspur": 0}]
import random

def main():
    print("\t\tThe Big Six of the English Premier League Begins!!!\n\n")
    matches = 0
    for i in range(len(TEAMS)):
        team1 = list(TEAMS[i].keys())[0]
        print(f"Team {team1.title()} plays against the other teams")
        for x in range(3):
            for j in range(i+1,len(TEAMS)):
                team2 = list(TEAMS[j].keys())[0]
                TEAMS[i][team1] += generatePoints()
                TEAMS[j][team2] += generatePoints()
                matches += 1
    sorted_teams = sorted(TEAMS, key=lambda team: list(team.values())[0], reverse=True)
    print("\n\nThe final standings are: \n")
    for i in range(len(sorted_teams)):
        print(f"{i+1}. {list(sorted_teams[i].keys())[0]}: {list(sorted_teams[i].values())[0]}")
    print(f"\nTotal matches played: {matches}")

# Generate a random number between 0 and 3
def generatePoints():
    return random.randint(0,3)

if __name__ == "__main__":
    main()