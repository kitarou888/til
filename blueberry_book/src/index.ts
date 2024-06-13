import { readFileSync } from "fs";
import path from "path";
import { fileURLToPath } from "url";

const execDir = path.parse(import.meta.url).dir;
// console.log(path.join(fileURLToPath(execDir), "../uhyo.txt"));
const filePath = path.join(fileURLToPath(execDir), "../uhyo.txt");

const text: string = readFileSync(filePath, "utf8");
// const text: string = readFileSync("uhyo.txt", "utf8"); // 実行場所によってファイルパスを変えないといけない

let position = text.indexOf("uhyo");
let count = 0;

while (position !== -1) {
  count++;
  position = text.indexOf("uhyo", position + 1);
}

console.log(count);
