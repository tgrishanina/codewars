def compute_ranks(number, games):
    # Initialize lists for points, goal differentials, and total goals
    points = [0] * number
    goal_differentials = [0] * number
    total_goals = [0] * number
    
    # Process each game to update points, goal differentials, and total goals
    for game in games:
        team1, team2, score1, score2 = game
        if score1 > score2:
            points[team1] += 2
        elif score2 > score1:
            points[team2] += 2
        else:
            points[team1] += 1
            points[team2] += 1
        
        goal_differentials[team1] += (score1 - score2)
        goal_differentials[team2] += (score2 - score1)
        total_goals[team1] += score1
        total_goals[team2] += score2
    
    # Create a list of teams with their respective stats
    team_stats = [
        (i, points[i], goal_differentials[i], total_goals[i])
        for i in range(number)
    ]
    
    # Sort teams by total points, goal differential, and total goals (all in descending order)
    sorted_teams = sorted(team_stats, key=lambda x: (x[1], x[2], x[3]), reverse=True)
    
    # Create a ranking dictionary
    rank_dict = {}
    current_rank = 1
    for i, (team, pt, gd, tg) in enumerate(sorted_teams):
        if i > 0 and (pt == sorted_teams[i - 1][1] and gd == sorted_teams[i - 1][2] and tg == sorted_teams[i - 1][3]):
            rank_dict[team] = rank_dict[sorted_teams[i - 1][0]]
        else:
            rank_dict[team] = current_rank
        current_rank += 1
    
    # Return the ranks based on the original team order
    return [rank_dict[i] for i in range(number)]   
