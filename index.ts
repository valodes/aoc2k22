import { exit } from 'process';
import * as readline from 'node:readline/promises';

const args = process.argv.slice(2);

let daystorun: number = parseInt(args[0], 10);
let puzzletorun: number = parseInt(args[1], 10);

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

if (!daystorun) {
    daystorun = parseInt(await rl.question('which day do you want to run ? '), 10)
}

if (!puzzletorun) {
    puzzletorun = parseInt(await rl.question('which puzzle do you want to run ? '), 10)
}

const { run } = await import(`./src/day_${daystorun}/${puzzletorun}.ts`);
console.log(await run());
exit();