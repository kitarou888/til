function leftover<T>(array: T[]): T[] {
  return array.slice(1, array.length);
}

const numArray = [10,20,30,40]

const resultArr1 = leftover<number>(numArray);


function takeOne<A extends R[], R>(target: A): R {
  if (Array.isArray(target)) {
    return target[0];
  } else {
    throw new Error();
  }
}

const array1 = ['ABC', 'DEF', 'GHE', 'JKL'];
const array2 = [1, 2, 3, 4];
takeOne<string[], string>(array1);
takeOne<string[], number>(array2);
