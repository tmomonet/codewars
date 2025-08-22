def roll_value(roll: str, prev: str = None) -> int:
    """Convert a single roll symbol to its pin value."""
    if roll == "X":     # Strike
        return 10
    elif roll == "/":   # Spare → 10 minus previous roll
        return 10 - int(prev)
    elif roll == "-":   # Miss
        return 0
    else:               # Number
        return int(roll)


def score_frame(frame: list[str], next_rolls: list[str]) -> int:
    """Score one frame including bonuses."""
    if frame == ["X"]:  # Strike
        bonus = sum(roll_value(r, next_rolls[i-1] if r == "/" else None)
                    for i, r in enumerate(next_rolls[:2]))
        return 10 + bonus
    elif "/" in frame:  # Spare
        next_roll = next_rolls[0] if next_rolls else "0"
        return 10 + roll_value(next_roll, frame[0])
    else:               # Open frame
        return sum(roll_value(ch) for ch in frame)


def bowling_score(frames: str) -> int:
    rolls = [ch for frame in frames.split(" ") for ch in frame]
    eachBall = [list(frame) for frame in frames.split(" ")]

    score = 0
    roll_index = 0
    for i, frame in enumerate(eachBall):
        next_rolls = rolls[roll_index+len(frame):]
        if i == 9:  # 10th frame, score raw
            score += sum(roll_value(ch, frame[idx-1] if ch == "/" else None)
                         for idx, ch in enumerate(frame))
        else:       # frames 1–9, normal scoring
            score += score_frame(frame, next_rolls)
        roll_index += len(frame)
    return score

# Community Solution
# def bowling_score(frames):
#     rolls = list(frames.replace(' ',''))
#     for i, hit in enumerate(rolls):
#         if hit == 'X':
#             rolls[i] = 10
#         elif hit == '/':
#             rolls[i] = 10 - rolls[i - 1]
#         else:
#             rolls[i] = int(hit)
#     score = 0
#     for i in range(10):
#         frame = rolls.pop(0)
#         if frame == 10:
#             score += frame + rolls[0] + rolls[1]    # Strike!
#         else:
#             frame += rolls.pop(0)
#             score += frame
#             if frame == 10:
#                 score += rolls[0]                   # Spare!
#     return score
