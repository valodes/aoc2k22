import { readFileSync } from 'fs';

export const run = async () => {

    //On vient lire l'input et on le met dans une variable
    const input = readFileSync('./src/day_3/input.txt', 'utf-8').split('\n');

    //Le résultat final qu'on va retourner à la fin
    let finalResult: number = 0;

    //Une fonction qui génère un alphabet de 26 lettres, on va l'utiliser pour générer les lettres de l'alphabet pour les scores
    function generateAlphabet(capital = false): string[] {
        return [...Array(26)].map((_, i) => String.fromCharCode(i + (capital ? 65 : 97)));
    }

    //On intialise notre alphabet complet avec une Map pour pouvoir accéder aux lettres par leur score
    const alphabetMap = new Map<string, number>();
    const alphabet = generateAlphabet().concat(generateAlphabet(true)).forEach((letter, index) => {
        alphabetMap.set(letter, index + 1);
    });

    input.forEach((line) => {

        //On ajoute le score à la variable finale 
        finalResult += alphabetMap.get(line.slice(0, line.length / 2).split('').find(letter => line.slice(line.length / 2).split('').includes(letter))!)!;

    });

    return finalResult;

};