import { useContext } from "react";
import { GreetingMessage } from "./App";

const Brother = () => {
  const [greeting, setGreeting] = useContext(GreetingMessage);
  // // TODO:供給されているコンテキストを受け取る
  // const greeting = useContext(GreetingMessage);

  return (
    <div>
      {/* コンポーネント間で共有するデータをここで表示する */}
      <p>兄弟コンポーネント:{greeting.message}</p>
    </div>
  );
};
export default Brother;
