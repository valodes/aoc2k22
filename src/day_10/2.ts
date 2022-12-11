import { readFileSync } from "fs";

function printCrt(input: string[][]) : void {
    for (let i = 0; i < input.length; i++) {
        console.log(input[i].join(""));
    }
  }

export const run = () => {

    const input = readFileSync("./src/day_10/input.txt", "utf-8").split("\r\n");

    let cycle = 0;
    let x = 1;
    let pixelsVisible = [0, 1, 2];
    let line = 0;

    const crt = new Array(6).fill("░").map(() => new Array(40).fill("░"));

    input.forEach(instruction => {
        const instructionArray = instruction.split(" ");
        if (instructionArray[0] === "noop") {
            if (pixelsVisible.includes(cycle)) {
                crt[line][cycle] = "▓";
            }
            cycle += 1;
            if (cycle % 40 === 0) {
                cycle = 0;
                line += 1;
            }
        } else if (instructionArray[0] === "addx") {
            for (let i = 0; i < 2; i++) {
                if (pixelsVisible.includes(cycle)) {
                    crt[line][cycle] = "▓";
                }
                cycle += 1;
                if (cycle % 40 === 0) {
                    cycle = 0;
                    line += 1;
                }
                if (i === 1) {
                    const v = parseInt(instructionArray[1], 10);
                    x += v;
                    pixelsVisible = [x - 1, x, x + 1];
                }
            }
        }
    })

    return printCrt(crt);

};