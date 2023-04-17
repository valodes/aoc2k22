#include <bits/stdc++.h>

using namespace std;

typedef unordered_map<string, unordered_map<string, int>> Graph;

class Valve
{
  int pressurePerMin;

public:
  Valve(int pressure) : pressurePerMin(pressure) {}

  int getPressure() const
  {
    return pressurePerMin;
  }
};

Graph nonZeros(Graph &bigGraph,
               const unordered_set<string> &importantKeys)
{
  for (const auto &[origin, dists] : bigGraph)
  {
    if (!importantKeys.count(origin))
    {
      for (const auto &[first, firstToOrigin] : dists)
      {
        for (const auto &[second, secondToOrigin] : dists)
        {
          if (first == second)
            continue;
          auto it = bigGraph[first].find(second);
          int current_dist = INT32_MAX;
          if (it != bigGraph[first].end())
          {
            current_dist = it->second;
          }
          bigGraph[first][second] = min(current_dist, firstToOrigin + secondToOrigin);
        }
      }
    }
  }

  Graph ret;
  for (const string &origin : importantKeys)
  {
    for (const string &dest : importantKeys)
    {
      auto it = bigGraph[origin].find(dest);
      if (it != bigGraph[origin].end())
      {
        ret[origin][dest] = it->second;
      }
    }
  }

  return ret;
}

pair<unordered_map<string, Valve>, Graph> parseInput(const vector<string> &lines)
{
  Graph bigGraph;
  unordered_set<string> keysToCareAbout{"AA"};
  unordered_map<string, Valve> valves;
  for (const string &line : lines)
  {
    const string key = line.substr(6, 2);
    int semicolon = line.find(';');
    const int pressure = stoi(line.substr(23, semicolon - 23));
    if (pressure > 0 || key == "AA")
    {
      keysToCareAbout.insert(key);
      valves.emplace(key, Valve(pressure));
    }
    int begin = line.find(' ', line.find('v', line.find(';'))) + 1;
    int end = begin + 2;
    while (end < line.size())
    {
      bigGraph[key][line.substr(begin, 2)] = 1;
      begin = end + 2;
      end = begin + 2;
    }
    bigGraph[key][line.substr(begin, 2)] = 1;
  }

  return {valves, nonZeros(bigGraph, keysToCareAbout)};
}

void findOptimal(const unordered_map<string, Valve> &valves, const Graph &graph,
                 unordered_set<string> &open, string current, long long &best, int time, int total_remaining, long long current_path)
{
  if (time <= 0 || total_remaining == 0)
  {
    best = max(best, current_path);
    return;
  }
  if (total_remaining * (time - 1) + current_path <= best)
  {
    return;
  }
  const auto &neighbors = graph.at(current);
  if (open.count(current) == 0 && time > 1)
  {
    const int currentPressure = valves.at(current).getPressure();
    const int pressureEarned = currentPressure * (time - 1);
    const long long pathWithCurrent = pressureEarned + current_path;
    const int remainingWithNoCurrent = total_remaining - currentPressure;
    open.insert(current);
    for (const auto &[dest, dist] : neighbors)
    {
      const int t = time - dist - 1;
      findOptimal(valves, graph, open, dest, best, t, remainingWithNoCurrent, pathWithCurrent);
    }
    open.erase(current);
  }
  for (const auto &[dest, dist] : neighbors)
  {
    const int t = time - dist;
    findOptimal(valves, graph, open, dest, best, t, total_remaining, current_path);
  }
}

void part1(vector<string> &lines)
{
  auto [valves, graph] = parseInput(lines);
  unordered_set<string> open;
  int total = 0;
  for (auto it = valves.begin(); it != valves.end(); ++it)
  {
    total += it->second.getPressure();
  }

  long long answer = 0ll;
  findOptimal(valves, graph, open, "AA", answer, 30, total, 0);

  cout << "PART 1: " << answer << endl;
}

void findOptimal2(const unordered_map<string, Valve> &valves, const Graph &graph,
                  unordered_set<string> &open, pair<string, int> playerState, pair<string, int> elephantState,
                  long long &best, int total_remaining, long long current_path)
{
  const int time = max(playerState.second, elephantState.second);
  if (time <= 0 || total_remaining == 0)
  {
    best = max(best, current_path);
    return;
  }
  if (total_remaining * (time - 1) + current_path <= best)
  {
    return;
  }
  string current;
  bool playerDecides = time == playerState.second;
  if (playerDecides)
    current = playerState.first;
  else
    current = elephantState.first;

  const auto &neighbors = graph.at(current);
  if (open.count(current) == 0 && time > 1)
  {
    const int currentPressure = valves.at(current).getPressure();
    const int pressureEarned = currentPressure * (time - 1);
    const long long pathWithCurrent = pressureEarned + current_path;
    const int remainingWithNoCurrent = total_remaining - currentPressure;
    open.insert(current);
    for (const auto &[dest, dist] : neighbors)
    {
      const int t = time - dist - 1;
      if (playerDecides)
      {
        findOptimal2(valves, graph, open, {dest, t}, elephantState, best, remainingWithNoCurrent, pathWithCurrent);
      }
      else
      {
        findOptimal2(valves, graph, open, playerState, {dest, t}, best, remainingWithNoCurrent, pathWithCurrent);
      }
    }
    open.erase(current);
  }
  for (const auto &[dest, dist] : neighbors)
  {
    const int t = time - dist;
    if (playerDecides)
    {
      findOptimal2(valves, graph, open, {dest, t}, elephantState, best, total_remaining, current_path);
    }
    else
    {
      findOptimal2(valves, graph, open, playerState, {dest, t}, best, total_remaining, current_path);
    }
  }
}

void part2(vector<string> &lines)
{
  auto [valves, graph] = parseInput(lines);
  unordered_set<string> open;
  int total = 0;
  for (auto it = valves.begin(); it != valves.end(); ++it)
  {
    total += it->second.getPressure();
  }

  long long answer = 0ll;
  findOptimal2(valves, graph, open, {"AA", 26}, {"AA", 26}, answer, total, 0);

  cout << "PART 2: " << answer << endl;
}

int main(int argc, char const *argv[])
{
  if (argc != 2)
  {
    cerr << "Invalid Usage. Usage: ./[binary] [input]" << endl;
    exit(EXIT_FAILURE);
  }

  string current;
  vector<string> lines;

  ifstream istr(argv[1]);

  while (getline(istr, current))
  {
    if (current == "\n")
      break;
    lines.push_back(current);
  }

  // part1(lines);
  part2(lines);

  return EXIT_SUCCESS;
}