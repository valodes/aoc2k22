import { readFileSync } from 'fs';

export const run = async () => {

    const lutinScores = {'A': {'X': 3,'Y': 4,'Z': 8},'B': {'X': 1,'Y': 5,'Z': 9},'C': {'X': 2,'Y': 6,'Z': 7}}
    return readFileSync('./src/day_2/input.txt', 'utf-8').split('\n').reduce((acc, curr) => {return acc + lutinScores[curr[0]][curr[2]];}, 0);

}
