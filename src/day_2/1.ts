import { readFileSync } from 'fs';

export const run = async () => {

    //On vient lire l'input et on le met dans une variable
    const input = readFileSync('./src/day_2/input.txt', 'utf-8').split('\n');

    //On stocke le score final dans une variable
    var finalScore: number = 0;

    //On itère sur chaque ligne de l'input, car 1 ligne = 1 tour
    for (var i: number = 0; i < input.length; i++) {

        const firstPlay: string = input[i].split(' ')[0];
        const secondPlay: string = input[i].split(' ')[1];

        /**
         * (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
         */
        switch (firstPlay) {
            case 'A': //Cas de la pierre chez le Lutin
                if (secondPlay.includes('X')) { // Cas de la pierre
                    finalScore += 4;
                } else if (secondPlay.includes('Y')) { //Cas du papier
                    finalScore += 8;
                } else if (secondPlay.includes('Z')) { //Cas du ciseau
                    finalScore += 3;
                }
                break;
            case 'B': //Cas du papier chez le Lutin
                if (secondPlay.includes('X')) { // Cas de la pierre
                    finalScore += 1;
                } else if (secondPlay.includes('Y')) { //Cas du papier
                    finalScore += 5;
                } else if (secondPlay.includes('Z')) { //Cas du ciseau
                    finalScore += 9;
                }
                break;
            case 'C': //Cas du ciseau chez le Lutin
                if (secondPlay.includes('X')) { // Cas de la pierre
                    finalScore += 7;
                } else if (secondPlay.includes('Y')) { //Cas du papier
                    finalScore += 2;
                } else if (secondPlay.includes('Z')) { //Cas du ciseau
                    finalScore += 6;
                }
                break;
        }

    }

    return finalScore;

}