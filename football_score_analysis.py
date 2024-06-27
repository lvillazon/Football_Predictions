# Euros scores analysis

import random

# Population data (in millions)
# Combined population data (in millions)
population = {
    "Argentina": 45,  # Population in millions
    "Germany": 83,
    "Scotland": 5.5,
    "Hungary": 9.6,
    "Switzerland": 8.6,
    "Spain": 47,
    "Croatia": 4,
    "Italy": 60,
    "Albania": 2.8,
    "Poland": 38,
    "Netherlands": 17,
    "Slovenia": 2.1,
    "Denmark": 5.8,
    "Serbia": 6.7,
    "England": 56,
    "Romania": 19,
    "Ukraine": 41,
    "Belgium": 11.5,
    "Slovakia": 5.4,
    "France": 67,
    "Turkey": 84,
    "Georgia": 3.7,
    "Portugal": 10,
    "Austria": 9,
    "Czech Republic": 10.7,
    "Saudi Arabia": 35,
    "Mexico": 126,
    "Tunisia": 12,
    "Australia": 26,
    "Japan": 125,
    "Costa Rica": 5.1,
    "Morocco": 37,
    "Canada": 38,
    "Cameroon": 27,
    "Brazil": 214,
    "South Korea": 52,
    "Ghana": 32,
    "Uruguay": 3.5
}


# Match results with teams
euro_2024_group_stage = [
    ((5, 1), "Germany", "Scotland"),
    ((1, 3), "Hungary", "Switzerland"),
    ((3, 0), "Spain", "Croatia"),
    ((2, 1), "Italy", "Albania"),
    ((1, 2), "Poland", "Netherlands"),
    ((1, 1), "Slovenia", "Denmark"),
    ((0, 1), "Serbia", "England"),
    ((3, 0), "Romania", "Ukraine"),
    ((0, 1), "Belgium", "Slovakia"),
    ((0, 1), "Austria", "France"),
    ((3, 1), "Turkey", "Georgia"),
    ((2, 1), "Portugal", "Czech Republic"),
    ((2, 2), "Croatia", "Albania"),
    ((2, 0), "Germany", "Hungary"),
    ((1, 1), "Scotland", "Switzerland"),
    ((1, 1), "Slovenia", "Serbia"),
    ((1, 1), "Denmark", "England"),
    ((1, 0), "Spain", "Italy"),
    ((1, 2), "Slovakia", "Ukraine"),
    ((1, 3), "Poland", "Austria"),
    ((0, 0), "Netherlands", "France"),
    ((1, 1), "Georgia", "Czech Republic"),
    ((0, 3), "Turkey", "Portugal"),
    ((2, 0), "Belgium", "Romania"),
    ((1, 1), "Switzerland", "Germany"),
    ((0, 1), "Scotland", "Hungary"),
    ((1, 1), "Croatia", "Italy"),
    ((0, 1), "Albania", "Spain"),
    ((3, 2), "Austria", "Netherlands"),
    ((1, 1), "France", "Poland"),
    ((0, 0), "England", "Slovenia"),
    ((0, 0), "Denmark", "Serbia"),
    ((1, 1), "Slovakia", "Romania"),
    ((0, 0), "Ukraine", "Belgium"),
    ((1, 2), "Czech Republic", "Turkey"),
    ((2, 0), "Georgia", "Portugal")
]

world_cup_2022_group_stage = [
    ((1, 2), "Argentina", "Saudi Arabia"),
    ((0, 0), "Mexico", "Poland"),
    ((2, 0), "Poland", "Saudi Arabia"),
    ((2, 0), "Argentina", "Mexico"),
    ((0, 2), "Poland", "Argentina"),
    ((2, 1), "Saudi Arabia", "Mexico"),
    ((0, 0), "Denmark", "Tunisia"),
    ((4, 1), "France", "Australia"),
    ((0, 1), "Tunisia", "Australia"),
    ((2, 1), "France", "Denmark"),
    ((1, 0), "Australia", "Denmark"),
    ((1, 0), "Tunisia", "France"),
    ((1, 2), "Germany", "Japan"),
    ((7, 0), "Spain", "Costa Rica"),
    ((0, 1), "Japan", "Costa Rica"),
    ((1, 1), "Spain", "Germany"),
    ((2, 1), "Japan", "Spain"),
    ((4, 2), "Germany", "Costa Rica"),
    ((0, 0), "Morocco", "Croatia"),
    ((1, 0), "Belgium", "Canada"),
    ((0, 2), "Belgium", "Morocco"),
    ((4, 1), "Croatia", "Canada"),
    ((0, 0), "Croatia", "Belgium"),
    ((2, 1), "Morocco", "Canada"),
    ((1, 0), "Switzerland", "Cameroon"),
    ((2, 0), "Brazil", "Serbia"),
    ((3, 3), "Cameroon", "Serbia"),
    ((1, 0), "Brazil", "Switzerland"),
    ((2, 3), "Serbia", "Switzerland"),
    ((1, 0), "Cameroon", "Brazil"),
    ((0, 0), "Uruguay", "South Korea"),
    ((3, 2), "Portugal", "Ghana"),
    ((2, 3), "South Korea", "Ghana"),
    ((2, 0), "Portugal", "Uruguay"),
    ((0, 2), "Ghana", "Uruguay"),
    ((2, 1), "South Korea", "Portugal")
]


# Function to analyze the results
def analyze_results(matches):
    larger_wins = 0
    total_matches = len(matches)
    proportional_results = []

    for match in matches:
        score, team1, team2 = match
        pop1 = population[team1]
        pop2 = population[team2]
        score1, score2 = score

        if pop1 > pop2:
            if score1 > score2:
                larger_wins += 1
        elif pop2 > pop1:
            if score2 > score1:
                larger_wins += 1

        if score1 != 0 and score2 != 0:
            score_ratio = score1 / score2
            pop_ratio = pop1 / pop2
            proportional_results.append((score_ratio, pop_ratio))

    larger_win_percentage = (larger_wins / total_matches) * 100

    # Calculate correlation without using numpy
    if proportional_results:
        mean_score_ratio = sum([r[0] for r in proportional_results]) / len(proportional_results)
        mean_pop_ratio = sum([r[1] for r in proportional_results]) / len(proportional_results)

        numerator = sum((r[0] - mean_score_ratio) * (r[1] - mean_pop_ratio) for r in proportional_results)
        denominator_score = sum((r[0] - mean_score_ratio) ** 2 for r in proportional_results)
        denominator_pop = sum((r[1] - mean_pop_ratio) ** 2 for r in proportional_results)

        correlation = numerator / ((denominator_score * denominator_pop) ** 0.5)
    else:
        correlation = 0

    return larger_win_percentage, correlation

# Function to calculate expected scores based on inverse population ratios
def calculate_expected_scores(matches):
    expected_results = []
    
    for match in matches:
        score, team1, team2 = match
        pop1 = population[team1]
        pop2 = population[team2]
        
        # Calculate inverse population ratio
        inverse_pop_ratio = pop2 / pop1 if pop1 != 0 else 0
        
        # Calculate total goals scored in the match
        total_goals = score[0] + score[1]
        
        # If no goals were scored, keep the result as 0-0
        if total_goals == 0:
            expected_results.append((0, 0, team1, team2))
            continue
        
        # Calculate expected scores based on the inverse population ratio
        expected_score1 = total_goals * (pop2 / (pop1 + pop2))
        expected_score2 = total_goals * (pop1 / (pop1 + pop2))
        
        # Round the expected scores to the nearest whole number
        expected_score1 = round(expected_score1)
        expected_score2 = round(expected_score2)
        
        expected_results.append((expected_score1, expected_score2, team1, team2))
    
    return expected_results

# return the score for a given match prediction
def prediction_points(actual_result, prediction):
    if actual_result[0] == prediction[0] and actual_result[1] == prediction[1]:
        return 3  # 3 points for the correct score
    elif ((actual_result[0] > actual_result[1] and prediction[0] > prediction[1]) or
          (actual_result[0] < actual_result[1] and prediction[0] < prediction[1]) or
          (actual_result[0] ==actual_result[1] and prediction[0] ==prediction[1])):
        return 1  # 1 point for the correct result (win/lose/draw)
    else:
        return 0

# MAIN PROGRAM
matches = world_cup_2022_group_stage

# Analyze the results
larger_win_percentage, correlation = analyze_results(matches)

# Display the results
print(f"Larger country win percentage: {larger_win_percentage:.2f}%")
print(f"Correlation between score ratios and population ratios: {correlation:.2f}")

# Calculate expected scores for each match
expected_results = calculate_expected_scores(matches)

# Display the expected results
print("Expected results if scores were proportional to population size ratio of teams")
for result in expected_results:
    score1, score2, team1, team2 = result
    print(f"{team1} {score1} - {score2} {team2}")


# 1. Which prediction scores the most:
# 0-0, 1-1, 1-0, 0-1
print("\nUsing the same result for every match:")
possible_scores = [[0, 0], [1, 1], [0, 1], [1, 0]]
possible_points = [0, 0, 0, 0]
for match in matches:
    for i in range(len(possible_scores)):
        prediction = possible_scores[i]
        possible_points[i] += prediction_points(match[0], prediction)

for i in range(len(possible_scores)):
    print(possible_scores[i], ":", possible_points[i])

# 2. What would a random prediction score
# assuming we choose between 0 and 2 goals for each team, at random
total_random_points = 0.0
runs = 100000
upper_score = 1
print("\nChoosing the score at random (0-{}), averaged over {} runs:".format(upper_score, runs))
for _ in range(runs):
    random_points = 0
    for i in range(len(matches)):
        random_prediction = [random.randint(0, upper_score), random.randint(0, upper_score)]
        random_points += prediction_points(matches[i][0], random_prediction)
    total_random_points += random_points
    
print("Average score:", total_random_points/runs)
                                    
# 3. What would we score if we chose scores based on the inverse population size ratio of the teams
# (this correlation seems to be strongly supported by the results of this competition)
print("\nScores if we picked results based on population ratios (smaller countries do better):")
population_dependent_results = calculate_expected_scores(matches)

points = 0
for i in range(len(matches)):
    actual_result = matches[i][0]
    predicted_result = population_dependent_results[i]
    points += prediction_points(actual_result, predicted_result)
print("Total score:", points)
