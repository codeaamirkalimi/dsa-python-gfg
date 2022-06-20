# {
#   "competitions": [
#     ["HTML", "C#"],
#     ["C#", "Python"],
#     ["Python", "HTML"]
#   ],
#   "results": [0, 0, 1]
#  }

def updateScore(winningTeam, point, scores):
    if winningTeam not in scores:
        scores[winningTeam] = 0
    scores[winningTeam] += point


def winners(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}
    for i, competition in enumerate(competitions):
        # print(i, competition)
        homeTeam, awayTeam = competition
        # print(homeTeam, awayTeam)
        winningTeam = homeTeam if results[i] == 1 else awayTeam
        updateScore(winningTeam, 3, scores)
        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam
    return currentBestTeam


def Tournament():
    competitions = [["HTML", "C#"],
                    ["C#", "Python"],
                    ["Python", "HTML"]]
    results = [0, 0, 1]
    result = winners(competitions, results)
    print(result)


if __name__ == '__main__':
    Tournament()
