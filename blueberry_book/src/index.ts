import { readFileSync } from "fs";

const text: string = readFileSync("./uhyo.txt", "utf8");

let position = text.indexOf("uhyo");
let count = 0;

while (position !== -1) {
  count++;
  position = text.indexOf("uhyo", position + 1);
}

console.log(count);
