import { readFileSync } from 'fs';

export const run = async () => {

    //On vient lire l'input et on le met dans une variable
    const input = readFileSync('./src/day_4/input.txt', 'utf-8');
    const sections = input.split('\n');

    let overlap = 0;
    let partialOverlap = 0;

    //On boucle sur chaque section et on compare avec les autres
    for(const section of sections) {
        const pair = section.split(',');
        const first = pair[0].split('-');
        const second = pair[1].split('-');

        const [as, ae, bs, be] = [+first[0], +first[1], +second[0], +second[1]];

        if ((as <= bs && ae >= be) || (as >= bs && ae <= be)) overlap++;
        if (ae >= bs && be >= as) partialOverlap++;

    }  

    return { overlap, partialOverlap };

};