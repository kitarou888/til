import { useState } from "react";
import "./App.css";
import TaskBoard from "./TaskBoard";

function App() {
  const [cards, setCards] = useState(initialData);

  const addCard = (newCard) => {
    newCard.id = cards.length + 1;
    setCards([...cards, newCard]);
  };

  const handleClick = () => {
    addCard({ id: null, body: "新しい買い物", category: "テスト" });
  };

  return (
    <div>
      <h1>TASK LIST</h1>
      <button onClick={handleClick}>データ追加</button>
      <TaskBoard cards={cards} />
    </div>
  );
}

const initialData = [
  { id: 1, body: "お茶を買う", category: "今日やること" },
  // { id: 2, body: "牛乳を買う", category: "今日やること" },
  { id: 3, body: "あんぱんを買う", category: "今日やること" },
];

export default App;
