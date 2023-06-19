import { useState, useEffect } from "react";
import "./App.css";
import TaskBoard from "./TaskBoard";

const App = () => {
  const [cards, setCards] = useState(null);

  useEffect(() => {
    const fetchCards = async () => {
      try {
        const response = await fetch("http://localhost:8080/cards");
        if (!response.ok)
          throw new Error(`${response.status} ${response.statusText}`);
        const data = await response.json();
        setCards(data);
      } catch (error) {
        console.error(error);
        window.alert(error);
      }
    };
    fetchCards();
  }, []);

  const postNewCard = async (newCard) => {
    const fetchOptions = {
      method: "POST",
      body: JSON.stringify(newCard),
      header: { "Content-Type": "application/json" },
    };
    try {
      const response = await window.fetch(
        "http://localhost:8080/cards",
        fetchOptions
      );
      if (!response.ok)
        throw new Error(`${response.status} ${response.statusText}`);
      window.alert(`タスクカード：${newCard.body}を登録しました`);
    } catch (error) {
      console.error(error);
      window.alert(error);
    }
  };

  const addCard = (newCard) => {
    newCard.id = cards.length + 1;
    postNewCard(newCard);
    setCards([...cards, newCard]);
  };

  const handleClick = () => {
    addCard({ id: null, body: "新しい買い物", category: "テスト" });
  };

  return (
    <div>
      <h1>TASK LIST</h1>
      <button onClick={handleClick}>データ追加</button>
      {cards ? <TaskBoard cards={cards} addCard={addCard} /> : "読み込み中"}
    </div>
  );
};

export default App;
