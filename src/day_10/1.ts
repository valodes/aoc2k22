import { readFileSync } from "fs";

export const run = () => {

    const input = readFileSync("./src/day_10/input.txt", "utf-8");

    const instructions: string[] = input.split("\n");

    let cycle = 0;
    let X = 1;
    const steps = [20, 60, 100, 140, 180, 220];

    return instructions
        .map((instruction) => {
            let strength = 0;

            if (instruction.split(" ")[0] == "addx") {
                if (steps.indexOf(++cycle) > -1) strength = cycle * X;
                if (steps.indexOf(++cycle) > -1) strength = cycle * X;
                X += parseInt(instruction.split(" ")[1]);
            } else {
                if (steps.indexOf(++cycle) > -1) strength = cycle * X;
            }

            return strength;
        })
        .reduce((a, c) => a + c);

};