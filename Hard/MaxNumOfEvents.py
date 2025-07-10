events.sort()  # Sort by start day
    n = len(events)
    
    # Preprocess start days for binary search
    start_days = [e[0] for e in events]

    # Initialize DP table with zeros
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Fill table from bottom up
    for i in range(n - 1, -1, -1):
        # Binary search to find the next event after events[i]'s end
        next_index = bisect_right(start_days, events[i][1])
        for j in range(1, k + 1):
            # Option 1: skip event
            skip = dp[i + 1][j]
            # Option 2: take event
            take = events[i][2] + dp[next_index][j - 1]
            # Maximize
            dp[i][j] = max(skip, take)

    return dp[0][k]