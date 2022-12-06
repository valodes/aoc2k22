import { readFileSync } from "fs";

function findStartOfPacketMarker(dataStreamBuffer) {
    // Keep track of the last four characters received
    let lastFourChars: Buffer[] = [];

    // Loop through the characters in the datastream buffer
    for (let i = 0; i < dataStreamBuffer.length; i++) {
        // Add the current character to the lastFourChars array
        lastFourChars.push(dataStreamBuffer[i]);

        // If the lastFourChars array has more than four characters, remove the first character
        if (lastFourChars.length > 14) {
            lastFourChars.shift();
        }

        // Check if the lastFourChars array contains only unique characters
        if (new Set(lastFourChars).size === 14) {
            // Return the number of characters processed
            return i + 1;
        }
    }

    // If no start-of-packet marker is found, return -1
    return -1;
}

export const run = async () => {

    const input = readFileSync('./src/day_6/input.txt');

    const numCharsProcessed = findStartOfPacketMarker(input);

    return numCharsProcessed;
};