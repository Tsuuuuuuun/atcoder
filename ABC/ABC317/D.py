N = int(input())
districts = [tuple(map(int, input().split())) for _ in range(N)]

def min_votes_to_win(N, districts):
    diffs = [(x - y, z) for x, y, z in districts]

    diffs.sort(reverse=True)
    
    total_seats = sum(z for _, z in diffs)
    required_seats = (total_seats // 2) + 1
    required_votes_to_win = 0
    current_seats = 0
    current_diff = 0

    for diff, z in diffs:
        if current_seats < required_seats:
            current_seats += z
            current_diff += diff


    required_votes_to_win = -current_diff // 2

    return max(0, required_votes_to_win)

print(min_votes_to_win(N, districts))