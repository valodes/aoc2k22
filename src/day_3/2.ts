import { readFileSync } from 'fs';

type Compartiment = string[];
type ItemsMap = { [key: string]: number };

export const run = async () => {

    //On vient lire l'input et on le met dans une variable
    const input = readFileSync('./src/day_3/input.txt', 'utf-8').split('\n');

    const alphabetMap = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".split('');

    function countItemsInRucksack(compartment: Compartiment, itemsMap: ItemsMap) {
        compartment.forEach((item) => {
            if (!itemsMap.hasOwnProperty(item)) {
                itemsMap[item] = 0;
            }
            itemsMap[item]++;
        });
    }

    function getSumOfPriorities(repeatingItems: string[]): number {
        return repeatingItems
            .reduce((partialSum, item) => partialSum + getItemPriority(item), 0);
    }

    function getItemPriority(item: string): number {
        return alphabetMap.indexOf(item) + 1;
    }

    const repeatingItems: string[] = [];

    for (let i = 0; i < input.length; i += 3) {
        const rucksack1 = input[i].split('');
        const rucksack2 = input[i + 1].split('');
        const rucksack3 = input[i + 2].split('');

        const firstRucksackItems = {};
        const secondRucksackItems = {};
        countItemsInRucksack(rucksack1, firstRucksackItems);
        countItemsInRucksack(rucksack2, secondRucksackItems);

        for (let j = 0; j < rucksack3.length; j++) {
            const item = rucksack3[j];
            if (firstRucksackItems.hasOwnProperty(item) && secondRucksackItems.hasOwnProperty(item)) {
                repeatingItems.push(item);
                break;
            }
        }

    };

    return getSumOfPriorities(repeatingItems);

};