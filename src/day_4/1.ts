import { readFileSync } from 'fs';

export const run = async () => {
  // Read input and split into sections
  const input = readFileSync('./src/day_4/input.txt', 'utf-8');
  const sections = input.split('\n');

  let overlap = 0;
  let partialOverlap = 0;

  // Loop over each section and compare with the other sections
  for (const section of sections) {
    const pair = section.split(',');
    const first = pair[0].split('-');
    const second = pair[1].split('-');

    // Destructure the start and end times for each section
    const [aStart, aEnd, bStart, bEnd] = [+first[0], +first[1], +second[0], +second[1]];

    // Check for overlap or partial overlap
    if ((aStart <= bStart && aEnd >= bEnd) || (aStart >= bStart && aEnd <= bEnd)) {
      overlap++;
    }
    if (aEnd >= bStart && bEnd >= aStart) {
      partialOverlap++;
    }
  }

  return { overlap, partialOverlap };
};