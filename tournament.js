function tournament(competitions, results) {
    let homeTeam = {};
    let awayTeam = {};
    for (let i = 0; i < competitions.length; i++) {
        if (!homeTeam[competitions[i][0]]) {
            homeTeam[competitions[i][0]] = 0
        }
        if (!awayTeam[competitions[i][1]]) {
            awayTeam[competitions[i][1]] = 0
        }
    }
    for (let i = 0; i < results.length; i++) {
        if (results[i] == 0) {
            awayTeam[competitions]
        }
    }
    console.log({homeTeam, awayTeam});
}

let competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
  ]

let results = [0, 0, 1];
tournament(competitions, results)