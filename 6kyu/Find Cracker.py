# Someone was hacking the score. Each student's record is given as an array The objects in the array are given again
# as an array of scores for each name and total score. ex>
#
# array = [
# ["name1", 445, ["B", "A", "A", "C", "A", "A"]],
# ["name2", 110, ["B", "A", "A", "A"]],
# ["name3", 200, ["B", "A", "A", "C"]],
# ["name4", 200, ["A", "A", "A", "A", "A", "A", "A"]]
# ]
# The scores for each grade is:
#
# A: 30 points B: 20 points C: 10 points D: 5 points Everything else: 0 points If there are 5 or more courses and all
# courses has a grade of B or above, additional 20 points are awarded. After all the calculations, the total score
# should be capped at 200 points.
#
# Returns the name of the hacked name as an array when scoring with this rule.
#
# array = [
# ["name1", 445, ["B", "A", "A", "C", "A", "A"]], # name1 total point is over 200 => hacked
# ["name2", 110, ["B", "A", "A", "A"]], #  name2 point is right
# ["name3", 200, ["B", "A", "A", "C"]] # name3 point is 200 but real point is 90 => hacked
# ["name4", 200, ["A", "A", "A", "A", "A", "A", "A"]] # name4 point is right
# ];
#
# return ["name1", "name3"]


arr = [
    ["name1", 445, ["B", "A", "A", "C", "A", "A"]],
    ["name2", 110, ["B", "A", "A", "A"]],
    ["name3", 200, ["B", "A", "A", "C"]],
    ["name4", 200, ["A", "A", "A", "A", "A", "A", "A"]]
]

grades = {'A': 30,
          'B': 20,
          'C': 10,
          'D': 5}


def is_hacked(result):
    name, total_score, scores = result
    high_grades = [score for score in scores if score in ['A', 'B']]
    bonus = len(high_grades) > 4 and len(high_grades) == len(scores)
    total = sum([grades[x] if x in grades else 0 for x in scores])
    total += 20 if bonus else 0
    if total > 200:
        total = 200
    return total != total_score


def find_hack(arr):
    hacker_results = [result for result in arr if is_hacked(result)]
    return [result[0] for result in hacker_results]


print(find_hack(arr))

# @ -> https://www.codewars.com/users/rokas2019/completed_solutions
# You can find version in which I've used (map, filter, lambda) functions
