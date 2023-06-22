import { useContext } from 'react';
import { GreetingMessage } from './App';

const Third = () => {
  // TODO:供給されているコンテキストを受け取る
  const greeting = null;

  const handleRadio = (event) => {
    console.log(event.target.value);
    // （その２での）TODO：ここは後で書きます
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
          <input type="radio" name="res" onChange={handleRadio} value="いいえ"/>
        </label>
      </div>
    </div>
  );
};
export default Third;
