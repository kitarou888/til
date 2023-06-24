import { useState } from "react";

const useTaskCardsState = (initialData) => {
  // useStateを使い状態と状態更新用関数を得る
  // （既存のフック関数を内部で利用していることがカスタムフック関数の条件）
  const [cards, setCards] = useState(initialData);

  // 指定されたカテゴリーの全タスクカードを返すカスタム関数
  const getCategorizedTaskCards = (targetCategory) => {
    const categorizedCards = cards.filter(
      (card) => card.category === targetCategory
    );
    return categorizedCards;
  };

  // タスクカードを1つ追加するカスタム状態更新用関数
  const addCard = (cardBody, targetCategory) => {
    const newCard = {
      id: cards.length + 1,
      body: cardBody,
      category: targetCategory,
    };
    setCards([...cards, newCard]);
  };

  return {
    getCategorizedTaskCards,
    addCard,
  };
};

export default useTaskCardsState;
