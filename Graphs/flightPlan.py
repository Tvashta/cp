# Question
# Note: Try to solve this task in O(m log n) time, where n is a number of cities and m is a number of flights,
# since this is what you'll be asked to do during an interview.

# Elle is trying to arrange a flight from source to dest.
# She doesn't mind taking multiple connecting flights, but wants to get to her destination dest as soon as possible.
# She has a timetable of flights, times, where:

# times[i][0] is the starting location of flight i,
# times[i][1] is the destination for flight i,
# times[i][2] is the time flight i departs,
# times[i][3] is the time flight i arrives.
# The earliest Elle can leave is midnight(00: 00). All times have been encoded as HH: MM.
# All times are referenced in the timezone of the source, where the hours HH are bigger than 23 if the time is on a subsequent day.

# Given the timetable times, source, and dest, return the time when Elle will arrive at dest,
# if she wants to get here as soon as possible, or "-1" if it's impossible. For her flights:

# Assume they all leave and arrive on time.
# She needs 60 minutes between flights.

# Though this question sounds really complicated it is a simple Dijikstra problem
# Flights are edges, cities are nodes and times are weights

from collections import defaultdict
import heapq


def time(s):
    (h, m) = map(int, s.split(':'))
    return h*60+m


def flightPlan(times, source, dest):
    adj = defaultdict(lambda: [])
    for i in times:
        adj[i[0]].append([i[1], time(i[2]), time(i[3])])
    h = []
    d = defaultdict(lambda: float('inf'))
    d[source] = 0
    heapq.heappush(h, [0, source])
    while h:
        s = heapq.heappop(h)
        if s[1] == dest:
            return "%02d:%02d" % (s[0]//60 - 1, s[0] % 60)
        for j in adj[s[1]]:
            if j[1] >= d[s[1]]:
                if d[j[0]] > j[2]+60:
                    heapq.heappush(h, [j[2]+60, j[0]])
                    d[j[0]] = j[2]+60
    return '-1'
