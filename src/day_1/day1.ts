/**
 * Made by Valentin H.
 */
import { readFileSync } from 'fs';

export const run = async () => {
    // On met l'input dans une variable pour pouvoir itérer dessus
    const input = readFileSync('./src/day_1/input.txt', 'utf-8').split('\n');

    //On créé une classe Lutin pour que ce soit plus simple à gérer
    class Lutin {

        calories: number = 0;

        constructor(calories) {
            this.calories = calories;
        }

        getCalories(): number {
            return this.calories;
        }
    }

    //On créé une variable calorie qui comptera le nombre de calories de chaque lutin
    var calorie = 0;

    //On crée un tableau de Lutin car ils sont plusieurs 🎅
    var lutins: Lutin[] = [];

    /* 
        Maintenant on vient lire chaque ligne de l'input et on ajoute les calories à la variable calorie
        Si la ligne est vide, on créé un nouveau Lutin et on ajoute le nombre de calories qu'il transporte et on réinitialise la variable calorie
    */
    input.forEach(line => {
        parseInt(line) ? calorie += parseInt(line) : lutins.push(new Lutin(calorie)) && (calorie = 0);
    });

    //Maitenant on trie les lutins par ordre décroissant de calories
    lutins.sort((a, b) => b.getCalories() - a.getCalories());
    console.log("Le meilleur lutin transporte : " + lutins[0].getCalories() + " calories");

    //Et là on affiche la somme des calories transportées par les 3 meilleurs lutins en une seule ligne
    console.log("Le top 3 des lutins transporte : " + lutins.slice(0, 3).reduce((a, b) => a + b.getCalories(), 0)) + " calories");

    return 'done';
}
