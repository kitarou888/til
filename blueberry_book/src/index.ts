// type User = {
//   firstName: string,
//   lastName: string,
//   age: number,
//   favoriteFoods: string[],
//   hasProgrammingExperience: boolean,
// }
// const user: User = {
//   firstName: '太郎',
//   lastName: '山田',
//   age: 24,
//   favoriteFoods: ['寿司', 'ラーメン', 'カレー'],
//   hasProgrammingExperience: true,
// }

// function getSelfIntroduction(user: User): string {
//   return `私の名前は ${user.lastName} ${user.firstName} です。` +
//     `年齢は ${user.age} 歳です。` +
//     `好きな食べ物は ${user.favoriteFoods.join(' と ')} です。` +
//     `プログラミングの経験${user.hasProgrammingExperience ? 'があります。' : 'はありません。'}`
// }

// console.log(getSelfIntroduction(user))

// type User = { name: string };
// function getUserName(maybeUser: unknown): string | undefined {
//   if (typeof maybeUser !== 'object' || maybeUser === null) {
//     return undefined
//   }

//   const user = maybeUser as Record<keyof User, unknown>;

//   if (typeof user.name !== 'string') {
//     return undefined
//   }
//   return user.name
// }

// type Subject =
//   | { type: "name"; payload: string }
//   | { type: "favorite_food"; payload: string[] };

// function printSelfIntroduction(subject: Subject) {
//   switch (subject.type) {
//     case "name":
//       console.log(`私の名前は${subject.payload}です`);
//       return;
//     case "favorite_food":
//       console.log(`私の好きな食べ物は${subject.payload.join("と")}です`);
//       return;
//     default:
//       throw Error('ありません！')
//   }
// }

// function triple<T>(arg: T): T[] {
//   return [arg, arg, arg]
// }

// console.log(triple(123))

type Animal = { name: string };
type Dog = { name: string; forefoot: "前足" };
const dog: Dog = { name: "イヌ", forefoot: "前足" };

let dogToAnimal = (dog: Dog): Animal => dog;
// より部分な型は代入できる→返り値は部分が、引数はスーパーが入る
dogToAnimal = (dog: Dog): Dog => {
  return dog;
};

const animal: Animal = dogToAnimal(dog);

type D = { prop: { a: number } } & { prop: { b: string } };
type E = number & 12345;
type F = "love" & "peace";

// type Multiply = <a, b>(a * b)
