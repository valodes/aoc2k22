import { readFileSync } from "fs";

export const run = () => {

  const input = readFileSync("./src/day_7/input.txt", "utf-8").split("\r\n");

  const dirMap = new Map<string, number>();

  let currentDir = "";

  for (let i = 0; i < input.length; i++) {

    if (input[i].startsWith("$")) {

      const words = input[i].split(" ");

      if (words[1] === "cd") {

        if (words[2] === "/") {
          currentDir = "";
        }

        else if (words[2] === "..") {

          const dir = currentDir.split("/");

          dir.pop();

          currentDir = dir.join("/");
        } else {

          currentDir += "/" + words[2];
        }
      } else if (words[1] === "ls") {


      }
    } else if (input[i].startsWith("dir")) {

      const words = input[i].split(" ");

      if (!dirMap.has(currentDir)) {
        dirMap.set(currentDir, 0);
      }
    } else {

      const words = input[i].split(" ");

      if (!dirMap.has(currentDir)) {
        dirMap.set(currentDir, 0);
      }

      dirMap.set(currentDir, dirMap.get(currentDir)! + parseInt(words[0]));

      const dirs = currentDir.split("/");

      for (let j = dirs.length - 1; j >= 0; j--) {

        const parentDir = dirs.slice(0, j).join("/");

        dirMap.set(parentDir, dirMap.get(parentDir)! + parseInt(words[0]));
      }
    }
  }

  let total = 0;

  dirMap.forEach((value, key) => {
    if (value <= 100000) {
      total += value;
    }
  });

  return total;

};