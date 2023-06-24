import { useContext } from "react";
import { GreetingMessage } from "./App";

const Third = () => {
  const [greeting, setGreeting] = useContext(GreetingMessage);
  // // TODO:供給されているコンテキストを受け取る
  // const greeting = useContext(GreetingMessage);

  const handleRadio = (event) => {
    console.log(event.target.value);
    // 状態変数用の関数を使って実際に値を変更
    setGreeting({ message: event.target.value });
  };

  return (
    <div>
      {/* コンポーネント間で共有するデータをここで表示する */}
      <h3>第３階層コンポーネント:{greeting.message}</h3>
      <div>
        <label>
          はい
          <input type="radio" name="res" onChange={handleRadio} value="はい" />
        </label>
        <label>
          いいえ
          <input
            type="radio"
            name="res"
            onChange={handleRadio}
            value="いいえ"
          />
        </label>
      </div>
    </div>
  );
};
export default Third;
