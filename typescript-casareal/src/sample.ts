function leftover<T>(array: T[]): T[] {
  return array.slice(1, array.length);
}

const numArray = [10,20,30,40]

const resultArr1 = leftover<number>(numArray);
